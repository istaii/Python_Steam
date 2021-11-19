import random

# enter your pair {'theme': 'word'}
theme_word_dict = {'Животное': 'тюлень', 'млекопитающее': 'дельфин', 'жалеет зерно': 'крот', 'жжется': 'крапива'}
words = []
themes = []
for k, n in theme_word_dict.items():
    themes.append(k)
    words.append(n)
n = random.randrange(len(words))


def get_word():
    word = ''
    word = words[n].upper()
    return word


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    print('Давайте играть в угадайку слов!')
    tries = 6
    theme = themes[n]
    word_completion = '.' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    count = 0
    while True:
        print('ТЕМА', theme)
        print(display_hangman(tries))
        print(word_completion)
        letter = input('Попробуйте угадать букву или слово целиком>>>').upper()
        if letter.isalpha() and len(letter) == 1:
            True
        elif letter.isalpha() and len(letter) == len(word):
            if letter == word:
                print('Вы угадали слово!')
                break
            else:
                print('У вас не получилось угадать слово сразу(')
        elif letter.isalpha() and len(letter) > 1:
            print('В слове', len(word), 'букв(ы)! А вы написали слово из', len(letter), 'букв!')
        else:
            tries += 1
            print('Введите букву! А не другой знак!')
        if letter in guessed_letters and len(letter) == 1:
            print('Эта буква уже была. Введите еще раз')
            tries += 1
        elif letter in guessed_words and len(letter) > 1:
            print('Это слово уже было, попробуйте еще раз')
            tries += 1
        elif letter in word and letter not in guessed_letters:
            for i in range(len(word)):
                if word[i] == letter:
                    word_completion = word_completion[:i] + word[i] + word_completion[i + 1:]
                    if letter not in word[i + 1:]:
                        tries += 1
                        guessed_letters.append(letter)
                        print('Вы угадали букву!')
        else:
            if len(letter) == 1:
                print('Вы не угадали букву!')
                guessed_letters.append(letter)
            else:
                guessed_words.append(letter)
        if word_completion == word:
            print('Поздравляем! Вы угадали слово!')
            break
        tries -= 1
        if tries == 0:
            display_hangman(tries)
            print('Ваши попытки исчерпаны. Слово:', word)
            break


def start_game():
    while True:
        word = get_word()
        play(word)
        while True:
            q = input('Хотите еще сыграть, д/н?')
            if q == 'н':
                return 'Спасибо за игру!'
                False
            elif q == 'д':
                break
            else:
                print('Введите д(да) или н(нет)')


print(start_game())
