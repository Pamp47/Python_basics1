import re

mail_template = "([\w\.'+-]+)@([\w\.-]+\.{1}[\w\.-]+)"


def email_parse(email, regex_template=mail_template):
    rez = re.fullmatch(regex_template, email)
    if rez is None:
        raise ValueError
    rez = rez.groups()
    return {'username': rez[0], 'domain': rez[1]}


lst_data = [
    "someo_ne1@geekbrains1.ru",
    "some+one@geekbrains2.ru",
    "some&one@geek-brains.ru",
    "some'one@geekbrains.ru",
    "some'one@geekbrainsru",
]

for email in lst_data:
    try:
        print(f"for email: {email} result is {email_parse(email)}")
    except ValueError:
        print(f"Error {email}")
