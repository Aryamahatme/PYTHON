import random

COLORS =["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def gen_code():
    return random.sample(COLORS, CODE_LENGTH)

def guess_code():
     while True:
         guess = input("Guess: ").upper().split(" ")
    
         if len(guess) != CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors from {COLORS} (type with spaces between).")
            continue
        
         for color in guess:
             if color not in COLORS:
                 print(f"Invalid color: {color}. Try again. ")
                 break
         else:
            
            return guess       
   
def check_code(guess, real_code):
    color_counts ={}
    correct_pos = 0
    incorrect_pos = 0
    
    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
            
    for guess_color, real_color in zip(guess, real_code):
        if guess_color== real_color:
            correct_pos+= 1
            color_counts[guess_color] -= 1
            
    for guess_color, real_color in zip(guess,real_code):              
        if guess_color in color_counts and color_counts[guess_color]> 0 and guess_color != real_color: 
            incorrect_pos += 1
            color_counts[guess_color] -= 1
            
    return correct_pos, incorrect_pos            

def game():
    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the code.... ")
    print(f"The valid colors are: {','.join(COLORS)} (type with spaces between) ")
    code = gen_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos ,incorrect_pos = check_code(guess, code)
        
        if correct_pos== CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries!")
            break
        
        print(f"Correct Position : {correct_pos} | Incorrect Position : {incorrect_pos}")
        
    else:
        print(f"You ran out of tries, the code was:{' '.join(code)}" )
if __name__ == "__main__" :        
   game()
