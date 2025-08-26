""" 
##########################
## Sam, Joenniel lll L. ##
########################## 
"""

import sys

print("\nSam's Magic Words")

while True:
    while True:
        # USER WORD INPUT
        word = input("\nEnter your word: ").strip()
        if word:
            break

        # USER INPUT BLANK
        print("Please enter a word :)")

    # MENU LOOP
    while True:
        operation = input(
            "\n1. Reverse "
            "\n2. Count vowels"
            "\n3. Check if palindrome"
            "\n4. Find and replace a word"
            "\n5. Format (title case)"
            "\n6. Split into words"
            "\n7. Word frequency counter"
            "\n8. Swap case"
            "\n9. New sentence"
            "\n0. Exit"
            "\nChoose operation: ".strip())

        # CONDITIONS
        if operation == "1":
            print(f"\nResult: {word[::-1]}")

        elif operation == "2":
            VOWELS = "aeiouAEIOU"
            COUNT = 0
            for x in word:
                if x in VOWELS:
                    COUNT += 1
            print(f"\nVowel COUNT: {COUNT}")

        elif operation == "3":
            if word.lower() == word[::-1].lower():
                print("\nIt's a palindrome!")
            else:
                print("\nNot a palindrome.")

        elif operation == "4":
            old = input("\nWord to replace: ").strip()
            new = input("New word: ").strip()
            if old in word:
                print(f"\nResult: {word.replace(old, new)}")
            else:
                print(f"\n'{old}' not found in the sentence.")

        elif operation == "5":
            print(f"\nResult: {word.title()}")

        elif operation == "6":
            print(f"\nSplit into words: {word.split()}")

        elif operation == "7":
            frequency = {}
            words = word.split()

            for w in words:
                frequency[w] = frequency.get(w, 0) + 1

            print("\nWord Frequency:")
            for k, v in frequency.items():
                print(f"{k}: {v}")

            total_words = len(words)
            print(f"Total words: {total_words}")

        elif operation == "8":
            print(f"\nResult: {word.swapcase()}")

        # LOOP BACK TO "ENTER NEW WORD"
        elif operation == "9":
            break

        elif operation == "0":
            print("\nGoodbye! Thank you :)")
            sys.exit()

        else:
            print("\nInvalid choice. Please try again :)")
