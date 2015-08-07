from kafka import SimpleProducer, KafkaClient

kafka = KafkaClient('kfk-kafka01:9092')
producer = SimpleProducer(kafka)

producer.send_messages(b'idiraspberrypi', b'Kaixo Nextel from kafka-python!')
