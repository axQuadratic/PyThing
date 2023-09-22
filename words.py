import os
import platform as pf
import random as r

words = {}
word_num = 0
tries = 0

def main():
    while True:
        cont = add_to_list()
        clear_console()
        if (not cont):
            break
    
    while True:
        cont = ask_from_list()
        clear_console()
        if (not cont):
            break

def clear_console():
    if (pf.system() == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def add_to_list():
    global word_num

    word1 = input("Input a word of your choice:\n")
    word2 = input("Now input that word in another language of your choice:\n")
    words[word1.lower()] = word2.lower()
    word_num += 1
    print("Add another word?\n[1 - yes; 2 - no]")
    if cnotine():
        return True
    else:
        return False
        
def ask_from_list():
    global word_num
    global tries

    if (len(words) <= 0):
        print(f"Congratulations, you appear to have cleared {word_num} word{'' if word_num == 1 else 's'} (which is all of them)" +
              f", and it only took you {tries} tr{'y' if tries == 1 else 'ies'}!")
        print("Here's your reward:")
        print(
            "░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░\n" +
            "░░░░░░░███████░░░░░░░██░░░░░░░░░░░░░░░░░░░███████░░░░░░░██░░░░░░░░░░░░\n" +
            "░░░░█████░░░░░░░░░░░░░░███░██░░░░░░░░░░█████░░░░░░░░░░░░░░███░██░░░░░░\n" +
            "░░░██░░░░░████░░░░░░░░░░██████░░░░░░░░██░░░░░████░░░░░░░░░░██████░░░░░\n" +
            "░░░██░░████░░███░░░░░░░░░░░░░██░░░░░░░██░░████░░███░░░░░░░░░░░░░██░░░░\n" +
            "░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░\n" +
            "░░░░██████████░███░░░░░░░░░░░██░░░░░░░░██████████░███░░░░░░░░░░░██░░░░\n" +
            "░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░\n" +
            "░░░░███████████░░██░░░░░░░░░░██░░░░░░░░███████████░░██░░░░░░░░░░██░░░░\n" +
            "░░░░░░██░░░░░░░████░░░░░██████░░░░░░░░░░░██░░░░░░░████░░░░░██████░░░░░\n" +
            "░░░░░░██████████░██░░░░███░██░░░░░░░░░░░░██████████░██░░░░███░██░░░░░░\n" +
            "░░░░░░░░░██░░░░░████░███░░░░░░░░░░░░░░░░░░░░██░░░░░████░███░░░░░░░░░░░\n" +
            "░░░░░░░░░█████████████░░░░░░░░░░░░░░░░░░░░░░█████████████░░░░░░░░░░░░░\n"
        )
        input()

    root, trans = r.choice(list(words.items()))
    res = input(f"Translate the word '{root}':\n").lower()
    tries += 1
    if res == trans:
        print(
            "░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░\n" +
            "░░░░░░░███████░░░░░░░██░░░░░░░░░░░░\n" +
            "░░░░█████░░░░░░░░░░░░░░███░██░░░░░░\n" +
            "░░░██░░░░░████░░░░░░░░░░██████░░░░░\n" +
            "░░░██░░████░░███░░░░░░░░░░░░░██░░░░\n" +
            "░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░\n" +
            "░░░░██████████░███░░░░░░░░░░░██░░░░\n" +
            "░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░\n" +
            "░░░░███████████░░██░░░░░░░░░░██░░░░\n" +
            "░░░░░░██░░░░░░░████░░░░░██████░░░░░\n" +
            "░░░░░░██████████░██░░░░███░██░░░░░░\n" +
            "░░░░░░░░░██░░░░░████░███░░░░░░░░░░░\n" +
            "░░░░░░░░░█████████████░░░░░░░░░░░░░\n" +
            "*lip smack*"
            )
        words.pop(root)
    else:
        print(
            "░░░░░░░░░█████████████░░░░░░░░░░░░░\n" +
            "░░░░░░░░░██░░░░░████░███░░░░░░░░░░░\n" +
            "░░░░░░██████████░██░░░░███░██░░░░░░\n" +
            "░░░░░░██░░░░░░░████░░░░░██████░░░░░\n" +
            "░░░░███████████░░██░░░░░░░░░░██░░░░\n" +
            "░░░░██░░░░░░░░████░░░░░░░░░░░██░░░░\n" +
            "░░░░██████████░███░░░░░░░░░░░██░░░░\n" +
            "░░░██░░░░░░░░███░░░░░░░░░░░░░██░░░░\n" +
            "░░░██░░████░░███░░░░░░░░░░░░░██░░░░\n" +
            "░░░██░░░░░████░░░░░░░░░░██████░░░░░\n" +
            "░░░░█████░░░░░░░░░░░░░░███░██░░░░░░\n" +
            "░░░░░░░███████░░░░░░░██░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░░██░░░░░░██░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░██░░░░░███░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░██░░░░██░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░██░░░███░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░██░░░██░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░██░░░█░░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░███░██░░░░░░░░░░░░░░░░░░░░\n" +
            "░░░░░░░░░░░████░░░░░░░░░░░░░░░░░░░░\n" +
            "*displeased lip smack*"
            )
        
    print("Would you like to continue?\n[1 - yes; 2 - no]")
    if cnotine():
        return True
    else:
        return False

def cnotine():
    while True:
        cont = input().strip()
        if (cont == "1"):
            return True
        elif (cont == "2"):
            return False

main()