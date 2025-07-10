import zmq

def topic_msg_handler(topic, msg):
    """토픽과 메시지를 받아서 처리하는 함수"""
    if topic == "test":
        print(f"정확히 'test' 토픽만 수신: {msg}")
    else:
        print(f"무시된 토픽: {topic}, 메시지: {msg}")

def main():
    ctx = zmq.Context()
    s = ctx.socket(zmq.SUB)
    s.bind("tcp://*:5555")
    s.setsockopt(zmq.SUBSCRIBE, b"test")  # "test"로 시작하는 모든 토픽 구독

    try:
        while True:
            topic, msg = s.recv_multipart()
            topic_str = topic.decode('utf-8')
            msg_str = msg.decode('utf-8')
            topic_msg_handler(topic_str, msg_str)
    except KeyboardInterrupt:
        pass
    finally:
        s.close()
        ctx.term()

if __name__ == "__main__":
    main()
