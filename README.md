# Simple Python Messenger App

A simple **multi-client chat server** built in **Python** using **sockets**, **threads**, and a **Tkinter GUI**. The app allows multiple clients to connect to a server, exchange messages in real-time, and display them in an easy-to-use graphical interface.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## Description

This project is a basic implementation of a **multi-client chat system**. It allows you to:
- **Server**: Listens for incoming client connections, assigns them a nickname, and broadcasts messages to all clients.
- **Client**: Sends and receives messages from the server using a GUI built with Tkinter. Each client can send a message, and they will see messages sent by other clients in real-time.

## Features

- **Real-time messaging**: Messages appear immediately on all connected clients.
- **Multi-client support**: Multiple clients can connect to the server at the same time.
- **GUI interface**: A simple chat interface with an input box for messages and a chat area to see conversation history.
- **Simulated server responses**: A mock server response is added to simulate interaction.

## Installation

### Prerequisites

You need to have **Python** installed on your system. Download the latest version of Python from [here](https://www.python.org/downloads/).

### Steps to Install

1. Clone this repository to your local machine using:

   ```bash
   git clone https://github.com/Mahima-5/python-messenger-app.git
   ```

2. Change into the project directory:

   ```bash
   cd python-messenger-app
   ```

3. Install any required dependencies (no additional dependencies are needed other than Python’s built-in libraries).

   **Important**: Tkinter comes pre-installed with Python, but if you don't have it, you can install it using the following:

   - **Linux** (Debian-based distributions like Ubuntu):

     ```bash
     sudo apt-get install python3-tk
     ```

   - **Windows/macOS**: Tkinter is bundled with Python, so no extra steps are needed.

## Usage

### Running the Server

1. Open a terminal window and navigate to the project directory.
2. Run the server script to start listening for incoming client connections:

   ```bash
   python chat_server.py
   ```

   You should see the following output when the server is running:

   ```
   Server is running and listening...
   ```

### Running the Client

1. Open a new terminal window and navigate to the project directory.
2. Run the client script to start the chat client:

   ```bash
   python chat_client.py
   ```

3. The client will prompt you for a **nickname**. After entering your nickname, the main chat window will open, allowing you to start sending messages.

4. You can now open as many clients as you like (in separate terminals), and they will all be able to chat with each other.

### Chatting
- Type a message in the **"You:"** field and click the **Send** button to send the message.
- You will see both your message and simulated server responses in the chat area.

To exit the chat, type **"exit"** in the input field.

## Technologies Used

- **Python 3.x** for the implementation.
- **Tkinter** for the graphical user interface.
- **Sockets** for client-server communication.
- **Threading** to handle multiple clients concurrently.

## Contributing

If you’d like to contribute to this project, feel free to fork the repository, make changes, and submit a pull request. I’m always open to suggestions for improvements or new features.
