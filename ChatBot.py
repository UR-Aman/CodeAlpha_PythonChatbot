import tkinter as tk
from tkinter import scrolledtext

# 💬 Predefined responses dictionary
responses = {
    "hello": "Hi there! 👋",
    "hi": "Hello! How can I assist you today?",
    "how are you": "I'm doing great, thank you! 😊",
    "what is your name": "I am CodeAlphaBot — your Python assistant 🤖",
    "who created you": "I was created by Aman as part of a Python internship project 💻",
    "what can you do": "I can answer simple questions. Try asking: 'hello', 'bye', 'help', etc.",
    "help": "Sure! You can try saying 'hello', 'how are you', 'what is your name', or 'bye'.",
    "bye": "Goodbye! Have a great day ahead! 👋"
}

# 🧠 Chatbot reply logic
def get_response(user_input):
    user_input = user_input.lower().strip()
    return responses.get(user_input, "Sorry, I didn't understand that. 🤖")

# 🪟 GUI setup
def send_message():
    user_message = entry.get()
    if user_message == "":
        return

    chat_window.config(state="normal")
    chat_window.insert(tk.END, f"You: {user_message}\n")

    bot_response = get_response(user_message)
    chat_window.insert(tk.END, f"CodeAlphaBot: {bot_response}\n\n")
    chat_window.config(state="disabled")
    entry.delete(0, tk.END)
    chat_window.yview(tk.END)

# 🪟 Main window
app = tk.Tk()
app.title("Chatbot 🤖")
app.geometry("500x600")
app.resizable(False, False)
app.configure(bg="#1e1e2f")

# 💬 Chat display
chat_window = scrolledtext.ScrolledText(app, state="disabled", wrap=tk.WORD, bg="#282c34", fg="white", font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# 🔤 Entry field
entry = tk.Entry(app, font=("Arial", 12), width=40)
entry.pack(padx=10, pady=10, side=tk.LEFT, expand=True, fill=tk.X)

# 📨 Send button
send_button = tk.Button(app, text="Send", command=send_message, bg="#61afef", fg="black", font=("Arial", 12))
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Run the app
chat_window.config(state="normal")
chat_window.insert(tk.END, "🤖 Bot: Hello! Type a message below to start chatting.\n\n")
chat_window.config(state="disabled")
app.mainloop()
