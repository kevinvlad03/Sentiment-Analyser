from textblob import TextBlob
import tkinter as tk
from tkinter import ttk
import psutil
import time

def analyze_sentiment():
    text = text_input.get("1.0", tk.END)
    blob = TextBlob(text)
    results = f"Polarity: {blob.sentiment.polarity:.3f}\n"
    results += f"Subjectivity: {blob.sentiment.subjectivity:.3f}\n"
    if blob.sentiment.polarity > 0:
        results += "Positive"
    elif blob.sentiment.polarity < 0:
        results += "Negative"
    else:
        results += "Neutral"
    sentiment_result.set(results)

def print_system_res():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")

def analyze_thread():
    while True:
        analyze_sentiment()
        time.sleep(1)

def close_window():
    window.destroy()

# Create main window
window = tk.Tk()
window.title("Sentiment Analysis")
window.configure(bg="lightgray")
window.geometry("600x400")

# Set a custom window icon
# window.iconbitmap('path_to_icon.ico') # Uncomment and set path to your icon file

# Frame for text input
input_frame = tk.Frame(window, bg="lightgray")
input_frame.pack(padx=10, pady=10, fill="x")

text_input_label = tk.Label(input_frame, text="Enter text to analyze:", font=("Arial", 12), bg="lightgray", fg="black")
text_input_label.pack(anchor="w")

text_input = tk.Text(input_frame, height=10, width=50, font=("Arial", 12), bg="white", fg="black")
text_input.pack(pady=10, fill="x")

scrollbar = tk.Scrollbar(input_frame, command=text_input.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_input.config(yscrollcommand=scrollbar.set)

# Frame for sentiment analysis result
result_frame = tk.Frame(window, bg="lightgray")
result_frame.pack(padx=10, pady=10, fill="x")

sentiment_label = tk.Label(result_frame, text="Sentiment", font=("Arial", 12), bg="lightgray", fg="black")
sentiment_label.pack(anchor="w")

sentiment_result = tk.StringVar()
result_label = tk.Label(result_frame, textvariable=sentiment_result, font=("Arial", 12), bg="lightgray", fg="black", justify="left")
result_label.pack(pady=10, fill="x")

# Frame for buttons
button_frame = tk.Frame(window, bg="lightgray")
button_frame.pack(padx=10, pady=10, fill="x")

analyze_button = ttk.Button(button_frame, text="Analyze text", command=analyze_sentiment)
analyze_button.pack(side=tk.LEFT, padx=5)

close_button = ttk.Button(button_frame, text="Close", command=close_window)
close_button.pack(side=tk.LEFT, padx=5)

# Start the GUI event loop
window.mainloop()
