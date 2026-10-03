import tkinter as tk
from google import genai

API_KEY = "AQ.Ab8RN6JNkEZdydqvRQsptiEgog0k3GhHNk-zs4B1RM2NioHgPg"


client = genai.Client(api_key=API_KEY)

def aks_ai():
    que = input_field.get()
    response = client.models.generate_content(model="gemini-3.6-flash", contents=que)
    print(response.text)
    output_field.config(text=response.text)


window = tk.Tk()
window.geometry(f"{window.winfo_screenwidth()}x{window.winfo_screenheight()}")
window.title("AI Assistant")

output_field = tk.Label(
    window,
    text="",
    font=("Arial", 16),
    wraplength=700
)
output_field.place(relx=0.5, rely=0.5, anchor="center")


bottom_frame = tk.Frame(window)
bottom_frame.pack(side="bottom", fill="x", padx=20, pady=20)

input_field = tk.Entry(
    bottom_frame,
    font=("Arial", 14)
)
input_field.pack(side="left", fill="x", expand=True, ipady=10)

button = tk.Button(
    bottom_frame,
    text="Submit",
    font=("Arial", 12),
    width=10,
    command=aks_ai
)
button.pack(side="right", padx=(10, 0), ipady=5)


window.mainloop()
