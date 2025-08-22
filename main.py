import random
import tkinter as tk
root=tk.Tk()
root.geometry("600x400")
root.title("Number Guessing Game")
secret_num= random.randint(1,50)
atempts=5
label=tk.Label(root,text=("Welcome! Guess a number between 1 and 50."),wraplength=280,font=("Arial",18))
label.pack()
entry =tk.Entry(root,font=("Arial",14))
entry.pack()
resultL=tk.Label(root,text=(""),font=("Arial",14))
resultL.pack()
submitB= tk.Button(root,text=("Submit"),font=("Arial",14))
submitB.pack()
attemptLft=tk.Label(root,text=(f"Attempts Left: {atempts}."),font=("Arial",14))
attemptLft.pack()
def check_guess():
    global atempts,secret_num
    guess = entry.get()
    if guess.isdigit():   
        guess = int(guess)
        atempts -= 1
    
        if guess<secret_num:
            resultL.config(text=("Too Low Bro"),fg="blue")
        elif guess>secret_num:
            resultL.config(text=("Too High Bro"),fg="red")
        if guess==secret_num:
            resultL.config(text=("You Won Bro"),fg="green")
            submitB.config(state='disabled')
        attemptLft.config(text=f"Attempts Left: {atempts}")
        if atempts==0:
            resultL.config(text=f"Game Over! You Lose. Number was {secret_num}", fg="purple")
            submitB.config(state="disabled")
    else:
        resultL.config(text="Please enter a valid number!", fg="orange")

submitB.config(command=check_guess)
root.mainloop()
