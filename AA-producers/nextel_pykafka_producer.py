from pykafka import KafkaClient

client = KafkaClient(hosts="kfk-kafka01:9092")
topic = client.topics['idiraspberrypi']
producer = topic.get_producer()
producer.produce(['Kaixo Nextel from pykafka!'])
