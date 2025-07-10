# ZeroMQ test
This is a simple test for ZeroMQ using Python.
It demonstrates how to set up a ZeroMQ server and client, send messages, and handle them asynchronously.

# ZeroMQ Setup
- Add the ZeroMQ repository to your system:
  ```bash
    echo 'deb http://download.opensuse.org/repositories/network:/messaging:/zeromq:/release-stable/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/network:messaging:zeromq:release-stable.list
  ```
  ```bash
    curl -fsSL https://download.opensuse.org/repositories/network:messaging:zeromq:release-stable/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/network_messaging_zeromq_release-stable.gpg > /dev/null
  ```
- Update your package list:
  ```bash
    sudo apt update
  ```
- Install ZeroMQ:
  ```bash
    sudo apt install libzmq3-dev
  ```

# Requirements
- Python 3.x
- ZeroMQ library for Python (pyzmq)
- Install dependencies using pip:
  ```bash
  pip3 install pyzmq
  ```
# Usage
1. Start the Subscribe:
  ```bash
  python3 main_sub(5555).py
  ```
2. Start the Publish:
  ```bash
  python3 pub.py
  ```
