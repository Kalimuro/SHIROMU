def main():
    fio = str(input('Введите ФИО жертвы: '))
    nomertelephona = int(input('Введите номер телефона жертвы: '))
    operator = str(input('Введите оператора жертвы: '))
    strana = str(input('Введите страну жертвы: '))
    gorod = str(input('Введите город жертвы: '))
    adres = str(input('Введите адрес жертвы: '))
    timezone = input('Введите часовой пояс жертвы: ')
    gender = str(input('Введите пол: '))
    vozrast = str(input('Введите возраст жертвы: '))
    documents = input('Введите документы: ')
    mother = str(input('Введите имя матери жертвы: '))
    father = str(input('Введите имя бати жертвы: '))
    cat = str(input('Введите имя кота жертвы: '))
    dog = str(input('Введите имя собаки жертвы: '))
    grandma = str(input('Введите имя бабки жертвы: '))
    grandpa = str(input('Введите имя деда жертвы: '))
    car = input('Введите номер машины жертвы: ')
    sister = input('Введите имя сестры жертвы: ')
    brother = input('Введите имя брата жертвы')
    cords = input('Введите координаты провайдера жертвы: ')
    vk = input('Введите ссылку на вк жертвы: ')
    tg = input('Введите username telegram жертвы: ')
    tgid = input('Введите телеграм-id жертвы: ')
    email = input('Введите email/s жертвы: ')
    password = input('Введите пароли жертвы: ')
    foto = input('Введите ссылки на фотограии жертвы: ')
    doxedby = input('Введите ник доксера: ')
    reason = input('Введите причину докса: ')
    logs = input('Введите ссылку на файл с логами жертвы: ')
    ip = int(input('Введите ip жертвы: '))
    nalichieproxyilivpn = str(input('Есть прокси или впн у жертвы(да/нет)?: '))
    other = input('Введите другую информацию о жертве: ')
    github_tool = 'SHIROMU'


    print('____________________________________________________________________________________')
    print('    ██████╗   ██████╗  ██╗  ██╗')
    print('    ██╔══██╗ ██╔═══██╗ ╚██╗██╔╝')
    print('    ██║  ██║ ██║   ██║  ╚███╔╝')
    print('    ██║  ██║ ██║   ██║  ██╔██╗')
    print('    ██████╔╝ ╚██████╔╝ ██╔╝ ██╗')
    print(f'    ╚═════╝   ╚═════╝  ╚═╝  ╚═╝   Software -  {github_tool}')
    print('_____________________________________________________________________________________')
    print(f'Doxed By : {doxedby} ')
    print(f'    Reason   : {reason}')
    print('__________PERSONAL INFO___________')
    print(f'ФИО: {fio}')
    print(f'Номер телефона: {nomertelephona}')
    print(f'Оператор: {operator}')
    print(f'Страна: {strana}')
    print(f'Город: {gorod}')
    print(f'Адрес: {adres}')
    print(f'Часовой пояс: {timezone}')
    print(f'Пол: {gender}')
    print(f'Возраст: {vozrast}')
    print(f'Документы: {documents}')
    print(f'Ссылки на Фотографии: {foto}')
    print(f'IP: {ip}')
    print(f'Координаты провайдера: {cords}')
    print('____________FAMILY_______________')
    print(f'Мать: {mother}')
    print(f'Отец: {father}')
    print(f'Кот: {cat}')
    print(f'Собака: {dog}')
    print(f'Бабка: {grandma}')
    print(f'Дед: {grandpa}')
    print(f'Сестра: {sister}')
    print(f'Брат: {brother}')
    print('____________SOCIAL_______________')
    print(f'Вк: {vk}')
    print(f'Telegram: {tg}')
    print(f'TelegramID: {tgid}')
    print(f'Emails: {email}')
    print('___________TRANSPORT_____________')
    print(f'Автомобили: {car}')
    print('____________OTHER________________')
    print(f'Пароли: {password}')
    print(f'Использование VPN/Proxy: {nalichieproxyilivpn}')
    print(f'Ссылка на файл с логом: {logs}')
    print(f'Прочая информация: {other}')
if __name__ == '__main__':
    main()