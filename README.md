# NTU MLDA-Hackathon Submission - PowerRecon

PowerRecon is the solution that our team (DoggoIpsum) is submitting for the NTU MLDA-Hackathon.
The Solution is an AI-based camera system that is able to detect humans in the compound and be able to intelligently change and regulate the compound's temperature and air-conditioning fan speed.

## Usage

1. Navigate to the project directory
2. Start up the Node Server by typing ```node server.js```
3. Activate the Conda environment by typing ```conda activate PowerRecon```
4. Once the environment is up and running, run the ```model.py``` file inside the Python folder.
5. In any web browser, open up ```http://localhost:4000``` to view the dashboard.


## Dependancies

**JavaScript Dependencies**

- Express.JS
- Socket.IO
- HTTP

```bash
## Run the command below to install the necessary dependancies
npm i express socket.io http
```


**Python Dependencies**

- mediapipe
- python-socketio[client]
- opencv-python
- datetime
- json

```bash
## Run the command below to install all necessary dependencies
conda create --name PowerRecon python==3.8
pip install -r requirements.txt
```

## Contributors
- [Kah Shin](https://www.github.com/angks)
- [Ting Xiao](https://www.github.com/tingxiao69)
- [Yu Hoe](https://www.github.com/tyh71)
