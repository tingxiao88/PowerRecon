# NTU MLDA-Hackathon Submission - PowerRecon

> PowerRecon is the solution that our team (Doggo Ipsum) is submitting for the NTU MLDA-Hackathon.

The Solution is an AI-based camera system that is able to detect humans in the compound and be able to intelligently change and regulate the compound's temperature and air-conditioning fan speed.

---

## Usage

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

- Express.JS
- Socket.IO
- HTTP

```bash
## Run the command below to install the necessary dependancies
npm i express socket.io http
```

### Python Dependencies

- mediapipe
- python-socketio
- opencv-python
- datetime
- json

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
