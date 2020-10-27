"""Alive Plugin for Pikabot
{i}alive
"""
#Made by @ItzSjDude. All Rights Reserved

import asyncio
from telethon import events
from pikabot import *
from pikabot.main_plugs.plug import *
from pikabot.utils import *
from pikabot.utils import get_readable_time as grt

@ItzSjDude(outgoing=True,pattern=r"alive$")
async def _(event):
     pupt=grt((time.time() - UpTime))
     pix=pikaa(event, "ALIVE_PIC")
     if pix is not None:
        pic=pix
     else:
        pic=apic
     az=pikaa(event, "ALIVE_NAME")
     await event.delete() 
     a=await event.client.send_file(event.chat_id, pic,caption=alivestr.format(pupt,az))
     await asyncio.sleep(15)
     await a.delete()
