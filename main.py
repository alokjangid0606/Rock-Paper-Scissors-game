import tkinter as tk
import random
import os
def speak(text):
    os.system(f"powershell -Command \"Add-Type –AssemblyName System.Speech; " +
              f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}');\"")
    
speak("welcome to rock paperscissors game")
def play(user_choice):
    computer_choice = random.choice(["rock", "paper", "scissors"])
    result = ""
    
    
    if user_choice == computer_choice:
        speak("ooh no its draw")
        result = "It's a Draw!"
    elif win_condi[user_choice] == computer_choice:
        result = "You Win!"
        speak("ooh yes you win")
    else:
        result = "Computer Wins!"
        speak("better luck next time computer win")
    
    result_label.config(text=f"Computer chose {computer_choice}\nYou chose {user_choice}\nResult: {result}")
    engine.say(result)
    engine.runAndWait()


win_condi = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

# Create GUI window
root = tk.Tk()
root.title("rock paper scissor game devlop by alok")
root.geometry("400x300")

# Heading
tk.Label(root, text="Choose Rock, Paper or Scissors", font=("Arial", 14)).pack(pady=10)

# Buttons
tk.Button(root, text="Rock", width=15, command=lambda: play("rock")).pack(pady=5)
tk.Button(root, text="Paper", width=15, command=lambda: play("paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=15, command=lambda: play("scissors")).pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
result_label.pack(pady=20)

# Start the GUI loop
root.mainloop()
