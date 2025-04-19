# chat_client.py

import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

HOST = '127.0.0.1'
PORT = 55555

nickname = ""

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
            else:
                text_area.config(state='normal')
                text_area.insert('end', message + '\n')
                text_area.yview('end')
                text_area.config(state='disabled')
        except:
            break

def write():
    message = f'{nickname}: {input_field.get()}'
    client.send(message.encode('utf-8'))
    input_field.delete(0, tk.END)

# GUI setup
window = tk.Tk()
window.title("Mini Chat App")

text_area = scrolledtext.ScrolledText(window)
text_area.pack(padx=10, pady=5)
text_area.config(state='disabled')

input_field = tk.Entry(window, width=50)
input_field.pack(padx=10, pady=5)

send_button = tk.Button(window, text="Send", command=write)
send_button.pack()

nickname_prompt = tk.Tk()
nickname_prompt.withdraw()
nickname = simpledialog.askstring("Nickname", "Enter your nickname:", parent=nickname_prompt)

receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

window.mainloop()
