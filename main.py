# Задача №3
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]
freqs = {}  # словарь где ключом будет количество слов в запросе, значением - количество таких запросов
for query in queries:
    word_count = len(query.split())
    freqs[word_count] = freqs.get(word_count, 0) + 1
for key, value in sorted(freqs.items()):
    print(f'Поисковых запросов из {key} слов - {int(value / sum(freqs.values()) * 100)}%')