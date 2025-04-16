# Predictive Maintenance Dashboard (with Ignition + ML)
Simulate machine sensor data, predict failures using a simple machine learning model, and display live predictions and alerts in an Ignition dashboard.

Repository Structure: 
```
ignition-ml-predictive-maintenance/
├── data_simulator/
│   └── simulate.py
├── ml_model/
│   ├── train_model.py
│   └── model.pkl
├── api_server/
│   └── app.py
├── ignition_dashboard/
│   └── dashboard_instructions.md
├── requirements.txt
└── README.md
```

### Task 1: Simulate Sensor Data

- Create `simulate.py` that generates time-series CSV files:
    
    ```python
    # generate rows with timestamp, temperature, humidity
    # failure label = 1 if temp > 80 and humidity > 80 for example
    
    ```
    
- Stream this data periodically using Python to:
    - A CSV file (`output.csv`)
    - An MQTT topic or a tag update script (depends on integration)
> Hint: Check out [this tutorial](https://dev.blues.io/guides-and-tutorials/collecting-sensor-data/notecarrier-pi/raspberry-pi/python/) on simulating sensor data with raspberry Pis

### Task 2: Train ML Model

- Use the simulated data to train a simple binary classifier (e.g., logistic regression or random forest)
- Input: `temperature`, `vibration`
- Output: `failure_risk` (0 or 1)
- Save the model as `model.pkl` using `joblib`
> Hint: [This](https://medium.com/@thommaskevin/tinyml-random-forest-classifier-and-regressor-b351aa0980e8) is a great tutorial on using a light random forest model. 

### Task 3: Create API for Model

- Build a Flask API in `api_server/app.py`:
    - `POST /predict` route that takes JSON data like `{ "temp": 75, "vib": 3.4 }`
    - Returns prediction like `{ "failure_risk": 1 }`
- Test using curl or Postman
> Hint: [Here's a tutorial](https://projects.raspberrypi.org/en/projects/python-web-server-with-flask) for building a 

### Task 4: Ignition Integration

- Pull sensor data from the simulator (via MQTT)
- Create a Perspective dashboard:
    - Show temperature and vibration gauges
    - Display the model’s predicted failure risk (via HTTP request or tag)
    - Set up a red alert box when failure risk = 1
  > Hint 1: [Here's a tutorial]([https://www.instructables.com/Installing-MQTT-BrokerMosquitto-on-Raspberry-Pi/](https://core-electronics.com.au/guides/getting-started-with-mqtt-on-raspberry-pi-pico-w-connect-to-the-internet-of-things/)) on using MQTT with the Raspberry Pi.
  > Hint 2: [This video](https://inductiveautomation.com/resources/video/using-the-mqtt-transmission-module-to-publish-data) provides a tutorial for integrating MQTT with Ignition. 

### Task 5: Connect Everything

- Automate data flow:
    - `simulate.py` sends data to Flask API and updates Ignition tags
    - Flask returns failure prediction → store as `Prediction/FailureRisk` tag
- Ensure Ignition displays real-time status

### Task 6: Documentation & GitHub Polish

- Fill in `README.md`:
    - Project overview
    - Setup instructions (Python + Ignition)
    - Screenshot or gif of dashboard
- Create a simple setup guide for others: `dashboard_instructions.md`

---
