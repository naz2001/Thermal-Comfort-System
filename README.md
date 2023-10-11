# Thermal-Comfort-Main-Project

This Python code is used to implement an IoT-based thermal comfort prediction system. The system uses a variety of sensors, including temperature, humidity, ultrasonic, and video cameras, to collect data about the environment and the individual. This data is then used to predict the individual's thermal comfort level using machine learning models and various APIs.

The system is designed to be used in a variety of settings, including smart buildings, offices, and homes. It can be used to optimize the environment for thermal comfort, which can lead to increased productivity and efficiency.

# Thermal Comfort IoT System

Thermal Comfort is an IoT and machine learning-based system designed to personalize and optimize thermal comfort in indoor environments. The system collects data from environmental sensors, such as temperature, humidity, and ultrasonic sensors, to continuously monitor and adjust the environmental conditions. Additionally, video cameras are used to capture individual data, including age, gender, clothing, and activity, which are crucial factors influencing thermal sensation.

The project employs various machine learning models and API integrations to provide accurate predictions for clothing, activity, age, and gender based on real-time data. This holistic approach to thermal comfort prediction takes into account both physiological and psychological factors, resulting in precise and reliable results.

## Features

- Real-time data collection from environmental sensors.
- Video camera integration for individual data capture.
- Machine learning models for predicting clothing, activity, age, and gender.
- Personalized thermal comfort optimization.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Raspberry Pi with required sensors and cameras.
- Python 3.7 or higher.
- Libraries and dependencies listed in the code.
- API keys for third-party services (Everypixel, Sightengine, Roboflow).

### Installation

1. Clone this repository.

   ```sh
   git clone https://github.com/yourusername/thermal-comfort-iot.git


### Installation

To install the code, you will need the following Python packages:

* Adafruit_DHT
* azure.iot.device
* requests
* json
* cv2
* roboflow
* RPi.GPIO

Once you have installed the required packages, you can clone the code repository to your local machine:
git clone https://github.com/YOUR_USERNAME/thermal-comfort-prediction-system.git

Usage
To use the code, you will need to create an IoT Hub account and obtain a connection string. You will also need to install the required sensors and connect them to your Raspberry Pi. Once you have configured the system, you can start it by running the following command:

python thermal_comfort_prediction_system.py

The system will start capturing data from the sensors and predicting the individual's thermal comfort level. The results of the prediction will be sent to the IoT Hub.

Thermal Comfort Prediction Method
The thermal comfort prediction method used in this system is based on the following factors:

* Age
* Gender
* Activity level
* Clothing
* Temperature
* Humidity
* Air velocity
The system uses a machine learning model to predict the individual's thermal sensation, which is a measure of how comfortable they feel. The thermal sensation is then used to predict the individual's thermal comfort level, which is classified as one of the following:

* Cold
* Cool
* Comfortable
* Warm
* Hot
Benefits of the System
The proposed system offers the following benefits:

* Improved thermal comfort for individuals
* Increased productivity and efficiency
* Reduced energy consumption
* Reduced greenhouse gas emissions

This IoT-based thermal comfort prediction system can be used to improve the thermal comfort of individuals in a variety of settings. The system is accurate and efficient, and it can be easily deployed and scaled.
