from datetime import datetime
import requests
import json
from bs4 import BeautifulSoup


def get_discord_user_info(username):
    trans = {
        "type": "Тип",
        "user_id": "Дс ID",
        "actual_name": "Main Nickname",
        "actual_avatar": "Ава",
        "display_name": "Отображаемое имя",
        "time_in_voice": "Время в гс (сек)",
        "last_date_in_voice": "Последнее дата/время в гс",
        "gender": "Пол",
        "total_messages": "Всего сообщений найдено",
        "voice_info": "Информация о гс",
        "status": "Статус",
        "guild_id": "ID сервера",
        "channel_id": "ID войса",
        "channel_name": "Название канала",
        "category_id": "ID категории",
        "category_name": "Категория",
        "server_name": "Название дс сервера",
        "server_avatar": "Ава сервера",
        "last_voice_time": "Последнее время в гс",
        "self_stream": "Демка",
        "self_video": "Видео-фвайлы",
        "role_guilds": "Сервера в которых есть роли",
        "owner_guilds": "Сервера, в которых есть овнерка"
    }

    def format_value(key, value):
        if key == "time_in_voice" and isinstance(value, int):
            hours = value // 3600
            minutes = (value % 3600) // 60
            seconds = value % 60
            return f"{hours}ч {minutes}м {seconds}с ({value} сек)"

        elif key in ["last_date_in_voice", "last_voice_time"] and value:
            return value.replace("T", " ").replace(".421Z", "").replace("Z", "")

        elif value is None:
            return "Не найдено"

        elif value is False:
            return "Нет"

        elif value is True:
            return "Да"

        elif isinstance(value, list) and len(value) == 0:
            return "Отсутствуют"

        return value

    def print_pretty_russian(data, indent=0, parent_key=""):
        result = []
        for key, value in data.items():
            russian_key = trans.get(key, key)

            if isinstance(value, dict):
                result.append(" " * indent + f"🎯 {russian_key}:")
                result.extend(print_pretty_russian(value, indent + 2, key))
            else:
                formatted_value = format_value(key, value)
                result.append(" " * indent + f"• {russian_key}: {formatted_value}")
        return result

    url = f"https://discord-sensor.com/api/tracker/get-user-info?content={username}"
    response = requests.get(url)

    if response.status_code != 200:
        return f"Ошибка, пишите sh1ro)"

    try:
        data = response.json()
    except json.JSONDecodeError:
        return "Ошибка: Неверный формат ответа от сервера"

    result_lines = []
    result_lines.append("=" * 60)
    result_lines.append("👤 ИНФОРМАЦИЯ О ТАРГЕТЕ")
    result_lines.append("=" * 60)

    main_info = {k: v for k, v in data.items() if
                 k not in ['voice_info', 'customization', 'role_guilds', 'owner_guilds']}
    result_lines.extend(print_pretty_russian(main_info))

    if 'voice_info' in data and data['voice_info']:
        result_lines.append("\n🎤ИНФОРМАЦИЯ ПО ВОЙСАМ:")
        result_lines.append("-" * 40)
        result_lines.extend(print_pretty_russian(data['voice_info'], 2))

    if 'role_guilds' in data and data['role_guilds']:
        result_lines.append(f"\n• Сервера с ролями: {len(data['role_guilds'])}")
    if 'owner_guilds' in data and data['owner_guilds']:
        result_lines.append(f"• Сервера-владельцы: {len(data['owner_guilds'])}")

    result_lines.append("=" * 60)

    result_lines.append("\nПРИМЕЧАНИЕ: При поиске по discord-id вы получите намного больше информации")
    result_lines.append("=" * 60)

    return "\n".join(result_lines)


