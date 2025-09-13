import re
import maigret
from maigret.sites import MaigretDatabase

MAIGRET_DB_FILE = 'data.json'
COOKIES_FILE = "cookies.txt"
id_type = "username"
USERNAME_REGEXP = r'^[a-zA-Z0-9-_\.]{5,}$'

TOP_SITES_COUNT = 1500
TIMEOUT = 30


class Logger_for_Maigret:
    def debug(self, msg):
        pass

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        pass

    def level(self, level):
        pass


async def maigret_search(username):
    db = MaigretDatabase().load_from_path(MAIGRET_DB_FILE)
    sites = db.ranked_sites_dict(top=TOP_SITES_COUNT)

    results = await maigret.search(
        username=username,
        site_dict=sites,
        timeout=TIMEOUT,
        logger=Logger_for_Maigret(),
        id_type=id_type,
        cookies=COOKIES_FILE,
    )
    return results


def format_results(found_sites):
    if not found_sites:
        return [], []

    found_accounts = len(found_sites)
    formatted_links = []
    detailed_results = []

    for site, link in found_sites:
        formatted_links.append(f'{site}: {link}')
        detailed_results.append({'site': site, 'url': link})

    messages = []
    current_message = f'{found_accounts} аккаунтов найдено:\n'

    for link in formatted_links:
        if len(current_message + link + '\n') > 4096:
            messages.append(current_message.rstrip('\n'))
            current_message = ''
        current_message += link + '\n'

    if current_message:
        messages.append(current_message.rstrip('\n'))

    return messages, detailed_results


async def search(username):
    try:
        results = await maigret_search(username)
    except Exception as e:
        print(f"Ошибка, пишите Shiro")
        return [], []

    found_exact_accounts = []

    for site, data in results.items():
        if data.get('url_user'):
            found_exact_accounts.append((site, data['url_user']))
        elif data.get('exists', False):
            url = data.get('url', f'https://{site}.com/{username}')
            found_exact_accounts.append((site, url))

    if not found_exact_accounts:
        return [], []

    messages, detailed_results = format_results(found_exact_accounts)
    return messages, detailed_results


async def main():
    while True:
        try:
            username = input("Введите никнейм:").strip().lstrip('@')

            if username.lower() == 'quit':
                break

            username_regexp = re.search(USERNAME_REGEXP, username)
            if not username_regexp:
                print("Неправильно введен username. Username должен содержать > 4 символов.")
                continue

            print(f'Поиск по: {username}...')

            messages, detailed_results = await search(username)

            if not messages:
                print('Аккаунты не найдены')
            else:
                for message in messages:
                    print(message)

                print(f'\nНайдено {len(detailed_results)} аккаунтов:')
                for result in detailed_results:
                    print(f"  {result['site']}: {result['url']}")

            print('-' * 50)

        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            print(f'Ошибка, пишите Sh1ro')

