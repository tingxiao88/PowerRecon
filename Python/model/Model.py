import datetime
import json
import cv2
import mediapipe as mp

# from socketIO_client import SocketIO, LoggingNamespace

# from peekingduck.pipeline.model import yolo
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
import socketio

sio = socketio.Client()

sio.connect('http://localhost:4000')

@sio.on('python_connection')
def connection():
    print(f"I'm connected! text from the server:")
    connection_return_package = {
        'current-temp': '29',
        'optimun_temp': '22',
        'aircon-fan' : '4',
        'aircon-temp' : '20',
    }

    frames = 0
    counter = 0
    cap = cv2.VideoCapture(0)
    with mp_face_detection.FaceDetection(
            model_selection=1, min_detection_confidence=0.4) as face_detection:
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                # If loading a video, use 'break' instead of 'continue'.
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
                print(frames)
                print('reaching 30')
                print(f"I'm connected! text from the server:")
                connection_return_package = {
                    'current-temp': '29',
                    'optimun_temp': '22',
                    'aircon-fan': '4',
                    'aircon-temp': '20',
                }
                print('Returning File')
                connection_return_package['time'] = str(datetime.datetime.now())
                connection_return_package['person'] = counter
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
