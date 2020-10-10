""" Plugin for reading nd Exporting as messge on Tg
{i}reveal <reply to file>
"""
#Made By @ItzSjDude. All rights reserved

import os
@ItzSjDude(pattern=r"reveal")
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    a = open(b, 'r')
    c = a.read()
    a.close()
    a = await event.edit("**Reading file...**")
    if len(c) > 4095:
    	await a.edit('`The Total words in this file is more than telegram limits.`')
    else:
    	await event.client.send_message(event.chat_id, f"```{c}```")
    	await a.delete()
    os.remove(b)
    await event.delete()