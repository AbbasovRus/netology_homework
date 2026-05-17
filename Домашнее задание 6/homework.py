import json

purchases = {}

with open('purchase_log.txt', 'r', encoding='utf-8') as f:
    next(f)  # Пропускаем первую строку (заголовок)
    for line in f:
        if line.strip():
            data = json.loads(line)
            purchases[data['user_id']] = data['category']

# Вывод
for user_id, category in list(purchases.items())[:20]:
    print(repr(user_id), repr(category))