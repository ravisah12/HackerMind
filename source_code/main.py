import tkinter as tk
from tkinter import scrolledtext

def send_message():
    user_input = entry.get()
    if user_input.strip():
        chat_area.insert(tk.END, f"You: {user_input}\n")
        chat_area.insert(tk.END, f"HackerMindAI: (This is a mock response)\n\n")
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("HackerMindAI v1.0.0 - Created by Ravi Sah")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

chat_area = scrolledtext.ScrolledText(root, bg="#252526", fg="#d4d4d4", font=("Segoe UI", 10))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Segoe UI", 10))
entry.pack(padx=10, pady=(0,10), fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=(0,10))

chat_area.insert(tk.END, "📘 HackerMindAI – A Multi-Agent GPT Intelligence Framework\n👨‍💻 Created by: Ravi Sah\n🧠 Booting distributed AI agents...\n⚠️ Status: Experimental Build | Use with caution.\n🗓️ Version: 1.0.0 | © 2025\n\n")

root.mainloop()
