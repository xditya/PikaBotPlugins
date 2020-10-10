# Copyright (C) 2020 BY - GitHub.com/code-rgb [TG - @deleteduser420]
# All rights reserved.

"""Detects Nsfw content with the help of A.I.
{i}nsfw <reply to image>"""

import os, requests

@ItzSjDude(pattern=r"nsfw")
async def detect_(event):
    """detect nsfw"""
    reply = await event.client.download_media(await event.get_reply_message(), )
    if not reply:
        await event.reply("reply to media !")
        await event.delete()
        return
    if Var.DEEPAI_KEY is None:
        await event.reply("add VAR `DEEP_AI` get Api Key from https://deepai.org/")
        await event.delete()
        return
    api_key = Var.DEEPAI_KEY
    photo = reply
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            'image': open(photo, 'rb'),
        },
        headers={'api-key': api_key}
    )
    os.remove(photo)
    if 'status' in r.json():
        await event.reply(r.json()['status'])
        return
    r_json = r.json()['output']
    pic_id = r.json()['id']
    percentage = r_json['nsfw_score'] * 100
    detections = r_json['detections']
    result = "**Detected Nudity** :\n[>>>](https://api.deepai.org/job-view-file/{}/inputs/image.jpg) `{:.3f} %`\n\n".format(pic_id, percentage)

    if detections:
        for parts in detections:
            name = parts['name']
            confidence = int(float(parts['confidence']) * 100)
            result += f"• {name}:\n   `{confidence} %`\n"
    await event.client.send_message(event.chat_id, result, link_preview=False, reply_to=event.message.reply_to_msg_id)
    await event.delete()
    
