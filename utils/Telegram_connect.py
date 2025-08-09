from telethon import TelegramClient, events
import asyncio


async def get_all_bot_messages(api_id, api_hash, bot_username, message_text, session_name='default_session',
                               timeout=20):
    client = TelegramClient(session_name, api_id, api_hash)
    messages = []
    stop_processing = False

    try:
        await client.connect()
        if not await client.is_user_authorized():
            await client.start()

        try:
            bot_entity = await client.get_entity(bot_username)
        except Exception as e:
            return []

        @client.on(events.NewMessage(from_users=bot_entity))
        async def handler(event):
            nonlocal messages, stop_processing
            try:
                full_text = event.raw_text
                buttons_info = ""
                if event.message.buttons:
                    buttons_info = "\n[Bttns]: " + str([btn[0].text for row in event.message.buttons for btn in row])

                formatted_message = f"{full_text}{buttons_info}"
                messages.append(formatted_message)
                print(f"Получено сообщение от {bot_username}:")
                print(formatted_message)
                print("-" * 40)

                if "конец" in full_text.lower():
                    stop_processing = True

            except Exception as e:
                print(f"Ошибка обработки, пропускаем...")

        await client.send_message(bot_entity, message_text)
        start_time = asyncio.get_event_loop().time()
        while (asyncio.get_event_loop().time() - start_time) < timeout and not stop_processing:
            await asyncio.sleep(0.5)

    except Exception as e:
        print(f"Незначительная ошибка, пропускаем...")
        return []
    finally:
        if client.is_connected():
            await client.disconnect()
        return messages


async def run_bot_flow(api_id, api_hash, message_text):
    bots = [
        '@telesint',
        '@Telelog_probiv_bot',
        '@infoswagga_bot',
        '@sherlockholmsdoxy_bot'
    ]

    results = {}

    for i, bot_username in enumerate(bots):
        try:
            print(f"\nОтправка запроса...")
            bot_messages = await get_all_bot_messages(
                api_id, api_hash,
                bot_username,
                message_text,
                session_name=f'session_{i}'
            )
            results[bot_username] = bot_messages
            print(f"Результаты:")
            for msg in bot_messages:
                print(f"- {msg}")

            if i < len(bots) - 1:
                await asyncio.sleep(5)

        except Exception as e:
            print(f"Незначительная ошибка, пропускаем...")
            results[bot_username] = None

    return results



