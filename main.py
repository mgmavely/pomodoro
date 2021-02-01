from tkinter import *
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

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer", fg=GREEN)
    canvas.itemconfig(time_text, text="00:00")
    rounds.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    window.lift()
    window.attributes('-topmost', True)
    window.attributes('-topmost', False)

    global reps
    reps += 1
    work = WORK_MIN * 60
    short = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short)
        title.config(text="Break", fg=PINK)
    else:
        count_down(work)
        title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global reps
    minutes = int(count / 60)
    seconds = count % 60
    new_text = f"{minutes:02d}:{seconds:02d}"
    canvas.itemconfig(time_text, text=new_text)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = ""
        for i in range(int(reps/2)):
            checks += "✓"
        rounds.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title = Label(text="Timer", font=(FONT_NAME, 38))
title.grid(column=1, row=0)
title.config(padx=20, bg=YELLOW, fg=GREEN)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", command=start_timer)
start.grid(column=0, row=2)

reset = Button(text="Reset", command=reset_timer)
reset.grid(column=2, row=2)

rounds = Label(font=("Arial", 14))
rounds.grid(column=1, row=3)
rounds.config(padx=20, bg=YELLOW, fg=GREEN)

window.mainloop()
