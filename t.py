
import random
lines = [
    "If you can keep your head when all about you\n Are losing theirs and blaming it on you",
    "If you can trust yourself when all men doubt you,\n But make allowance for their doubting too",
    "If you can wait and not be tired by waiting,\n Or being lied about, don’t deal in lies",
    "Or being hated, don’t give way to hating,\n And yet don’t look too good, nor talk too wise",
    "If you can dream—and not make dreams your master;\n If you can think—and not make thoughts your aim",
    "If you can meet with Triumph and Disaster\n And treat those two impostors just the same",
    "If you can bear to hear the truth you’ve spoken\n Twisted by knaves to make a trap for fools",
    "Or watch the things you gave your life to, broken,\n And stoop and build them up with worn-out tools",
    "If you can make one heap of all your winnings\n And risk it on one turn of pitch-and-toss",
    "And lose, and start again at your beginnings\n And never breathe a word about your loss",
    "If you can force your heart and nerve and sinew\n To serve your turn long after they are gone",
    "And so hold on when there is nothing in you\n Except the Will which says to them Hold on",
    "If you can talk with crowds and keep your virtue,\n Or walk with Kings—nor lose the common touch",
    "If neither foes nor loving friends can hurt you,\n If all men count with you but none too much",
    "If you can fill the unforgiving minute\n With sixty seconds’ worth of distance run",
    "Yours is the Earth and everything that’s in it,\n And which is more you will be a Man my son"
]


print("Welcome to the Verse Master!\nTest your memory with lines from the classic poem 'If—' by Rudyard Kipling. Can you fill in the missing words?\n")

input("Press any key to continue >> ")
print()

score = 0
total_questions = len(lines)

for line in lines:
    n = random.randint(1, 5)
    noofspace = line.count(" ")

    linelist = line.split(" ")
    nomwords = len(linelist)
    output = ""
    check = ""        
    for i, word in enumerate(linelist):
        if i >= nomwords-n:
            wordlen = len(word)
            output = output + "-"*wordlen + " "
            check = check + word + " "
        else:
            output = output + word + " "

    print(output)
    ans = input(">>>") + " "
    if ans.lower() == check.lower():
        print("Correct Phrase!!!")
    else:
        print("Wrong!!")
        print(f"Correct Phrase is '{check.strip()}'")

    print()

    
    
print("\n*********************************************************")
print(f"Quiz Complete! You scored {score} out of {total_questions}.")
print("*********************************************************\n")

input("Press Enter to cloae application")
