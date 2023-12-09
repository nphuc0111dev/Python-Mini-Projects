from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
CHECK = "✓"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    # Set 00:00 after reset
    canvas.itemconfig(timer_text, text="00:00")
    # Title is "Timer"
    timer_label.config(text="Timer")
    # Reset check mark
    check_label.config(text="")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:
        count_down(work_sec)
        timer_label.config(text="Work", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
    elif reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", bg=YELLOW, fg=RED, font=(FONT_NAME, 40, "bold"))
    else:
        count_down(short_break_sec)
        timer_label.config(text="Short Break", bg=YELLOW, fg=PINK, font=(FONT_NAME, 40, "bold"))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += CHECK
        check_label.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_photo = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_photo)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(row=0, column=1)
check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "bold"))
check_label.grid(row=3, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
