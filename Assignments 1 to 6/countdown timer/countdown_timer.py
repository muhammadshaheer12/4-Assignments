import tkinter as tk
from tkinter import messagebox
import winsound  

# Global variables to manage countdown state
is_paused = False
remaining_time = 0
original_time = 0

# Function to start the countdown
def start_timer():
    global remaining_time, original_time, is_paused
    try:
        # Get the time entered by the user in seconds
        total_seconds = int(entry.get())
        # Ensure the entered time is a positive integer
        if total_seconds <= 0:
            raise ValueError("Please enter a positive number.")
        
        # Set the original time and remaining time
        original_time = total_seconds
        remaining_time = total_seconds
        is_paused = False
        
        # Start the countdown with the entered time
        countdown(remaining_time)
    except ValueError as e:
        # Show an error message if the input is invalid
        messagebox.showerror("❌ Invalid Input", str(e))

# Function to update the timer and show countdown
def countdown(seconds_left):
    if seconds_left > 0 and not is_paused:
        global remaining_time
        # Calculate minutes and seconds
        minutes = seconds_left // 60
        seconds = seconds_left % 60
        
        # Update the label to display the countdown
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        remaining_time = seconds_left
        
        # Call this function again after 1 second (1000 ms)
        root.after(1000, countdown, seconds_left - 1)
    elif seconds_left == 0:
        # Sound notification when the countdown reaches zero
        winsound.Beep(1000, 1000)  
        # Show a message box when the countdown reaches zero
        messagebox.showinfo("🎉 Time's Up ⏰", "The countdown has finished! 🎉🎉")

# Function to pause the countdown
def pause_timer():
    global is_paused
    is_paused = True
    pause_button.config(state="disabled")
    resume_button.config(state="normal")
    pause_button.config(text="⏸️ Paused 🛑")

# Function to resume the countdown
def resume_timer():
    global is_paused
    is_paused = False
    countdown(remaining_time)
    pause_button.config(state="normal")
    resume_button.config(state="disabled")
    pause_button.config(text="⏸️ Pause ⏩")

# Function to reset the countdown
def reset_timer():
    global remaining_time, original_time, is_paused
    is_paused = False
    remaining_time = 0
    timer_label.config(text="⏳ 00:00")
    entry.delete(0, tk.END)
    pause_button.config(state="normal")
    resume_button.config(state="disabled")
    pause_button.config(text="⏸️ Pause ⏩")
    reset_button.config(text="🔄 Reset 🔁")

# Set up the main window
root = tk.Tk()
root.title("⏳ Countdown Timer 🕒")
root.geometry("450x450")
root.config(bg="#f2f2f2")  

# Set up the input label with emoji and styling
label = tk.Label(root, text="⏰ Enter time in seconds:", font=("Arial", 14), bg="#f2f2f2")
label.pack(pady=15)

# Entry field to input the time in seconds with improved design
entry = tk.Entry(root, width=20, font=("Arial", 14), justify="center", bd=2)
entry.pack(pady=10)

# Set up the start button with emoji and styling
start_button = tk.Button(root, text="🚀 Start Countdown 🕰️", command=start_timer, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", bd=5)
start_button.pack(pady=10)

# Set up the pause and resume buttons
pause_button = tk.Button(root, text="⏸️ Pause ⏩", command=pause_timer, font=("Arial", 14), bg="#FF9800", fg="white", relief="raised", bd=5)
pause_button.pack(pady=5)

resume_button = tk.Button(root, text="▶️ Resume 🔄", command=resume_timer, font=("Arial", 14), bg="#4CAF50", fg="white", relief="raised", bd=5)
resume_button.pack(pady=5)
resume_button.config(state="disabled")  

# Set up the reset button with a refreshed emoji
reset_button = tk.Button(root, text="🔄 Reset 🔁", command=reset_timer, font=("Arial", 14), bg="#f44336", fg="white", relief="raised", bd=5)
reset_button.pack(pady=10)

# Set up the timer display label with emojis and a larger font
timer_label = tk.Label(root, text="⏳ 00:00", font=("Helvetica", 30, "bold"), bg="#f2f2f2", fg="#333")
timer_label.pack(pady=30)

# Run the main event loop of the application
root.mainloop()
