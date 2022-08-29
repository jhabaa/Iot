# Iot
 Projet IoT : Réseau de capteurs. 

Des capteurs de température, de pression, de luminosité et d'humidité sont placés sur une breadboard. Par l'intermédaire d'un ADC (MCP3008), nous recoltons les données sur un Raspberry.

Le Raspberry à traves la bibliothèque Adafruit de Python lit les valeurs de tensions de l'ADC. Nous envoyons continuellement ces valeurs par blocs vers notre broker MQTT tournant sous RabbitMQ.

Il suffit ensuite de créer un socket, qui à chaque fois qu'une donnée sera récoltée sur le broker, l'enverra au client. 
