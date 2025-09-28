import requests
from bs4 import BeautifulSoup
import re


def search_email_lullar(email):
    url = 'https://lullar-com-3.appspot.com/en'
    payload = {'q': email}

    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        results = {}

        platform_divs = soup.find_all('div', id=True)

        for div in platform_divs:
            platform_id = div.get('id')
            if platform_id in ['fb-root', 'tiktok', 'youtube']:
                continue

            link_tag = div.find('a')
            if link_tag and link_tag.get('href'):
                platform_name = link_tag.get_text(strip=True)
                profile_url = link_tag['href']

                if platform_name and profile_url:
                    results[platform_name] = profile_url

        return results

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка сети: {e}")
        return {}
    except Exception as e:
        print(f"❌ Ошибка парсинга: {e}")
        return {}


def search_email_lullar_simple(email):
    url = 'https://lullar-com-3.appspot.com/en'
    payload = {'q': email}

    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()

        pattern = r'<div id="([^"]+)"><a[^>]+target=[^>]+><b>([^<]+)</b></a><br/><span class=urllink>([^<]+)</span>'
        matches = re.findall(pattern, response.text)

        results = {}
        for platform_id, platform_name, url in matches:
            results[platform_name] = url

        return results

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return {}


def search_email_lullar_advanced(email):
    url = 'https://lullar-com-3.appspot.com/en'
    payload = {'q': email}

    try:
        response = requests.post(url, data=payload, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        results = {}

        left_column = soup.find('div', style=lambda x: x and 'float:left; width:400px' in x)
        if left_column:
            links = left_column.find_all('a')
            for link in links:
                if link.get('href') and link.get('target') == '_blank':
                    platform_name = link.get_text(strip=True)
                    url = link['href']
                    if platform_name and url and not url.startswith('javascript'):
                        results[platform_name] = url

        return results

    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return {}


def print_results(results, email):
    if not results:
        print(f"\n❌ Для email {email} не найдено соцсетей на Lullar")
        return

    print(f"\n✅ Найдено {len(results)} соцсетей для {email}:")
    print("=" * 60)

    for platform, url in results.items():
        print(f"📱 {platform}: {url}")

    print("=" * 60)
