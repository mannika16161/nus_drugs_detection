# nus_fire_detection

 - A mesh network of microbits is laid down in the forest area. Each microbit is connected to a variety of sensors like : temperature, humidity, amount of Carbon Monoxide and Nitrogen Dioxide in the air, wind speed etc.
 - Microbits communicate with each other using radio signals.
 - Sensor data along with the unique microbit id is send across the mesh to the raspberry pi with acts as a gateway. The network has been developed in a way that the data reaches the gateway even in situations when some mictro bits have been damaged as well as we have made sure that the data is accepted by the gateway only once. 
 - A machine learning model has been trained from existing forest fire datasets.
 - Based on the received sensor data a prediction is made if the forest fire can occur.
 - Moreover the direction of the fire is predicted using the wind direction and microbits location.
 
