# source_code/main.py

import tkinter as tk
from tkinter import scrolledtext
import openai

# ⛳ API Key - Yahan apni OpenAI API key lagao
openai.api_key = "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"

def get_combined_response(user_input):
    try:
        system_prompt = (
            "You are HackerMindAI, a collective AI composed of:\n"
            "1. ChatGPT (general friendly assistant)\n"
            "2. KaliGPT (ethical hacker mindset)\n"
            "3. PenetrationGPT (cybersecurity/penetration tester)\n"
            "4. White Rabbit GPT (deep critical thinker with unorthodox logic)\n\n"
            "Each agent analyzes the user's input and collectively forms a single, unified, highly intelligent response "
            "that is helpful, creative, and secure."
        )

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        return completion.choices[0].message.content.strip()

    except Exception as e:
        return f"[Error] {str(e)}"

# 🔷 GUI Setup
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return
    chat_log.insert(tk.END, f"\n🧑 You: {user_input}\n")
    entry.delete(0, tk.END)
    chat_log.insert(tk.END, "🤖 HackerMindAI is thinking...\n")
    app.update()

    response = get_combined_response(user_input)
    chat_log.insert(tk.END, f"\n{response}\n")
    chat_log.see(tk.END)

app = tk.Tk()
app.title("HackerMindAI v1.0.0 – Multi-GPT Intelligence")
app.geometry("600x500")
app.configure(bg="#1e1e1e")

chat_log = scrolledtext.ScrolledText(app, wrap=tk.WORD, font=("Consolas", 10), bg="#252526", fg="#d4d4d4")
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(app, font=("Arial", 12), bg="#333333", fg="#ffffff")
entry.pack(padx=10, pady=(0, 10), fill=tk.X)

send_button = tk.Button(app, text="Send", command=send_message, bg="#007ACC", fg="white", font=("Arial", 10, "bold"))
send_button.pack(pady=(0, 10))

chat_log.insert(tk.END, "🚀 Welcome to HackerMindAI v1.0.0\nType your query below...\n")
app.mainloop() 
