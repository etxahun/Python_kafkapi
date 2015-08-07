from kafka import KafkaConsumer

# To consume messages
consumer = KafkaConsumer('idiraspberrypi', 
			 group_id='nextel', 
			 bootstrap_servers=['kfk-kafka01:9092'])

for message in consumer:
    print("%s:%d:%d: key=%s value=%s" % (message.topic, 
					 message.partition, 
					 message.offset, 
					 message.key, 
					 message.value))
