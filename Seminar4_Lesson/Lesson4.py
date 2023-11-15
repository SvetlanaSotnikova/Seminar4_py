# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

user_str = input("Input symbols: ")

symbols = user_str.split()

count_dict = {}

result = []

for symbol in symbols:
    if symbol in count_dict:
        count_dict[symbol] += 1
        result.append(f'{symbol}_{count_dict[symbol]}')
    else:
        count_dict[symbol] = 0
        result.append(symbol)

result_str = " ".join(result)

print(f'result: {result_str}')
    
# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

user_text = input("Input str: ")

user_text = user_text.upper()

words = user_text.replace(".", " ").split()

unique_word = set(words)

count_unique_word = len(unique_word)

print(f'unique words: {count_unique_word}')
