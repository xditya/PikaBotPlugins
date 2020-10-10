"""Transforms Msg into file
{i}pack <reply to msg filename.extension>

"""
#Made by @ItzSjDude. All Rights reserved

import os, asyncio
@ItzSjDude(pattern="pack ?(.*)")
async def _(event):
    a = await event.get_reply_message()
    input_str = event.pattern_match.group(1)
    b = open(input_str, 'w')
    b.write(str(a.message))
    b.close()
    await event.edit(f"**Packing into** `{input_str}`")
    await asyncio.sleep(2)
    await event.edit(f"**Uploading** `{input_str}`")
    await asyncio.sleep(2)
    await event.client.send_file(a.chat_id, caption="Here is your {}".format(input_str)
    os.remove(input_str)
