from util import connect_subscriber, recv_message, close_sockets
import time

def main():
    # Subscriber로 연결
    # topics = ["recv"]
    # connect_subscriber(topics, port="5556")  # 특정 토픽 구독
    connect_subscriber(port="5556")  # 모든 메시지 수신

    print("메시지 수신 대기 중...")

    while True:
        try:
            # 메시지 수신
            result = recv_message()

            if result:
                # topic, message = result
                print(f"수신된 메시지: {result}")

            time.sleep(0.5)

        except KeyboardInterrupt:
            print("\n프로그램 종료...")
            close_sockets()  # 정리
            break
        except Exception as e:
            print(f"오류 발생: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()

# from util import MessageQueue
# import time

# def main():
#     # MessageQueue 인스턴스 생성
#     with MessageQueue() as mq:
#         # Subscriber로 연결
#         topics = ["recv"]
#         mq.connect_subscriber(topics, 5556)  # 특정 토픽 구독
#         # mq.connect_subscriber("recv")
#         # mq.connect_publisher()

#         print("메시지 수신 대기 중...")

#         while True:
#             try:
#                 # 메시지 수신
#                 result = mq.recv_message("recv")

#                 if result:
#                     topic, message = result
#                     print(f"수신된 메시지: {topic} - {message}")

#                     # 메시지 처리 후 잠시 대기 (선택사항)

#                 time.sleep(0.5)

#             except KeyboardInterrupt:
#                 print("\n프로그램 종료...")
#                 break
#             except Exception as e:
#                 print(f"오류 발생: {e}")
#                 time.sleep(1)  # 오류 발생 시 1초 대기 후 재시도

# if __name__ == "__main__":
#     main()