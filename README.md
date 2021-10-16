# NTU MLDA-Hackathon Submission - PowerRecon

![PowerRecon Logo](public/BW%20Transparent.png)

PowerRecon is the solution that our team (73 Doggo Ipsum) is submitting for the NTU MLDA-Hackathon.

---

## About the Project

PowerRecon is a computer vision based solution, consisting of a object detection based camera system that is able to detect the presense of humans in the compound and be able to intelligently change and regulate the compound's temperature and air-conditionaing fan speed.

[Web Page hosted on Heroku](https://video-stream-mlda.herokuapp.com/)

---

## Getting Started

1. Navigate to the project directory

```bash
cd <Directory>
```

1. Start up the Express.js server (It is a prerequisite that **Node.js** is installed )

```bash
npm i ## Run this command only if the packages are not installed
node server.js
```

1. Activate the Conda virtual environment and install python dependencies

```bash
## Only do this step once
conda create --name PowerRecon python==3.8
conda activate PowerRecon
pip install -r requirements.txt
```

4. Once the environment is up and running, run the ```model.py``` file inside the Python folder. There should be another window displaying a  **video feed** and a **face detection bounding box**.

```bash
## Ensure Environment is up 
python model.py
```

5. ⚠️ **Important Note**: For the sake of this demonstration (and the lack of time to do further development), we used **OBS Studio** to broadcast the window via a virtual camera client provided.

    - Open OBS Studio -> Go to Virtual camera -> Select MediaPipe Window -> Start Virtual Camera
    - Go to this URL [https://video-stream-mlda.herokuapp.com/broadcast.html](https://video-stream-mlda.herokuapp.com/broadcast.html), ensure to allow camera on the browser
    - Direct browser camera to the virtual camera by OBS Studio (Ensure that it captures MediaPipe Video Feed)
    - The video feed will be broadcasted live to the [Dashboard](https://video-stream-mlda.herokuapp.com/).

6. In any web browser, open up ```http://localhost:4000``` or the [host web page](https://video-stream-mlda.herokuapp.com/) to view the dashboard.

---

## Dependancies

### JavaScript Dependencies

| Packages | Documentation Links |
| --- | --- |
| Express.JS | [Docs](https://expressjs.com/) |
| Socket-IO | [Docs](https://socket.io/) |
| HTTP | [Docs](https://nodejs.org/api/http.html) |

```bash
## Run the command below to install the necessary dependancies
npm install express socket.io http
```

### Python Dependencies

| Libraries | Documentation Links |
| --- | --- |
| mediapipe | [Docs](https://mediapipe.dev/) |
| python-socketio | [Docs](https://python-socketio.readthedocs.io/en/latest/) |
| opencv-python | [Docs](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html) |
| datetime | - |
| json | - |

```bash
## Run the command below to install all necessary dependencies
conda create --name PowerRecon python==3.8
pip install -r requirements.txt
```

---

## Contributors

- [Ang Kah Shin](https://www.github.com/angks)
- [Shi Ting Xiao](https://www.github.com/tingxiao69)
- [Tan Yu Hoe](https://www.github.com/tyh71)

All of us are from the Diploma of Applied AI and Artificial Intelligence, Singapore Polytechnic's School of Computing.

---

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
