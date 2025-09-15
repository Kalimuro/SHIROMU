import aiohttp
import asyncio
from urllib.parse import quote
from g4f.client import Client


class UsernameSearch:
    def __init__(self):
        self.username = ""
        self.results = {}
        self.platforms = {
            "Twitter": "https://twitter.com/",
            "Instagram": "https://instagram.com/",
            "Facebook": "https://facebook.com/",
            "Reddit": "https://www.reddit.com/user/",
            "LinkedIn": "https://linkedin.com/in/",
            "TikTok": "https://tiktok.com/@",
            "Pinterest": "https://pinterest.com/",
            "VK": "https://vk.com/",
            "Odnoklassniki": "https://ok.ru/",
            "Flickr": "https://www.flickr.com/people/",
            "GitHub": "https://github.com/",
            "GitLab": "https://gitlab.com/",
            "StackOverflow": "https://stackoverflow.com/users/",
            "Bitbucket": "https://bitbucket.org/",
            "Dev.to": "https://dev.to/",
            "HackerRank": "https://hackerrank.com/",
            "LeetCode": "https://leetcode.com/",
            "Kaggle": "https://www.kaggle.com/",
            "Steam": "https://steamcommunity.com/id/",
            "Epic Games": "https://www.epicgames.com/account/",
            "Xbox": "https://xboxgamertag.com/search/",
            "PlayStation": "https://psnprofiles.com/",
            "Roblox": "https://www.roblox.com/user.aspx?username=",
            "Twitch": "https://twitch.tv/",
            "Яндекс.Дзен": "https://zen.yandex.ru/user/",
            "Habr": "https://habr.com/ru/users/",
            "VC.ru": "https://vc.ru/u/",
            "Pikabu": "https://pikabu.ru/@",
            "Rutube": "https://rutube.ru/channel/",
            "Telegram": "https://t.me/",
            "Spotify": "https://open.spotify.com/user/",
            "eBay": "https://www.ebay.com/usr/",
            "Amazon": "https://www.amazon.com/gp/profile/amzn1.account.",
            "Quora": "https://www.quora.com/profile/",
            "Medium": "https://medium.com/@",
            "Wikipedia": "https://en.wikipedia.org/wiki/User:"
        }

    async def check_platform(self, session, platform, url, username_variant):
        try:
            full_url = url + quote(username_variant)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9"
            }

            async with session.get(full_url, headers=headers, timeout=6) as response:
                if response.status == 200:
                    text = await response.text()

                    if not any(e in text.lower() for e in ["not found", "doesn't exist", "404", "error", "не найдено"]):
                        variant_key = f"{platform} ({'@' if username_variant.startswith('@') else 'без @'})"
                        self.results[variant_key] = full_url
                        print(f"[+] {variant_key}: {full_url}")

        except Exception:
            pass

    async def search_all(self):
        self.results = {}
        print(f"\nПоиск аккаунтов для: {self.username}")

        connector = aiohttp.TCPConnector(limit=50, force_close=True)
        timeout = aiohttp.ClientTimeout(total=30)

        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            tasks = []

            username_variants = [self.username, f"@{self.username}"]

            for platform, url in self.platforms.items():
                for username_variant in username_variants:
                    tasks.append(self.check_platform(session, platform, url, username_variant))

            for i in range(0, len(tasks), 50):
                await asyncio.gather(*tasks[i:i + 50])

        print(f"\nНайдено аккаунтов: {len(self.results)}")

    async def gpt_help(self):
        if not self.results:
            print("❌ Нет результатов для анализа.")
            return

        print("\n🤖 Анализирую результаты с помощью SHIROMU-helper...")

        try:
            client = Client()
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "user", "content": f"Я OSINT-специалист, вот какие социальные сети удалось найти при "
                                                f"поиске в открытых источниках для username {self.username}: {self.results}. "
                                                f"Проанализируй найденные платформы и дай конкретные рекомендации "
                                                f"для дальнейшего исследования: какие данные можно извлечь, "
                                                f"какие связи установить, на что обратить особое внимание. "
                                                f"Будь конкретен и предложи пошаговый план действий."}],
                web_search=False
            )
            print("\n" + "=" * 80)
            print("💡 РЕКОМЕНДАЦИИ SHIROMU-helper ДЛЯ ДАЛЬНЕЙШЕГО ИССЛЕДОВАНИЯ:")
            print("=" * 80)
            print(response.choices[0].message.content)
            print("=" * 80)

        except Exception as e:
            print(f"❌ Ошибка при обращении к SHIROMU-helper")


async def main():
    searcher = UsernameSearch()

    while True:
        username = input("\nВведите никнейм: ").strip()

        if username:
            if username.startswith('@'):
                username = username[1:]

            searcher.username = username
            await searcher.search_all()

            await searcher.gpt_help()

        else:
            print("Ошибка: введите никнейм")
