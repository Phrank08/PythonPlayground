import random
#import os

words = [
    {"french": "le", "english": "the"},
    {"french": "de", "english": "of/from"},
    {"french": "un", "english": "a/an"},
    {"french": "à", "english": "to/at"},
    {"french": "être", "english": "to be"},
    {"french": "et", "english": "and"},
    {"french": "en", "english": "in"},
    {"french": "avoir", "english": "to have"},
    {"french": "que", "english": "that"},
    {"french": "pour", "english": "for"},
    {"french": "dans", "english": "in"},
    {"french": "ce", "english": "this/that"},
    {"french": "il", "english": "he/it"},
    {"french": "qui", "english": "who"},
    {"french": "ne", "english": "not"},
    {"french": "sur", "english": "on"},
    {"french": "se", "english": "oneself"},
    {"french": "pas", "english": "not"},
    {"french": "plus", "english": "more"},
    {"french": "pouvoir", "english": "to be able to"},
    {"french": "par", "english": "by"},
    {"french": "je", "english": "I"},
    {"french": "avec", "english": "with"},
    {"french": "tout", "english": "all/everything"},
    {"french": "faire", "english": "to do/make"},
    {"french": "son", "english": "his/her/its"},
    {"french": "mettre", "english": "to put"},
    {"french": "autre", "english": "other"},
    {"french": "mais", "english": "but"},
    {"french": "nous", "english": "we"},
    {"french": "comme", "english": "like/as"},
    {"french": "ou", "english": "or"},
    {"french": "si", "english": "if/yes"},
    {"french": "leur", "english": "their"},
    {"french": "y", "english": "there"},
    {"french": "dire", "english": "to say"},
    {"french": "elle", "english": "she/it"},
    {"french": "avant", "english": "before"},
    {"french": "deux", "english": "two"},
    {"french": "même", "english": "same"},
    {"french": "prendre", "english": "to take"},
    {"french": "aussi", "english": "also"},
    {"french": "celui", "english": "the one"},
    {"french": "donner", "english": "to give"},
    {"french": "bien", "english": "well/good"},
    {"french": "où", "english": "where"},
    {"french": "fois", "english": "time"},
    {"french": "vous", "english": "you"},
    {"french": "encore", "english": "again/still"},
    {"french": "nouveau", "english": "new"}
]


def quiz_user(words):
    #os.system('cls' if os.name == 'nt' else 'clear')
    score = 0
    random.shuffle(words)
    for word in words:
        #os.system('cls' if os.name == 'nt' else 'clear')
        user_data = input(f'What is the English word for {word['french']}? ').strip().lower()
        english_word = word['english'].lower()
        correct_answer = english_word.split('/')

        if user_data in correct_answer:
            print('Correct!')
            score +=1
        elif user_data == 'q':
            #print(f'You scored {score} out of {len(words)} questions')
            quit()
        else:
            print('Incorrect!')
            score = 0
    
    print(f'You scored {score} out of {len(words)} questions')


def main():
    print("WELCOME TO THE LANGUAGE TRANSLATION APP")
    user_input = input("Press Enter to continue / q to quit: ").lower()
    if user_input == 'q':
        quit()
    quiz_user(words)

if __name__ == '__main__':
    main()
