import datetime
import json
import cv2
import mediapipe as mp
import pandas as pd
import socketio


df_temp = pd.read_csv('../Data/TempData2.csv').drop('Unnamed: 0', axis=1)

# import mediapipe model from google
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

sio = socketio.Client()

sio.connect('https://video-stream-mlda.herokuapp.com/')

@sio.on('python_connection')
def connection():
    print(f"I'm connected!")

    temp_count = 0
    frames = 0
    counter = 0
    cap = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(
            # the best parameters based on the room lighting
            model_selection=1, min_detection_confidence=0.4) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue
            # Flip the image horizontally for a later selfie-view display, and convert
            # the BGR image to RGB.
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            # To improve performance, optionally mark the image as not writeable to
            # pass by reference.
            image.flags.writeable = False
            results = face_detection.process(image)

            # Draw the face detection annotations on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            font = cv2.FONT_HERSHEY_SIMPLEX
            counter = 0
            if results.detections:
                for detection in results.detections:
                    mp_drawing.draw_detection(image, detection)
                    counter += 1
            if counter == 0:
                cv2.putText(image, f"Switch: OFF", (50, 300),
                            font, 2, (0, 255, 0), 5)
            else:
                cv2.putText(image, f"Switch: ON", (50, 300),
                            font, 2, (0, 255, 0), 5)
            cv2.putText(image, f"Person: {counter}",
                        (50, 500), font, 2, (0, 0, 255), 5)
            img = cv2.resize(image, (1920, 1080))
            cv2.imshow('MediaPipe Face Detection', img)
            frames = frames + 1
            if frames > 30:
                # counter for mock temperature data
                temp_count = temp_count + 1
                if temp_count > 500:
                    temp_count = 0

                # start the returning of the data to our webapp
                connection_return_package = {
                    'current-temp': 29,
                    'optimun_temp': 22,
                    'aircon-fan': 4,
                    'aircon-temp': 20,
                }
                print('Returning File')
                connection_return_package['current-temp'] = int(float(df_temp.loc[temp_count].values))
                connection_return_package['time'] = str(datetime.datetime.now())
                connection_return_package['person'] = counter
                connection_return_package['well_cooled'] = 'false'

                # fan control logic
                current_temp = connection_return_package['current-temp']
                optimun_temp = connection_return_package['optimun_temp']
                aircon_fan = connection_return_package['aircon-fan']
                aircon_temp = connection_return_package['aircon-temp']

                difference = float(connection_return_package['current-temp']) - float(connection_return_package['optimun_temp'])
                if difference > 10:
                    aircon_fan = 5
                    aircon_temp = current_temp - 10
                if  8<difference<10:
                    aircon_fan = 4
                    aircon_temp = current_temp - 10
                if  6<difference<8:
                    aircon_fan = 4
                    aircon_temp = current_temp - 10
                if  4<difference<6:
                    aircon_fan = 3
                    aircon_temp = current_temp - 8
                if  2<difference<4:
                    aircon_fan = 2
                    aircon_temp = current_temp - 6
                if  0<difference<2:
                    aircon_fan = 2
                    aircon_temp = current_temp - 4
                if  difference<0:
                    aircon_fan = 1
                    aircon_temp = current_temp + 1
                if -1<difference<1:
                    connection_return_package['well_cooled'] = 'true'
                if aircon_temp < 18:
                    aircon_temp = 18
                if connection_return_package['person'] == 0:
                    aircon_fan = 'OFF'
                    aircon_temp = 'OFF'

                # update the dictionary
                connection_return_package['aircon-temp'] = aircon_temp
                connection_return_package['aircon-fan'] = aircon_fan


                # print(connection_return_package)
                json_file = json.dumps(connection_return_package)
                print(json_file)
                frames = 0
                sio.emit('data_back', json_file)
                print('finished')
            # print(f"PERSON DETECTED: {counter}")
            if cv2.waitKey(1) & 0xFF == 'q':
                break



    cap.release()
