
import requests
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder, carrier
import instaloader
import socket
import pyautogui
import time
from faker import Faker
from colorama import Fore, init
from art import *


init()

while True:

    tprint("SHIROMU")

    print(Fore.BLUE + "[1] Поиск по номеру телефона" + Fore.RESET)
    print(Fore.BLUE + "[2] Поиск по электронгой почте(осинт)" + Fore.RESET)
    print(Fore.BLUE + "[3] Поиск по паспортным данным(осинт)" + Fore.RESET)
    print(Fore.BLUE + "[4] Поиск по адресу(осинт)" + Fore.RESET)
    print(Fore.BLUE + "[5] Поиск по IP адресу" + Fore.RESET)
    print(Fore.BLUE + '[6] Поиск по Instagram' + Fore.RESET)
    print(Fore.BLUE + "[7] Информация о софте" + Fore.RESET)
    print(Fore.BLUE + "[8] Поиск IP-адреса по домену" + Fore.RESET)
    print(Fore.BLUE + "[9] Спамер" + Fore.RESET)
    print(Fore.BLUE + "[10] Сканер портов" + Fore.RESET)
    print(Fore.BLUE + "[11]Создание фейк-личности" + Fore.RESET)
    print(Fore.BLUE + '[12]Поиск по никнейму' + Fore.RESET)
    print(Fore.BLUE + "[esc] Выход" + Fore.RESET)

    vd = int(input("Выберите действие: "))

    if vd == 1:
        phone_number = input("Введите номер телефона(формат: +79304669445): ")
        if phone_number is False:
            print("Неверно введен номер")
        else:
            x = phonenumbers.parse(phone_number)
            timezone = timezone.time_zones_for_number(x)
            Carrier = carrier.name_for_number(x, "ru")
            Region = geocoder.description_for_number(x, "ru")
            valid = phonenumbers.is_valid_number(x)
            possible = phonenumbers.is_possible_number(x)

            print("Оператор: ", Carrier)
            print(x)
            print("Часовой пояс: ", timezone)
            print(possible)

            if valid is True:
                print("Номер валидный")
            else:
                print("Номер не валидный")


    if vd == 2:
        print('В разработке...')

    if vd == 3:
        print('В разработке...')

    if vd == 4:
        print('В разработке...')

    if vd == 5:
        def get_info_by_ip(ip="127.0.0.1"):
            try:
                response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
                data = {
                    '[IP]': response.get('query'),
                     '[Провайдер]':  response.get('isp'),
                     "[Организация]": response.get('org'),
                     '[Страна]': response.get('country'),
                     '[Регион]': response.get('regionName'),
                     '[Город]': response.get('city'),
                     '[Почтовый код]': response.get('zip'),
                     '[Широта]': response.get('lat'),
                     '[Долгота]': response.get('lon')
                }
                for k, v in data.items():
                    print(f'{k}:{v}')
            except requests.exceptions.ConnectionError:
                print("Произошла какая-то ошибка, попробуй снова, idk")

        def main():
            ip = input("Введите IP-адрес таргета: ")
            get_info_by_ip(ip=ip)
        if __name__ == '__main__':
            main()

    if vd == 6:
        il = instaloader.Instaloader()

        name = input("Введите username таргета: ")
        profile = instaloader.Profile.from_username(il.context, username=name)
        print(f'Информация о профиле: {name}\n {profile.biography}\n Постов: {profile.mediacount}\nПодписчиков: {profile.followers}')

    if vd == 7:
        print("SHIROMU находится на стадии бета-теста и постоянно обновляется.")
        print("Вскоре будут постепенно добавляться новые функции софта, ожидайте")
        print("Данная версия абсолютно бесплатная, предназначена для общего использования и поиска информации по открытым"
              " источникам")
        print("Поиск может иногда занимать продолжительное время(от 1 до 5 минут).")
        print( "Если у вас имеются какие-то вопросы/предложения, можете задать их в дискорд канале")
        print("База данных пока что не включена в эту версию, так что на данный момент это просто osint тулка, следите за"
              " обновлениями в дискорд канале - https://discord.gg/ZAfg7YxSVE" )

    if vd == 8:
        def get_ip_by_hostname():
            hostname = input("Введите домен: ")
            try:
                return f"Сервис: {hostname}\nIP: {socket.gethostbyname(hostname)}"
            except socket.gaierror as error:
                return f"Произошла ошибка, попробуйте снова"
        def main():
            print(get_ip_by_hostname())
        if __name__ == "__main__":
            main()

    if vd == 9:
        def SendMessage():
            message = input("Паста для спама: ")
            amount = input("Кол-во отправки: ")
            time.sleep(4)

            for i in range:
                pass
            while amount > 0:
                amount -= 1
                pyautogui.typewrite(message.strip())
                pyautogui.press("enter")
        SendMessage()

    if vd == 10:

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        target = input('Введите IP: ')
        target_ip = socket.gethostbyname(target)
        print('Сканирование...:', target_ip)

        def port_scan(port):
            try:
                s.connect((target_ip, port))
                return True
            except:
                return False

        start = time.time()

        for port in range(1000):
            if port_scan(port):
                print(f'Порт {port} открыт')
            else:
                print(f'Порт {port} закрыт')

        end = time.time()
        print(f'Time taken {end - start:.2f} seconds')


    if vd == 11:
        faker = Faker('RU')
        name = faker.name()
        adress = faker.address()
        email = faker.email()
        job = faker.job()
        phone = faker.phone_number()
        pasport = faker.passport_number()
        print(f'Имя: {name}\nАдрес:{adress}\nЭл.почта:{email}\nНомер телефона:{phone}\nРабота:{job}\nПаспорт:{pasport}')

    if vd == 12:
        print('В разработке...')