def get_info_by_dsid(ds_id):
    url = f"https://discord-sensor.com/api/tracker/get-mutual-guilds/{ds_id}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        data = response.json()

        print("=" * 80)
        print("🎯 ИНФОРМАЦИЯ О ВСЕХ СЕРВЕРАХ ТАРГЕТА")
        print("=" * 80)
        print(f"👤 Discord ID: {ds_id}")
        print(f"📊 Всего серверов: {data['item_count']}")
        print("=" * 80)

        sorted_servers = sorted(data['guild_list'], key=lambda x: (not x['left'], x['name']))

        current_servers = []
        left_servers = []

        for i, server in enumerate(sorted_servers, 1):
            status = "✅ На сервере" if not server['left'] else "❌ Ливнул"
            status_emoji = "✅" if not server['left'] else "❌"

            print(f"\n{status_emoji} СЕРВЕР #{i}")
            print(f"   🏷️  Название: {server['name']}")
            print(f"   🔢 ID сервера: {server['id']}")
            print(f"   👥 Участников: {server['member_count']:,}")
            print(f"   🎤 В голосовых: {server['voice_member_count']}")
            print(f"   💬 Сообщений: {server['messages']}")

            if server['voice_seconds'] > 0:
                hours = server['voice_seconds'] // 3600
                minutes = (server['voice_seconds'] % 3600) // 60
                seconds = server['voice_seconds'] % 60
                voice_time = f"{hours}ч {minutes}м {seconds}с"
            else:
                voice_time = "0 сек"

            print(f"   ⏰ Время в войсе: {voice_time}")
            print(f"   📍 Статус: {status}")
            print("-" * 40)

            if server['left']:
                left_servers.append(server)
            else:
                current_servers.append(server)

        print("\n📊 СТАТИСТИКА:")
        print(f"   ✅ На сервере: {len(current_servers)}")
        print(f"   ❌ Ливнул: {len(left_servers)}")
        print("=" * 80)

        return {
            'discord_id': ds_id,
            'total_servers': data['item_count'],
            'current_servers': current_servers,
            'left_servers': left_servers,
            'all_servers': data['guild_list'],
            'raw_data': data
        }

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка, пишите sh1ro", e)
        return None
    except Exception as e:
        print(f"❌Ошибка, пишите sh1ro", e)
        return None


def get_nicks_by_id(ds_id):
    url = f"https://discord-sensor.com/api/tracker/get-nicknames/{ds_id}?page=0"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(f"❌ Ошибка, пишите sh1ro")
            return None

        data = response.json()

        if not data.get('success', False):
            print("❌ Ошибка, пищите sh1ro")
            return None

        print("=" * 80)
        print("🎯 TARGET DISCORD NACKNAMES")
        print("=" * 80)
        print(f"👤 Discord ID таргета: {data['userId']}")
        print(f"📊 Всего никнеймов: {data['total_count']}")

        if data['hasNextPage']:
            print("ℹ️ Найдены еще никнеймы...")
        print("=" * 80)

        for i, nickname in enumerate(data['nicknames'], 1):
            print(f"\n🏷️  НИКНЕЙМ #{i}")
            print(f"   📛 Никнейм: {nickname['nickname']}")
            print(f"   🆔: {nickname['id']}")

            if nickname.get('guild'):
                guild = nickname['guild']
                print(f"   🏰 Сервер: {guild['name']}")
                print(f"   🔢 ID сервера: {guild['id']}")
                if guild.get('vanity_url'):
                    print(f"   🔗 Vanity URL: {guild['vanity_url']}")
            else:
                print(f"   🏰 Сервер: No")

            if nickname.get('time'):
                try:
                    ru_months = {
                        'января': '01', 'февраля': '02', 'марта': '03',
                        'апреля': '04', 'мая': '05', 'июня': '06',
                        'июля': '07', 'августа': '08', 'сентября': '09',
                        'октября': '10', 'ноября': '11', 'декабря': '12'
                    }

                    time_str = nickname['time']
                    for ru_month, num_month in ru_months.items():
                        time_str = time_str.replace(ru_month, num_month)

                    dt = datetime.strptime(time_str, '%d %m %Y %H:%M:%S')
                    formatted_time = dt.strftime('%d.%m.%Y %H:%M:%S')
                    print(f"   ⏰ Дата изменения: {formatted_time}")
                except:
                    print(f"   ⏰ Дата изменения: {nickname['time']}")
            else:
                print(f"   ⏰ Дата изменения: Не найдено")

            status = "👁️  Видимый" if not nickname.get('is_hidden', False) else "👻 Скрытый"
            print(f"   📍 Статус: {status}")
            print("-" * 40)

        print(f"\n📊 СТАТИСТИКА:")
        print(f"   📛 Всего найдено: {data['total_count']}")
        print(
            f"   🏰 Найдено Серверов: {len(set(nick['guild']['id'] for nick in data['nicknames'] if nick.get('guild')))}")
        print("=" * 80)

        return {
            'discord_id': data['userId'],
            'total_count': data['total_count'],
            'page': data['page'],
            'has_next_page': data['hasNextPage'],
            'nicknames': data['nicknames'],
            'raw_data': data
        }

    except requests.exceptions.RequestException as e:
        print(f"❌ Ошибка")
        return None
    except Exception as e:
        print(f"❌ Ошибка")
        return None


