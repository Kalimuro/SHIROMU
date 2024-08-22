import os
import subprocess
from os import system
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
import random
import string





init()

while True:

    tprint("SHIROMU")

    print(Fore.BLUE + "[1] Поиск по номеру телефона" + Fore.RESET)
    print(Fore.BLUE + "[2] Поиск по электронгой почте(осинт)" + Fore.RESET)
    print(Fore.BLUE + "[3] Поиск по номеру документа(осинт)" + Fore.RESET)
    print(Fore.BLUE + "[4] Поиск по адресу(осинт)" + Fore.RESET)
    print(Fore.BLUE + "[5] Поиск по IP адресу" + Fore.RESET)
    print(Fore.BLUE + '[6] Поиск по Instagram' + Fore.RESET)
    print(Fore.BLUE + "[7] Информация о софте" + Fore.RESET)
    print(Fore.BLUE + "[8] Поиск IP-адреса по домену" + Fore.RESET)
    print(Fore.BLUE + "[9] Спамер" + Fore.RESET)
    print(Fore.BLUE + "[10] Сканер портов" + Fore.RESET)
    print(Fore.BLUE + "[11]Создание фейк-личности" + Fore.RESET)
    print(Fore.BLUE + '[12]Поиск по никнейму' + Fore.RESET)
    print(Fore.BLUE + '[13]Поиск по ФИО' + Fore.RESET)
    print(Fore.BLUE + "[14] SMS-бомбер" + Fore.RESET)
    print(Fore.BLUE + "[15] Мануалы" + Fore.RESET)
    print(Fore.BLUE + "[16] Снос тг акков (новая функция)")
    print(Fore.BLUE + "[17] Снос тгк (новая функция)")
    print(Fore.BLUE + "[18] Временная анон почта(новая функция)")
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

            if valid is True:
                print("Номер валидный")
            else:
                print("Номер не валидный")
            if possible is True:
                print("Номер активен")
            else:
                print("Номер не активен")

    if vd == 2:
        print('Этой информации еще нет в базе, ожидайте обновлений...')

    if vd == 3:
        query = input("Введите номер гос.документа: ")
        found = True
        with open('freedb1.txt', 'r', encoding="utf-8") as file:
            for line in file:
                if query in line:
                    print(line)
                    found = True
        if found is False:
            print('Информации еще нету в базе данных, либо что-то введено не корректно')

    if vd == 4:
        query = input("Введите адрес: ")
        found1 = True
        with open('freedb1.txt', 'r', encoding="utf-8") as file:
            for line in file:
                if query in line:
                    print(line)
                    found = True
        if found1 is False:
            print("Информации еще нету в базе данных, либо что-то введено не корректно")

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
        print("Для осуществления поиска по документам, ФИО/ФИ, почте, адресу вам необходимо прокинуть базу данных весом"
              "в 5 гб. Ее вы можете взять в дискорд канале. ")

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
        def is_port_open(host, port):
            s = socket.socket()
            try:
                s.connect((host, port))
            except:
                return False
            else:
                return True
        host = input("Введите IP таргета:")
        print("Сканирование запущено, ожидайте...")
        for port in range(1, 1025):
            if is_port_open(host, port):
                print(f"[+] {host}:{port} открыт")
            else:
                print(f"[!] {host}:{port} закрыт", end="\r")

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
        print('В разработке... Пока что используйте Sherlock')

    if vd == 13:
        query = input("Введите ФИО: ")
        found2 = False
        with open('freedb1.txt', 'r') as file:
            for line in file:
                if query in line:
                    print(line)
                    found2 = True
        if found2 is False:
            print("информации еще нет в базе данных, или что то введено не корректно ")

    if vd == 14:
        phone = input('Введите номер таргета(формат 79009945209): ')
        phone9 = phone[1:]
        while True:
            try:
                requests.post('https://admin.growfood.pro/api/personal-cabinet/v2_0/authentication/send-sms', data={'phone': phone}, headers={})
                print('Сообщение отправлено')
            except:
                 print('Произошла какая-то ошибка, скорее всего sh1ro еблан и не обновил API-шник')
            try:
                requests.post('https://lk.megafon.ru/api/logs/v2/accept', json={'msisdn': phone}, headers={})
                print('Сообщение отправлено')
            except:
                print('Произошла какая-то ошибка, скорее всего sh1ro еблан и не обновил API-шник')

    if vd == 15:

        print(Fore.RED + "[81] Стартовый мануал по ОСИНТУ")
        print(Fore.RED + "[82] Мануал по сносу тг")
        print(Fore.RED + "[83] Мануал по сносу тгк")

        vibor = int(input("Выберите мануал: "))

        if vibor == 81:
            with open("OSINT.txt", "r", encoding="utf-8") as file:
                osint = file.read()
                print(osint)
        if vibor == 82:
            with open("snostg.txt", 'r', encoding='utf-8') as file:
                snostg = file.read()
                print(snostg)
        if vibor == 83:
            with open('snostgc.txt', 'r', encoding='utf-8') as file:
                snostgc = file.read()
                print(snostgc)


    if vd == 16:
        print("В разработке...")

    if vd == 17:
        print("В разработке...")

    if vd == 18:
        API = 'https://www.1secmail.com/api/v1/'
        domains = ["1secmail.com", "1secmail.org", "1secmail.net", "wwjmp.com", "esiix.com", "xojxe.com", "yoggm.com"]
        domain = random.choice(domains)


        def create_username():
            usrname = string.ascii_lowercase + string.digits
            username = ''.join(random.choice(usrname) for i in range(10))
            return username


        def check_mail(mail=''):
            req_link = f'{API}?action=getMessages&login={mail.split("@")[0]}&domain={mail.split("@")[1]}'
            r = requests.get(req_link).json()
            leghth = len(r)

            if leghth == 0:
                print('Пусто :(, обновляется каждые 5 сек')
            else:
                id_list = []

                for i in r:
                    for k, v in i.items():
                        if k == 'id':
                            id_list.append(v)
                print(f'{leghth} сообщений. Обновляется каждые 5 сек')
                current_dir = os.getcwd()
                final_dir = os.path.join(current_dir, 'all_mails')
                if not os.path.exists(final_dir):
                    os.makedirs(final_dir)

                for i in id_list:
                    read_msg = f'{API}?action=readMessage&login={mail.split("@")[0]}&domain={mail.split("@")[1]}&id={i}'
                    r = requests.get(read_msg).json()

                    sender = r.get('from')
                    subject = r.get('subject')
                    date = r.get('date')
                    content = r.get('textBody')

                    mail_file_path = os.path.join(final_dir, f'{i}.txt')

                    with open(mail_file_path, 'w') as file:
                        file.write(
                            f'Отправитель: {sender}\nНа анон почту: {mail}\nФайлы: {subject}\nДата: {date}\nСодержимое:{content}')


        def main():
            try:
                username = create_username()
                mail = f'{username}@{domain}'
                print(f'Временная анон почта: {mail}')

                mail_req = requests.get(f'{API}?login={mail.split("@")[0]}&domain={mail.split("@")[1]}')

                while True:
                    check_mail(mail=mail)
                    time.sleep(5)

            except(KeyboardInterrupt):
                print("Прервано")


        if __name__ == '__main__':
            main()
