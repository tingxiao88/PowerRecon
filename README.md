# NTU MLDA-Hackathon Submission - PowerRecon

![PowerRecon Logo](public/BW%20Transparent.png)

PowerRecon is the solution that our team (Doggo Ipsum) is submitting for the NTU MLDA-Hackathon.

---

## About the Project

PowerRecon is a computer vision based solution, consisting of a object detection based camera system that is able to detect the presense of humans in the compound and be able to intelligently change and regulate the compound's temperature and air-conditionaing fan speed.

---

## Getting Started

1. Navigate to the project

```bash
cd <Directory>
```

2. Start up the Node Server

```bash
node server.js
```

3. Activate the Conda environment by typing

```bash
conda activate PowerRecon
```

4. Once the environment is up and running, run the ```model.py``` file inside the Python folder.

```bash
## Ensure Environment is up 
python model.py
```

5. In any web browser, open up ```http://localhost:4000``` to view the dashboard.

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

All of us are from the Diploma of Applied AI and Artficial Intelligence, Singapore Polytechnic's School of Computing.

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
