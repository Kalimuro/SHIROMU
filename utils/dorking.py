import sys
import time

from googlesearch import search

dorks_list = [
    "site:{user_input}",
    "inurl:{user_input}",
    "intitle:{user_input}",
    "filetype:pdf {user_input}",
    "intext:{user_input}",
    "ext:log inurl:/admin/logs/{user_input}",
    "inurl:login.php {user_input}",
    "site:{user_input}",
    "inurl:{user_input}",
    "intitle:{user_input}",
    "intext:{user_input}",
    "allinurl:{user_input}",
    "allintitle:{user_input}",
    "allintext:{user_input}",
    "filetype:pdf {user_input}",
    "filetype:doc {user_input}",
    "filetype:docx {user_input}",
    "filetype:xls {user_input}",
    "filetype:xlsx {user_input}",
    "filetype:csv {user_input}",
    "filetype:txt {user_input}",
    "filetype:log {user_input}",
    "filetype:sql {user_input}",
    "filetype:conf {user_input}",
    "filetype:ini {user_input}",
    "filetype:bak {user_input}",
    "filetype:pem {user_input}",
    "filetype:zip {user_input}",
    "filetype:tar {user_input}",
    'filetype:xls intext:"password" site:{user_input}',
    'filetype:txt intext:"username" intext:"password" site:{user_input}',
    'filetype:conf intext:"password=" site:{user_input}',
    'filetype:ini intext:"password=" site:{user_input}',
    'filetype:pem intext:"PRIVATE KEY" site:{user_input}',
    'filetype:sql "dump" site:{user_input}',
    '"API_KEY" intext:"{user_input}"',
    "inurl:admin site:{user_input}",
    "inurl:login site:{user_input}",
    "inurl:dashboard site:{user_input}",
    "intitle:login site:{user_input}",
    "intitle:admin site:{user_input}",
    "\"powered by wordpress\" intitle:login",
    "inurl:.php?id= site:{user_input}",
    "inurl:view-source:site:{user_input}",
    "intitle:index.of site:{user_input}",
    "\"about me\" \"{user_input}\"",
    "\"contact\" \"{user_input}\"",
    "\"resume\" \"{user_input}\"",
    "\"cv\" \"{user_input}\"",
    "site:linkedin.com \"{user_input}\"",
    "site:{user_input} ext:php",
    "site:{user_input} ext:asp",
    "site:{user_input} ext:jsp",
    "site:{user_input} \"error\" \"warning\""
]

DELAY_SECONDS = 6


def perform_google_search(dork_query):
    print(f"\n--- Результаты по дорку: \"{dork_query}\" ---")
    try:
        results = search(dork_query, num_results=10, lang="ru", proxy=False, ssl_verify=True)

        found_any = False
        for i, url in enumerate(results):
            print(f"{i + 1}. {url}")
            found_any = True

        if not found_any:
            print("Ничего не найдено.")

    except Exception as e:
        print(f"Произошла ошибка при поиске {e}")
        print("Возможно вас забанил гугл :) Просто смените IP или подтвердите что вы не робот")


def main():
    user_input = input("\nВведите ваш запрос (например, 'Василий Думкин Васильевич' или '+8613290594348'): ")

    if not user_input.strip():
        print("Вы ввели пустой запрос...")
        sys.exit(1)

    print(f"\n--- Поиск с помощью: \"{user_input}\" ---")

    for i, template in enumerate(dorks_list):
        dork_to_search = template.format(user_input=user_input)
        perform_google_search(dork_to_search)

        if i < len(dorks_list) - 1:
            time.sleep(DELAY_SECONDS)


if __name__ == "__main__":
    main()
