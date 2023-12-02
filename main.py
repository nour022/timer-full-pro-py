from tkinter import *
import winsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rops = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
	global rops
	rops = 0
	window.after_cancel(timer)
	label.config(text="Timer", fg=GREEN)
	canvas.itemconfig(tiemer_text, text=f"00:00")
	checkMark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
	global rops
	rops += 1
	if rops % 8 == 0:
		winsound.PlaySound("C:/Users/mnour/Desktop/Daten/message.wav", winsound.SND_FILENAME)
		label.config(fg=RED, text="Long Break")

		count_down(LONG_BREAK_MIN * 60)
	elif rops % 2 == 0:
		winsound.PlaySound("C:/Users/mnour/Desktop/Daten/message.wav", winsound.SND_FILENAME)
		label.config(fg=PINK, text="Short Break")
		count_down(SHORT_BREAK_MIN * 60)
	else:
		winsound.PlaySound("C:/Users/mnour/Desktop/Daten/message.wav", winsound.SND_FILENAME)
		label.config(fg=GREEN, text="Work")
		count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
import time
import math


def count_down(count):
	min = math.floor(count / 60)
	secand = count % 60
	if secand < 10:
		secand = f"0{secand}"
	elif min < 10:
		min = f"0{min}"
	canvas.itemconfig(tiemer_text, text=f"{min}:{secand}")
	if count > 0:
		global timer
		timer = window.after(1000, count_down, count - 1)
	else:
		start_timer()
		mark = ""
		work_sessions = math.floor(rops / 2)
		for _ in range(work_sessions):
			mark = "✔"
		checkMark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)

# Label with Text Timer
label = Label(text="Timer")
label.config(fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
label.grid(row=1, column=2)
# Canvas a Image
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
tiemer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=2, column=2)
# Start Button
start_btn = Button(text="Start", command=start_timer)
start_btn.grid(row=3, column=1)
# Restert Button
reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(row=3, column=3)

# check Mark
checkMark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
checkMark.grid(row=4, column=2)

window.mainloop()
