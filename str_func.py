def capital_letters(s):

    """
    Функция, которая принимает на вход строку и возвращает ее со всеми заглавными буквами
    """

    # Разбиваем строку на список слов.
    words = s.split()

    # Обрабатываем первое слово.
    if words:
        words[0] = words[0].capitalize()

    # Обрабатываем остальные слова.
    for i in range(1, len(words)):
        # Если перед словом есть точка, восклицательный или вопросительный знак,
        # то делаем заглавной первую букву слова, не считая пробелы.
        if words[i - 1][-1] in '.!?':
            words[i] = words[i].capitalize()

    # Соединяем слова обратно в строку.
    return ' '.join(words)


s = 'привет, мир! как дела? что нового?'
print(capital_letters(s))
