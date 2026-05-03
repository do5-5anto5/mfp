from words import words
import random

number = random.randrange(len(words))

secret_word = words[number]

print(f"words size: {len(words)}\nrandom number {number}\n{secret_word}")

mask_list = ["-" for c in secret_word]
mask = "".join(mask_list)
print(mask)
placeholder_list = []


while True:
    answer = input("What is the word? ")

    for index, char in enumerate(secret_word):
        if answer[index] == char:
            print(f'char {char} answer {answer[index]}')
            print(answer[index] == char)
            mask_list[index] = char
        
    mask = "".join(mask_list)

    print(f'reposta: {mask}')

    if answer == "0":
        break
