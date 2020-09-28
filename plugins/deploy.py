"""Emoji

Available Commands:

.deploy"""

from telethon import events

import asyncio

from uniborg.util import ItzSjDude

from userbot import AUTONAME


DEFAULTUSER = str(AUTONAME) if AUTONAME else "PikaBot"

@ItzSjDude(outgoing=True, pattern=r"deploy")

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 10

    animation_ttl = range(0, 12)

   # input_str = event.pattern_match.group(1)



    await event.edit("Deploying...")

    animation_chars = [
        
            "**Heroku Connecting To Latest Github Build (ItzSjDude/PikachuUserbot)**",
            "**Build started by user** **{DEFAULTUSER}**",
            "**Deploy** `562a91f0` **by user** **{DEFAULTUSER}**",
            "**Restarting Heroku Server...**",
            "**State changed from up to starting**",    
            "**Stopping all processes with SIGTERM**",
            "**Process exited with** `status 143`",
            "**Starting process with command** `python3 -m Pikabot`",
            "**State changed from starting to up**",
            "__INFO:Pikabot:Logged in as 779890498__",
            "__INFO:PikaBot:Successfully loaded all plugins__",
            "**Build Succeeded**"

 ]

    for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 12])
