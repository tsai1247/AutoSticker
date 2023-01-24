import asyncio
from typing import List, Tuple
from telethon import TelegramClient, events
from dotenv import load_dotenv
from os import getenv
entity_cache = {}

load_dotenv()
session_name = getenv('session_name')
api_id = int(getenv('api_id'))
api_hash = getenv('api_hash')
sticker_set = getenv('sticker_set')

new_images: list = []
emoji = '❤️'

async def sendmsg(client: TelegramClient, event: Tuple[events.NewMessage.Event, str], content: str):
    print(f'send message to @{event}: {content}')
    if event in entity_cache.keys():
        entity = entity_cache[event]
    else:
        if type(event) is str:
            entity = await client.get_entity(event)
        else:
            entity = await client.get_entity(event.chat_id)
        entity_cache[event] = entity

    await client.send_message(entity, content)

async def sendfile(client: TelegramClient, event: Tuple[events.NewMessage.Event, str], path: str):
    print(f'send file to @{event}: {path}')
    if event in entity_cache.keys():
        entity = entity_cache[event]
    else:
        if type(event) is str:
            entity = await client.get_entity(event)
        else:
            entity = await client.get_entity(event.chat_id)
        entity_cache[event] = entity
    
    await client.send_file(entity, path, force_document=True)


def AddSticker(imageList: List[str], wait = 1):
    # create telethon client
    client = TelegramClient(session_name, api_id, api_hash)
    client.start()
    
    async def start():
        cur_index = 0
        await sendmsg(client, 'Stickers', '/addsticker')
        await asyncio.sleep(wait)
        await sendmsg(client, 'Stickers', sticker_set)

        while cur_index < len(imageList):
            await sendfile(client, 'Stickers', imageList[cur_index])
            await asyncio.sleep(wait)
            await sendmsg(client, 'Stickers', emoji)
            cur_index += 1

        await asyncio.sleep(wait)
        await sendmsg(client, 'Stickers', '/done')
        print('Done')
        client.disconnect()

    client.loop.run_until_complete(start())


