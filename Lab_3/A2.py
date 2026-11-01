import string

password = input("Введите пароль: ")

if len(password) != 8:
    print("Длина пароля не равна 8")

if password == password.lower():
    print("В пароле отсутствуют заглавные буквы")

if password == password.upper():
    print("В пароле отсутствуют строчные буквы")

if not any(symbol.isdigit() for symbol in password):
    print("В пароле отсутствуют цифры")

if not any(symbol in "*-#" for symbol in password):
    print("В пароле отсутствуют специальные символы")

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + "*-#"

if not all(symbol in allowed for symbol in password):
    print("В пароле используются непредусмотренные символы")

if (len(password) == 8
    and password != password.lower()
    and password != password.upper()
    and any(symbol.isdigit() for symbol in password)
    and any(symbol in "*-#" for symbol in password)
    and all(symbol in allowed for symbol in password)):
    print("Надежный пароль")
