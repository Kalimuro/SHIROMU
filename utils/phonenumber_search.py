from utils.imports import *


def get_phone_number_info(phone_number):
    if not phone_number:
        print("Неверно введен номер")
        return

    x = phonenumbers.parse(phone_number, "RU")
    if not phonenumbers.is_valid_number(x):
        print("Номер не валидный")
        return

    timezone_list = timezone.time_zones_for_number(x)
    Carrier = carrier.name_for_number(x, "ru")
    Region = geocoder.description_for_number(x, "ru")
    valid = phonenumbers.is_valid_number(x)
    possible = phonenumbers.is_possible_number(x)

    print("Оператор: ", Carrier)
    print(x)
    print("Часовой пояс: ", timezone_list)

    if valid:
        print("Номер валидный")
    else:
        print("Номер не валидный")

    if possible:
        print("Номер активен")
    else:
        print("Номер не активен")

    print("Тг: t.me/" + phone_number)
    print("WhatsApp: wa.me/" + phone_number)
    print("Вайбер: viber.click/" + phone_number)
    print("Фэйсбук: m.me/" + phone_number)
    print("Возможные имена: gogtc.co/search/" + phone_number)
    print("Упоминания в соцсетях: https://cse.google.com/cse?cx=006976128084956795641:ad1xj14zfap&q=" + phone_number)
    print("Дополнительная информация: https://search.0t.rocks/records?phoneNumbers=" + phone_number)


def for_windows(phone_number):
    x = phonenumbers.parse(phone_number, "RU")
    timezone_list = timezone.time_zones_for_number(x)
    Carrier = carrier.name_for_number(x, "ru")
    Region = geocoder.description_for_number(x, "ru")
    valid = phonenumbers.is_valid_number(x)
    possible = phonenumbers.is_possible_number(x)

    info = (
        f"Номер телефона: {phone_number}\n"  
        f"Часовой пояс: {timezone_list}\n"
        f"Оператор: {Carrier}\n"
        f"Регион: {Region}\n"
        f"Валидный: {valid}\n"
        f"Активный/нет: {possible}"
    )
    return info

