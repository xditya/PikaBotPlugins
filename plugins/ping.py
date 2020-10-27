"""Ping Module for Pikabot
{i}pika""" 

#Made by @ItzSjDude for Pikabot 

from telethon import events
from datetime import datetime
from pikabot.utils import ItzSjDude

@ItzSjDude(outgoing=True, pattern="pika")
async def _(event):
    if event.fwd_from:
        return
    az=pikaa(event, "ALIVE_NAME")
    start = datetime.now()
    await event.edit("Pong!")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit("✪  𝗣𝗂𝗄𝖺 𝗣𝗂𝗄𝖺 𝗣𝗂𝗄𝖺𝖼𝗁𝗎 !\n➥ {} Ms\n➥ 𝑴𝒚 𝑩𝒐𝒔𝒔 **{}**".format(ms,az))
    await asyncio.sleep(7)
    await event.delete()
