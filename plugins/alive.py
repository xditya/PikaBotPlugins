"""Alive Plugin for Pikabot
{i}alive
"""
#Made by @ItzSjDude. All Rights Reserved

import asyncio
from telethon import events
from pikabot.main_plugs.plug import *
from userbot.utils import ItzSjDude
from telethon import events


@ItzSjDude(outgoing=True,pattern=r"alive")
async def amireallyalive(event):
     az=pikaa(event, "ALIVE_NAME")
     await event.delete() 
     a=await event.client.send_file(event.chat_id, pic,caption=alivestr.format(az))