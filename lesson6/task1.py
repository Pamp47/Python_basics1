list_string = []
with open('nginx_logs.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        line1, line2, *_ = line.split('"')
        line1, line2 = line1.split(), line2.split()
        list_string.append((line1[0], line2[0], line2[1]))

for el in list_string:
    print(el)
