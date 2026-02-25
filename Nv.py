import tkinter as tk
from tkinter import messagebox

def create_plan():
    name = entry_name.get()
    subject = entry_subject.get()
    time_text = entry_time.get()

    if not name or not subject or not time_text:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        time = int(time_text)
    except ValueError:
        messagebox.showerror("Error", "Time must be a number.")
        return

    plan = f"Hello {name}\n\nSTUDY PLAN\n\n"

    if time < 30:
        plan += (
            "Short study session:\n"
            f"- 20 minutes: revise {subject}\n"
            "- 10 minutes: summary and rest\n"
        )
    elif time <= 60:
        plan += (
            "Medium study session:\n"
            f"- 30 minutes: study {subject}\n"
            "- 10 minutes: break\n"
            "- 20 minutes: exercises\n"
        )
    else:
        plan += (
            "Long study session:\n"
            f"- 40 minutes: study {subject}\n"
            "- 10 minutes: break\n"
            "- 30 minutes: practice\n"
            "- 10 minutes: review mistakes\n"
        )

    plan += (
        "\nMotivation:\n"
        "- Stay focused.\n"
        "- Every minute matters.\n"
        "- Progress is better than perfection.\n"
        "- You are capable of success.\n"
    )

    result_label.config(text=plan)


# Window setup
window = tk.Tk()
window.title("Study Buddy")
window.geometry("400x500")

# Title
title = tk.Label(window, text="STUDY BUDDY", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Name
tk.Label(window, text="Your name:").pack()
entry_name = tk.Entry(window)
entry_name.pack()

# Subject
tk.Label(window, text="Subject to study:").pack()
entry_subject = tk.Entry(window)
entry_subject.pack()

# Time
tk.Label(window, text="Time available (minutes):").pack()
entry_time = tk.Entry(window)
entry_time.pack()

# Button
tk.Button(window, text="Create study plan", command=create_plan).pack(pady=10)

# Result
result_label = tk.Label(window, text="", justify="left", wraplength=350)
result_label.pack(pady=10)

# Run window
window.mainloop()