def get_all_nicknames(ds_id):
    all_nicknames = []
    page = 0

    while True:
        url = f"https://discord-sensor.com/api/tracker/get-nicknames/{ds_id}?page={page}"
        response = requests.get(url)

        if response.status_code != 200:
            break

        data = response.json()

        if not data.get('success', False):
            break

        all_nicknames.extend(data['nicknames'])

        if not data['hasNextPage']:
            break

        page += 1

    return all_nicknames


def get_friends_by_id(user_id='1117374856011464704'):
    url = f"https://discord-sensor.com/api/tracker/get-friends/{user_id}?page=0"
    response = requests.get(url)
    data = response.json()

    if data['success']:
        display_friends(data)
    else:
        print("❌ Ошибка... Снова... Пишите sh1ro, а лучше в чат the flying dutchman")


def display_friends(data):
    friends_info = data['friends']

    print("🎮" + "=" * 50 + "🎮")
    print(f"👥 ДРУЗЬЯ ПОЛЬЗОВАТЕЛЯ 👥")
    print("🎮" + "=" * 50 + "🎮")
    print(f"📊 Всего друзей: {friends_info['totalFriends']} 👤")
    print(f"📑 Страница: {friends_info['page'] + 1}/{friends_info['totalPages']} 📄")
    print("-" * 55)

    for i, friend in enumerate(friends_info['records'], 1):
        print(f"\n{f'{i}. 👤 ДРУГ #{i}':-^55}")
        print(f"   🆔 ID: {friend['friendId']}")
        print(f"   📛 Имя: {friend['username']}")
        print(f"   🖼️ Ава: {friend['avatar']}")

        hours = int(friend['friends_online_duration']) // 3600
        minutes = (int(friend['friends_online_duration']) % 3600) // 60

        print(f"   ⏱️  Время онлайн: {hours}ч {minutes}м ⏳")

        last_online = datetime.fromisoformat(friend['last_friends_online'].replace('Z', '+00:00'))
        formatted_date = last_online.strftime("%d.%m.%Y в %H:%M")
        print(f"   📅 Последний онлайн: {formatted_date} 🕒")

    if data['mutualFriends']:
        print(f"\n🤝 Общих друзей: {len(data['mutualFriends'])}")
    else:
        pass

    print("\n" + "🎮" + "=" * 50 + "🎮")


def sobitiya_usera(user_id):
    url = f'https://discord-sensor.com/api/users/get-latest-events/{user_id}?subTab=server_history&limit=20&page=2'

    try:
        response = requests.get(url)
        data = response.json()

        result_text = format_events(data)

        print(result_text)

        return result_text

    except Exception as e:
        error_message = f"❌ Ошибка при получении данных: {e}"
        print(error_message)
        return error_message


