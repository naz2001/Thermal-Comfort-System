import random  
import Adafruit_DHT
import time
from azure.iot.device import IoTHubDeviceClient, Message 
import requests
import json
import cv2
import requests
from sklearn.preprocessing import LabelEncoder
from roboflow import Roboflow
import RPi.GPIO as GPIO
import Adafruit_DHT
#////////////////////////////////////////////////////capture image////////////////////////////////////////////////////////////////////
#the camera shall take pictures every 1 minutes or so
def capture_image(image_path):    
    # Initialize the webcam
    print("Taking image")
    cap = cv2.VideoCapture(0)  # 0 represents the default webcam, change it if necessary
    # Capture the image from the webcam
    ret, frame = cap.read()
    # Save the captured image to a file
    #image_path = 'capture.jpg'  # Path to save the captured image
    cv2.imwrite(image_path, frame)
    # Close the webcam
    cap.release()
    
def run_api_calls():
    image_path = 'capture.jpg'  # Path to save the captured image
    capture_image(image_path)
    # Set GPIO mode
    GPIO.setmode(GPIO.BCM)
    # Ultrasonic sensor pins
    TRIG_PIN = 23
    ECHO_PIN = 24
    # DHT11 sensor
    DHT_PIN = 4
    # Set ultrasonic sensor pins as output and input
    GPIO.setup(TRIG_PIN, GPIO.OUT)
    GPIO.setup(ECHO_PIN, GPIO.IN)
    def measure_distance():
        # Send ultrasonic pulse
        GPIO.output(TRIG_PIN, GPIO.HIGH)
        GPIO.output(TRIG_PIN, GPIO.LOW)
        # Wait for echo start
        while GPIO.input(ECHO_PIN) == GPIO.LOW:
            pulse_start = time.time()
        # Wait for echo end
        while GPIO.input(ECHO_PIN) == GPIO.HIGH:
            pulse_end = time.time()
        # Calculate pulse duration
            pulse_duration = pulse_end - pulse_start
        # Calculate distance (speed of sound in air: 343m/s)
            distance = pulse_duration * 34300 / 2
        return distance

    def measure_temperature_humidity():
        # Read temperature and humidity from DHT11 sensor
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHT_PIN)
        return temperature, humidity
    
    def calculate_air_velocity():
        # Measure distance from ultrasonic sensor
        distance = measure_distance()
        # Measure temperature and humidity from DHT11 sensor
        temperature, humidity = measure_temperature_humidity()
        # Calculate speed of sound
        speed_of_sound = 331.4 + 0.606 * temperature + 0.0124 * humidity
        # Calculate air velocity
        air_velocity = distance / speed_of_sound
        return air_velocity
 

#////////////////////////////////////////////////////Age///////////////////////////////////////////////////////////////////////////////
    client_id = 'xxxxxxxxxxxxx'
    client_secret = 'xxxxxxxxxxxxx'
    params = {'url': 'https://labs.everypixel.com/api/static/i/estest_sample3.jpg'}
    quality = requests.get('https://api.everypixel.com/v1/faces', params=params, auth=(client_id, client_secret)).json()
# Perform the API request with the captured image
    with open(image_path, 'rb') as image:
        data = {'data': image}
        quality = requests.post('https://api.everypixel.com/v1/faces', files=data, auth=(client_id, client_secret)).json()
        #print(quality)
        age1 = quality['faces'][0]['age']
        #age1 = round(age, 0)
        #print("Age:",age1)    
        if age1 < 11:
            age = "0"
        elif 11<= age1 < 20:
            age = "1"
        elif 21<= age1 < 30:
            age = "2"
        elif 31<= age1 < 40:
            age = "3"
        elif 41<= age1 < 50:
            age = "4"
        elif 51<= age1 < 60:
            age = "5"
        elif 61<= age1 < 70:
            age = "6"
        elif 71<= age1 < 80:
            age = "7"
        else:
            age = "8"
    print("Age:", age)
#/////////////////////////////////////////////////////gender////////////////////////////////////////////////////////////////////////////
    params = {
        'models': 'faces,face-attributes',
        'api_user': 'xxxxxxxxxxxxx',
        'api_secret': 'xxxxxxxxxxxxx'
    }
    files = {'media': open(image_path, 'rb')}
# Make the API request
    response = requests.post('https://api.sightengine.com/1.0/check.json', files=files, data=params)
    output = json.loads(response.text)
    print(output)
    female_score = output['faces'][0]['attributes']['female']
    male_score = output['faces'][0]['attributes']['male']
    if female_score > male_score:
        gender = '0'
    else:
        gender = '1'
    print("Gender:", gender)
#///////////////////////////////////////////////////activity//////////////////////////////////////////////////////////////////////////
    rf = Roboflow(api_key="xxxxxxxxxxxxx")
#for activity model
    project1 = rf.workspace().project("action-detection-zt808")
    model1 = project1.version(5).model
