from utils.imports import *


def get_info_by_ip(ip="127.0.0.1"):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[Провайдер]': response.get('isp'),
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


def get_ip_by_hostname(hostname):
    try:
        return f"Сервис: {hostname}\nIP: {socket.gethostbyname(hostname)}"
    except socket.gaierror as error:
        return f"Произошла ошибка, попробуйте снова"