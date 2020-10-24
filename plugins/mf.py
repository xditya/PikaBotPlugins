import sys
import time
import os
"""Available Commands:
.mf"""

from telethon import events, functions, __version__

import asyncio

from pikabot.utils import ItzSjDude

@ItzSjDude(outgoing=True, pattern="(.*)")

async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0,27)
    input_str = event.pattern_match.group(1)
    if input_str == "mf":
        await event.edit(input_str)
        animation_chars = [
            "\n......................................../´¯/)\n......................................,/¯../ \n...................................../..../ \n..................................../´.¯/\n..................................../´¯/\n..................................,/¯../ \n................................../..../ \n................................./´¯./\n................................/´¯./\n..............................,/¯../\n............................./..../ \n............................/´¯/\n........................../´¯./\n........................,/¯../ \n......................./..../ \n....................../´¯/\n....................,/¯../ \n.................../..../ \n............./´¯/'...'/´¯¯`·¸ \n........../'/.../..../......./¨¯\ \n........('(...´...´.... ¯~/'...') \n.........\.................'...../ \n..........''...\.......... _.·´ \n............\..............( \n..............\.............\..."
        ]

        for i in animation_ttl:
          
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i %27 ])

@ItzSjDude(pattern="dc")  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await event.client(functions.help.GetNearestDcRequest())  # pylint:disable=E0602
    await event.edit(result.stringify())


@ItzSjDude(pattern="config")  # pylint:disable=E0602
async def _(event):
    if event.fwd_from:
        return
    result = await event.client(functions.help.GetConfigRequest())  # pylint:disable=E0602
    result = result.stringify()
    logger.info(result)  # pylint:disable=E0602
    await event.edit("""**Telethon UserBot powered by [[ItzSjDude](t.me/ItzSjDude)]""")
