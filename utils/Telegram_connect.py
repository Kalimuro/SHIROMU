from telethon import TelegramClient, events
import asyncio


async def get_all_bot_messages(api_id, api_hash, bot_username, message_text, timeout=10):

    client = TelegramClient('tg1', api_id, api_hash)
    messages = []
    stop_processing = False

    try:
        await client.connect()
        if not await client.is_user_authorized():
            await client.start()

        try:
            bot_entity = await client.get_entity(bot_username)
        except ValueError:
            print(f"Ошибка, пишите Широ'.")
            return []

        @client.on(events.NewMessage(from_users=bot_entity))
        async def handler(event):
            nonlocal messages, stop_processing
            messages.append(event.message.message)
            print(f"Дополнительная информация из Vector: {event.message.message}")
            if "конец" in event.message.message.lower():
                stop_processing = True
                await client.disconnect()

        try:
            await client.send_message(bot_entity, message_text)
        except Exception:
            print(f"Ошибка, пишите Широ")
            return []

        start_time = asyncio.get_event_loop().time()
        while (asyncio.get_event_loop().time() - start_time) < timeout and not stop_processing:
            await asyncio.sleep(1)

    except Exception:
        print(f"Ошибка, пишите Широ")
        return []

    finally:
        if client.is_connected():
            await client.disconnect()

        return messages


async def run_bot_flow(api_id, api_hash, message_text):

    bot_username = '@infoswagga_bot'
    bot_messages = await get_all_bot_messages(api_id, api_hash, bot_username, message_text)
    if bot_messages:
        print("\nДоп.нформация:")
        for msg in bot_messages:
            print(f"- {msg}")
    else:
        print("Ошибка, пишите Широ")
