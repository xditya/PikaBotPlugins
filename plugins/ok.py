"""Emoji

Available Commands:

.ok"""

from telethon import events

import asyncio

from pikabot.utils import ItzSjDude

@ItzSjDude(outgoing=True, pattern="ok")
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 0.1
    animation_ttl = range(0,36)
    await event.edit("ok")
    animation_chars = [
            "OK",
            "BOSS",
            "OK MAN",
            "OK BITCH",
            "OK FUKCER",
            "OK SEXY BABE",
            "OK GAY",
            "OK SIR",
            "GO AND SAY OK",
            "OK LOL",
            "YAA OK",
            "FCUK",
            "OK",
            "Boss",
            "Yeahhhhhh",
            "O",
            "K",
            "Ok Boss! 😇"
        ]

    for i in animation_ttl:
        	
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])
