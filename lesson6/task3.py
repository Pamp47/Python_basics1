def initials(fio):
    fio = fio.strip().split(",")
    return " ".join([fio[0][:len(fio[0])], fio[1][:len(fio[1])], fio[2][:len(fio[2])]])


with open("users.csv", mode="rt", encoding="UTF-8") as file_fio:
    fio_data = file_fio.readlines()
with open("hobby.csv", mode="rt", encoding="UTF-8") as file_hobby:
    hobby_data = file_hobby.readlines()

fio_data_len = len(fio_data)
hobby_data_len = len(hobby_data)
dict_man3 = {}

for idx in range(min(fio_data_len, hobby_data_len)):
    fio = fio_data[idx]
    dict_man3[initials(fio)] = hobby_data[idx].strip()
if hobby_data_len > fio_data_len:
    exit(1)
else:
    for idx in range(hobby_data_len, fio_data_len):
        fio = fio_data[idx]
        dict_man3[initials(fio)] = None
print(dict_man3)

with open('FIO_hobby.txt', mode='wt', encoding='UTF-8') as FIO_hobby:
    FIO_hobby.write(str(dict_man3))
    