import json
import time
import zmq

class MessageQueue:
    def __init__(self, host="localhost", port="5555"):
        self.context = zmq.Context()
        self.pub_socket = None
        self.sub_socket = None
        self.host = host
        self.sub_port = port
        self.pub_port = port

    def connect_publisher(self, pub_port=None):
        if(pub_port is not None):
            self.pub_port = pub_port

        self.pub_socket = self.context.socket(zmq.PUB)
        self.pub_socket.connect(f"tcp://{self.host}:{self.pub_port}")
        print(f"Publisher connected to port {self.pub_port}")

    def connect_subscriber(self, topic="", sub_port=None):
        if(sub_port is not None):
            self.sub_port = sub_port

        self.sub_socket = self.context.socket(zmq.SUB)
        self.sub_socket.bind(f"tcp://{self.host}:{self.sub_port}")

        if( isinstance(topic, list) and topic):
            for t in topic:
                self.sub_socket.subscribe(t)
                print(f"Subscribed to topic: {t}")
        else:
            self.sub_socket.subscribe(topic)

        print(f"Subscriber connected to port {self.sub_port}")

    def send_message(self, msg_topic, msg, pub_port=None):
        self.connect_publisher(pub_port)

        time.sleep(0.1)  # Wait for the subscriber to connect

        if self.pub_socket:
            topic_bytes = msg_topic.encode("utf8") if isinstance(msg_topic, str) else msg_topic
            msg_bytes = msg.encode("utf8") if isinstance(msg, str) else msg

            self.pub_socket.send_multipart([topic_bytes, msg_bytes])
            print(f'Sent message: {msg_topic} - {msg}')
        else:
            print("Error: Publisher socket not connected")

        self.pub_socket.close()
        # time.sleep(0.1)  # Wait for the message to be sent before closing

    def recv_message(self, expected_topic=None):
        if self.sub_socket:
            topic, msg = self.sub_socket.recv_multipart()
            topic_str = topic.decode('utf-8')
            msg_str = msg.decode('utf-8')

            if expected_topic and topic_str != expected_topic:
                print('Not Matching Topic:', topic_str)
                # 이제 다른 소켓으로 재전송 가능
                self.send_message(topic_str, msg_str)
                return None
            return topic_str, msg_str

    def close(self):
        if self.pub_socket:
            self.pub_socket.close()
        if self.sub_socket:
            self.sub_socket.close()
        self.context.term()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()