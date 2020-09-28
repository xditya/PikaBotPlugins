from telethon import events
import subprocess
import asyncio
import time
from pikabot.utils import ItzSjDude

@ItzSjDude(outgoing=True, pattern=r"cmds")
async def install(event):
    if event.fwd_from:
        return
    cmd = "ls ./plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"**Plugins In PikaBot:**\n{o}\n\n**HELP:** __If you want to know the commands for a plugin, do:-__ \n `.help <plugin name>` **without the < > brackets.**\n__All plugins might not work directly. Visit [Here](t.me/ItzSjDudeSupport) for assistance.__"
    await event.edit(OUTPUT)
