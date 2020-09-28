# For UniBorg
# By Priyam Kalra
# Syntax (.hl <link>)

from telethon import events
from userbot.utils import *
import asyncio
from telethon.tl import functions, types

@itzzSj(outgoing=True, pattern="^.hl(.*)")
async def _(event):
        if event.fwd_from:
            return
        input = event.pattern_match.group(1)
        await event.edit("[ㅤㅤㅤㅤㅤㅤㅤ](" + input + ")")
