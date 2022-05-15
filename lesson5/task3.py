def generator_tutors(tutors, groups):
    length1 = len(groups)
    for idx, man in enumerate(tutors):
        if idx < length1:
            yield man, groups[idx]
        else:
            yield man, None


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
groups = ['9А', '7В', '9Б', '9В']

# print(next(generator_tutors(tutors, groups)))
# print(next(generator_tutors(tutors, groups)))

gen_tutors = generator_tutors(tutors, groups)
print(f"Тип объекта: {type(gen_tutors)}")

for el in gen_tutors:
    print(el)
