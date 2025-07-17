import time
from util import send_message, close_sockets

def main():
    count = 0

    while True:
        try:
            # 메시지 전송
            send_message("test", "Hello, World! Count: {}".format(count), port="5555")
            # 잠시 대기
            time.sleep(0.5)
            send_message("recv", "pub.py Count: {}".format(count), port="5556")
            time.sleep(0.5)
            count += 1

        except KeyboardInterrupt:
            print("\n프로그램 종료...")
            close_sockets()  # 리소스 정리
            break
        except Exception as e:
            print(f"오류 발생: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()

# import time
# from util import MessageQueue


# def main():
#     with MessageQueue() as mq:
#         # mq.connect_publisher()

#         count = 0

#         while True:
#             try:
#                 # 메시지 전송
#                 mq.send_message("test", "Hello, World! Count: {}".format(count), 5555)
#                 # 잠시 대기
#                 time.sleep(0.5)
#                 mq.send_message("recv", "Hello, World! Count: {}".format(count), 5556)
#                 time.sleep(0.5)
#                 count += 1

#             except KeyboardInterrupt:
#                 print("\n프로그램 종료...")
#                 break
#             except Exception as e:
#                 print(f"오류 발생: {e}")
#                 time.sleep(1)

# if __name__ == "__main__":
#     main()