# infer on a local image
#print(model1.predict("teacher.png", confidence=40, overlap=30).json())
    pred1=model1.predict(image_path, confidence=40, overlap=30).json()
    if not pred1['predictions']:
        activity='2'
    else:
        predicted_class1 = pred1["predictions"][0]["class"]
# Print the predicted class
    #print("Predicted Class:", predicted_class1)
        if predicted_class1 == 'sitting':
            activity='2'
        elif predicted_class1 == 'standing':
            activity='3'
        else:
            activity='4'    
        print(activity)
#////////////////////////////////////////////////////////////clothing//////////////////////////////////////////////////////////////////
#for clothing model
    project2 = rf.workspace().project("clothing-detection-ev04d")
    model2 = project2.version(3).model
# infer on a local image
    predicted_classes2 = []
    pred2=model2.predict(image_path, confidence=40, overlap=30).json()
    #print(pred2)
    #output = {'predictions': [], 'image': {'width': '640', 'height': '480'}}
    if not pred2['predictions']:
        clothing=12
    else:
        for i in range(2):
            predicted_class = pred2["predictions"][i]["class"]
            predicted_classes2.append(predicted_class)
            print(predicted_classes2)
            predicted_classes2 = ['pants', 'shirt', 'tshirt', 'kurta', 'churidhaar', 'sari']
            # Define a custom encoding dictionary
            encoding_dict2 = {
                'pants': 1,
                'shirt': 2,
                'tshirt': 4,
                'kurta': 5,
                'churidhaar': 6,
                'sari': 8  
                }
        # Perform custom encoding
            encoded_classes2 = [encoding_dict2[class_name] for class_name in predicted_classes2]
        # Join the encoded values to create a two-digit value
            clothing = encoded_classes2[0] * 10 + encoded_classes2[1]
            print(clothing)
#///////////////////////////////////////////////////////thermal comfort model//////////////////////////////////////////////////////////
# Define the API endpoint URL
    velocity = calculate_air_velocity()
    temperature, humidity = measure_temperature_humidity()
            # Print the results
    print("Temperature: ",temperature)
    print("Humidity: ",humidity)
    print("Air Velocity:",velocity)
    url = 'https://comfort-prediction.onrender.com/comfort_prediction'
    age=age
    gen=gender
    ct=activity
    cl=clothing
    t=temperature
    h=humidity
    w=velocity
    # Define the request payload as a dictionary
    payload = {
    'Age': age,
    'Gender': gen,
    'CurrentActivity': ct,
    'Clothing': cl,
    'Temperature': t,
    'Humidity': h,
    'WindSpeed': w
    }
# Convert the payload to JSON
    json_payload = json.dumps(payload)
# Set the request headers
    headers = {'Content-Type': 'application/json'}
# Send the POST request
    response = requests.post(url, data=json_payload, headers=headers)
# Check the response status code
    if response.status_code == 200:
    # Request was successful
        result = response.json()
        print(result)
    else:
    # Request failed
        print('Error:', response.status_code)

    #sensor = Adafruit_DHT.DHT11
    CONNECTION_STRING = "HostName=xxxxxxxxxxxxx;DeviceId=xxxxxxxxxxxxx;SharedAccessKey=xxxxxxxxxxxxx"  
    MSG_SND = '{{"temperature": {temperature},"humidity": {humidity},"velocity":{velocity},"age":{age},"gender":{gender},"activity":{activity},"clothing":{clothing},"result":{result}}}'  
    #while True:
        #humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    def iothub_client_init():
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)  
        return client  
    def iothub_client_telemetry_sample_run():  
        #try:
        client = iothub_client_init()  
        print ( "Sending data to IoT Hub, press Ctrl-C to exit" )  
        
        
        msg_txt_formatted = MSG_SND.format(temperature=temperature, humidity=humidity, velocity=velocity, age=age, gender=gender, activity=activity, clothing=clothing, result=result)  
        message = Message(msg_txt_formatted)  
        print( "Sending message: {}".format(message) )  
        client.send_message(message)  
        print ( "Message successfully sent" )  
        time.sleep(3)  
           # except KeyboardInterrupt:  
            #    print ( "IoTHubClient stopped" )  
        #if _name_ == '_main_':  
         #   print ( "Press Ctrl-C to exit" )
         
    iothub_client_telemetry_sample_run()


#////////////////////////////////////////////start of execution./////////////////////////////
max_retries =3

while True:
    retry_count=0
    while retry_count<max_retries:
        try:
            run_api_calls()
            break
        except Exception as e:
            print(f"Error :{e}")
            retry_count+=1
            if retry_count < max_retries:
                print(f" Retrying image capture...(Attempt{retry_count+1})")
                time.sleep(1)
            else:
                print("Maximum retries reached.Exiting...")
    if retry_count==max_retries:
        print("Image capture failed after maximun retries")
    print("Wait for next image capture")    
    time.sleep(15)        
    print("Wait over")
