import json
import time
import zmq

# 전역 변수로 socket과 context 관리
_context = zmq.Context()
_context.setsockopt(zmq.LINGER, 0)  # 소켓이 닫힐 때 대기하지 않도록 설정

# _pub_socket = None    // Publisher 소켓은 필요할때마다 생성 후
_sub_socket = None
_host = "localhost"

def connect_publisher(port="5555"):
    # global _pub_socket

    # if _pub_socket is not None:
    #     return _pub_socket

    _pub_socket = _context.socket(zmq.PUB)
    _pub_socket.connect(f"tcp://{_host}:{port}")
    # print(f"Publisher connected to {_host}:{port}")
    time.sleep(0.5)

    return _pub_socket

def connect_subscriber(port="5555"):
    global _sub_socket

    if _sub_socket is not None:
        return _sub_socket

    _sub_socket = _context.socket(zmq.SUB)
    _sub_socket.bind(f"tcp://{_host}:{port}")
    _sub_socket.subscribe("")  # 모든 메시지 수신

    print(f"Subscriber bound to {_host}:{port} - All messages")
    return _sub_socket

def send_message(msg, port="5555"):
    _pub_socket = connect_publisher( port)

    if _pub_socket:
        msg_bytes = msg.encode("utf8") if isinstance(msg, str) else msg
        _pub_socket.send(msg_bytes)  # 단일 part로 전송
        print(f'Sent message: {msg}')
        time.sleep(0.1)
        _pub_socket.close()

def recv_message():
    global _sub_socket

    if _sub_socket:
        msg = _sub_socket.recv()  # 단일 part 수신
        msg_str = msg.decode('utf-8')
        # print(f'Received message: {msg_str}')
        return msg_str

# def connect_subscriber(topic="", host="localhost", port="5555"):
#     global _sub_socket

#     if _sub_socket is not None:
#         return _sub_socket

#     _sub_socket = _context.socket(zmq.SUB)
#     _sub_socket.bind(f"tcp://{host}:{port}")

#     if isinstance(topic, list):
#         for t in topic:
#             _sub_socket.subscribe(t)
#             print(f"Subscribed to topic: {t}")
#     else:
#         _sub_socket.subscribe(topic)

#     print(f"Subscriber bound to {host}:{port}")
#     return _sub_socket

# def send_message(msg_topic, msg, host="localhost", port="5555"):
#     # global _pub_socket

#     # if _pub_socket is None:
#         # connect_publisher(host, port)

#     _pub_socket = connect_publisher(host, port)

#     if _pub_socket:
#         topic_bytes = msg_topic.encode("utf8") if isinstance(msg_topic, str) else msg_topic
#         msg_bytes = msg.encode("utf8") if isinstance(msg, str) else msg

#         _pub_socket.send_multipart([topic_bytes, msg_bytes])
#         print(f'Sent message: {msg_topic} - {msg}')
#         time.sleep(0.1)
#         _pub_socket.close()
#     else:
#         print("Publisher socket is not connected.")

# def recv_message(expected_topic=None):
#     global _sub_socket

#     if _sub_socket:
#         topic, msg = _sub_socket.recv_multipart()
#         topic_str = topic.decode('utf-8')
#         msg_str = msg.decode('utf-8')

#         if expected_topic and topic_str != expected_topic:
#             print('Not Matching Topic:', topic_str)
#             send_message(topic_str, msg_str)
#             return None
#         return topic_str, msg_str

def close_sockets():
    # global _pub_socket, _sub_socket, _context
    global _sub_socket

    # if _pub_socket:
    #     _pub_socket.close()
    #     _pub_socket = None

    if _sub_socket:
        _sub_socket.close()
        _sub_socket = None