def format_events(data):
    if not data or 'results' not in data:
        return "📭 Нет данных о истории серверов пользователя"

    events = data['results']

    if not events:
        return "📭 Пользователь не имеет событий на серверах"

    output = f"📊 ИСТОРИЯ DISCORD СЕРВЕРОВ ТАРГЕТА\n"
    output += f"Всего событий: {data.get('total_count', 0)}\n"
    output += f"Показано: {data.get('item_count', 0)} из {len(events)}\n"
    output += "=" * 60 + "\n\n"

    for i, event in enumerate(events, 1):
        event_type = "✅ ПРИСОЕДИНИЛСЯ" if event.get('type') else "❌ ПОКИНУЛ"

        timestamp = event.get('timestamp', '')
        try:
            dt = datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
            formatted_date = dt.strftime("%d.%m.%Y в %H:%M:%S")
        except:
            formatted_date = timestamp

        guild_name = event.get('guild_name', 'Неизвестный сервер')
        guild_id = event.get('guild_id', 'N/A')

        output += f"{i}. {event_type}\n"
        output += f"   🏰 Сервер: {guild_name}\n"
        output += f"   📍 ID сервера: {guild_id}\n"
        output += f"   🕐 Дата: {formatted_date}\n"
        output += f"   🔢 ID события: {event.get('id', 'N/A')}\n"

        if i < len(events):
            output += "   " + "-" * 40 + "\n"
        else:
            output += "\n"

    output += "=" * 60
    return output


def voice_history(user_id):
    url = f'https://discord-sensor.com/api/users/get-latest-events/{user_id}?subTab=voice_history&limit=20&page=1'

    try:
        response = requests.get(url)
        data = response.json()
        result_text = format_voice_history(data)
        print(result_text)
        return result_text
    except Exception as e:
        error_message = f"❌ Ошибка при получении данных: {e}"
        print(error_message)
        return error_message


def format_duration(seconds):
    if seconds < 60:
        return f"{seconds} сек"
    elif seconds < 3600:
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes} мин {secs} сек"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours} ч {minutes} мин {secs} сек"


def format_voice_history(data):

    if not data or 'results' not in data:
        return "📭 Нет данных о голосовой истории таргета"

    events = data['results']

    if not events:
        return "📭 Таргет не имеет истории голосовых каналов"

    output = f"🎧 ИСТОРИЯ АКТИВНОСТИ В ГОЛОСОВЫХ КАНАЛАХ \n"
    output += f"Всего сессий: {data.get('total_count', 0)}\n"
    output += f"Показано: {len(events)} из {data.get('total_count', 0)}\n"
    output += "=" * 70 + "\n\n"

    for i, event in enumerate(events, 1):

        join_time = event.get('join_timestamp', '')
        leave_time = event.get('leave_timestamp', '')

        try:
            join_dt = datetime.fromisoformat(join_time.replace('Z', '+00:00'))
            leave_dt = datetime.fromisoformat(leave_time.replace('Z', '+00:00'))
            formatted_join = join_dt.strftime("%d.%m.%Y в %H:%M:%S")
            formatted_leave = leave_dt.strftime("%d.%m.%Y в %H:%M:%S")
            date_only = join_dt.strftime("%d.%m.%Y")
        except:
            formatted_join = join_time
            formatted_leave = leave_time
            date_only = "Неизвестно"

        guild_name = event.get('guild_name', 'Неизвестный сервер')
        channel_name = event.get('channel_name', 'Неизвестный канал')
        voice_duration = event.get('voice_duration', 0)

        output += f"{i}. 🎤 ГОЛОСОВАЯ СЕССИЯ ({date_only})\n"
        output += f"   🏰 Сервер: {guild_name}\n"
        output += f"   📍 Канал: {channel_name}\n"
        output += f"   ⏱️  Длительность: {format_duration(voice_duration)}\n"
        output += f"   🔽 Вошел: {formatted_join}\n"
        output += f"   🔼 Вышел: {formatted_leave}\n"
        output += f"   🔢 ID сессии: {event.get('id', 'N/A')}\n"
        output += f"   🆔 ID сервера: {event.get('guild_id', 'N/A')}\n"
        output += f"   🆔 ID канала: {event.get('channel_id', 'N/A')}\n"

        if i < len(events):
            output += "   " + "-" * 50 + "\n"
        else:
            output += "\n"

    total_duration = sum(event.get('voice_duration', 0) for event in events)
    avg_duration = total_duration / len(events) if events else 0

    output += "=" * 70

    return output


