from pykafka import KafkaClient

client = KafkaClient(hosts="kfk-kafka01:9092")
topic = client.topics['idiraspberrypi']

consumer = topic.get_simple_consumer()
for message in consumer:
    if message is not None:
        print message.offset, message.value
