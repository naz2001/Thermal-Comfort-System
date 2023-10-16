# Thermal Comfort System
<p align="justify"> 
Thermal comfort is an emerging variable that plays a crucial role in maximizing human productivity and creating livable environments. This project combines the power of Internet of Things (IoT) and machine learning to create a personalized model for thermal comfort. It utilizes environmental sensors, such as temperature and humidity sensors, along with video cameras to gather data on individual activities, clothing, age, and gender. These factors are essential for understanding an individual's thermal sensation.
  
Thermal comfort systems have the potential to be used in a variety of settings, such as homes, offices, schools, and hospitals, to improve thermal comfort and productivity.The project was my main project for my Bachelor of Technology in Computer Science and Engineering degree under APJKTU.  
</p>

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Software and Hardware Used](#software-and-hardware-used)
- [APIs and Machine Learning Models](#apis-and-machine-learning-models)
- [Scope](#scope)
- [Results](#results)
- [License](#license)

## Introduction
<p align="justify"> 
Thermal comfort is a critical factor in ensuring the well-being and productivity of individuals. Traditional HVAC systems often adopt a one-size-fits-all approach, disregarding individual preferences and physiological variations. As a result, occupants may experience discomfort or dissatisfaction with the indoor thermal conditions.

IoT and ML can be used to develop personalized thermal comfort prediction systems that consider individual factors such as age, gender, activity level, and clothing. These systems can continuously monitor the environment and adapt the HVAC settings accordingly, ensuring optimal comfort levels for all occupants.
</p>

## Project Overview

<p align="justify"> 
The primary objective of this project is to develop a sophisticated system that can create personalized models for thermal comfort. These models are capable of considering a variety of factors, including environmental conditions, individual activities, clothing choices, age, and gender.
</p>

## Key Features

- Real-time monitoring of environmental conditions (temperature, humidity, air velocity).
- Activity, clothing, age, and gender prediction using machine learning models.
- Personalized thermal comfort prediction for each individual.
- Integration of IoT devices for data collection.
- Data visualization and reporting.

## How It Works
<p align="justify"> 
The project utilizes a network of sensors, including temperature, humidity, and ultrasonic sensors, to continuously collect environmental data. A camera is used to capture data on individual activities, clothing, age, and gender, which are vital factors in determining thermal comfort. A thermal comfort prediction model has been trained on a dataset of thermal comfort data collected from a variety of individuals under different environmental conditions. The model takes into account a variety of factors, including environmental conditions, individual activities, clothing choices, age, and gender.

Machine learning models and various APIs are employed to predict clothing, activity, age, and gender-based on real-time data captured by the camera. The thermal comfort prediction model combines all the data to provide precise and accurate thermal comfort predictions, taking into account psychological and physiological factors. The system will continuously capture data, predict thermal comfort, and send the results to the Azure IoT Hub. The data and results are visualized in the PowerBI dashboard.
</p>

## Software and Hardware Used
- Raspberry Pi
- Raspberry Pi camera module 2, DHT11, and ultrasonic sensor.
- Python 3.7 or higher.
- Libraries and dependencies listed in the code.
- API keys for third-party services (Everypixel, Sightengine, Roboflow).
- PowerBI

<p align="center">
<img src="https://github.com/naz2001/Thermal-Comfort-Main-Project/assets/57052959/ea29ad4b-7c26-4c76-b9b0-857a377d1f20" width="500" height="300" align="center">
</p>
<p align="justify"> 

Figure shows the
final connections between the different components used in the system. The camera module
is connected to the camera slot on the Raspberry Pi. A GPIO extension board is fitted on the
breadboard and to these pins the sensors are connected. The DHT11 sensor uses GPIO pin
no:4. A 10K ohm resistor is placed between the VCC and the data pin of the DHT11, to act as a
medium-strength pull-up on the data line. Connections are placed from the VCC, data, and Gnd
pin to the GPIO extension board. The ultrasonic sensor uses pins 23 and 24 as trigger and echo
respectively. Resistors are used between the ultrasonic sensor's connection to the GPIO
board. This is done to protect the Raspberry Pi GPIO pins as the ultrasonic sensor outputs a 5V
signal, which can damage the Raspberry Pi GPIO pins. The connection of the ultrasonic sensor to
the GPIO board is as follows:
- Connect the positive wire from the sensor to the 5V pin on the Raspberry Pi GPIO extension
board.
- Connect the negative wire from the sensor to the ground pin on the board.
- Connect a resistor between the echo pin on the ultrasonic sensor and the GPIO pin on the
Raspberry Pi GPIO extension board. Two 1K ohm resistors are used in series.
- Connect a second resistor between the trigger pin on the ultrasonic sensor and the GPIO
pin on the board. A 1K ohm resistor is used.
</p>

## APIs and Machine Learning Models
* Everypixel: Used for age prediction
* Sightengine: Used for gender prediction 
* Roboflow: Used for activity and clothing prediction
* Comfort Prediction API: A custom API for calculating thermal comfort ( https://github.com/naz2001/Thermal-Comfort-API )

## Scope
<p align="justify"> 

Implementing IoT with thermal comfort systems has fueled the demand for
these systems in commercial and residential applications. Systems can be used in areas where
low initial costs and simplified installations are important. High investments are made in infrastructure
development. This has increased the demand for HVAC systems to remove pollutants,
maintain quality, and control the temperature and humidity in a building. Studies say that 30%
of total energy usage in buildings is due to HVAC systems. Thermal comfort systems help
increase the efficiency of energy usage and consumption.
The system can be used by:

- Young children and the elderly: Maintaining an optimal thermal environment is crucial for their well-being. Extreme cold or inadequate heating can pose a higher risk for hypothermia in these vulnerable populations. Monitoring their thermal comfort and responding to their specific needs can help prevent thermal discomfort and the associated health risks.
- Offices and workplaces: Thermal comfort plays a crucial role in office/workplace environments and can have a significant impact on employee productivity and well-being. The ability to control thermal conditions within these spaces is essential to ensure optimal comfort for employees.

- Educational institutions: Thermal comfort is a crucial factor in educational institutions, as it can significantly impact the learning environment and the well-being of students and staff. Controlling thermal comfort in educational institutions involves implementing various measures to ensure optimal conditions.
- Hotels and smart homes: Achieving optimal thermal comfort is crucial in both hotels and smart homes as it directly influences the comfort and satisfaction of guests and residents. The effective control of thermal comfort in these environments requires the implementation of diverse measures.
- Hospitals and nursing homes: Thermal comfort plays a critical role in hospitals and nursing homes as it directly impacts the well-being and recovery of patients, as well as the comfort of staff and residents. Controlling thermal comfort in these settings involves implementing specific systems and measures to ensure optimal conditions.
</p>

## Results
<p align="center">
<img src="https://github.com/naz2001/Thermal-Comfort-Main-Project/assets/57052959/5d603858-e4fc-405d-9b15-02cbbbc3ea19" >
</p>

<p align="justify"> 

The final output of the system is presented using the Power BI dashboard, enabling easy interpretation
and visualization of the predicted thermal comfort indices. The system categorizes
thermal comfort into five levels, ranging from ”Comfortable” to ”Highly Uncomfortable”. This
information can be used by occupants, facility managers, or HVAC control systems to make informed
decisions and adjust the indoor conditions accordingly. Figure shows a model of the
dashboard created using Power BI. A line chart has been used to show the varying thermal
comfort, temperature, humidity, and air velocity values levels with respect to time. Pie charts
have been used to show the distributions of age, clothing, and activity. A table has been used
to show the thermal comfort values with respect to time.
</p>

## License
This project is licensed under the MIT License - see the LICENSE file for details.
