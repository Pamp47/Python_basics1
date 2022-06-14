activity = {}
with open("nginx_logs.txt", mode='r', encoding='utf-8') as f:
    for line in f:
        line1, *_ = line.split('"')
        address = line1.split()[0]
        if address not in activity.keys():
            activity[address] = 1
        else:
            activity[address] += 1

spam_quantity = max(activity.values())
for key, val in activity.items():
    if val == spam_quantity:
        print(f'Спамер: Адрес: {key}, количество отправленных запросов: {val}')
