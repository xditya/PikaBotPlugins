"""Beautifies nd convert python code into image
{i}ncode <reply to file for normal image>
{i}ncode doc <reply to file for document format> 
"""
#created by @Buddhhu, Rebased by @ItzSjDude. All Rights Reserved 

import pygments, os, asyncio
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter

@ItzSjDude(pattern=r"ncode (.*)")
async def coder_print(event):
    input=event.pattern_match.group(1)
    a=await event.client.download_media(await event.get_reply_message(), Var.TEMP_DOWNLOAD_DIRECTORY)
    s=open(a, 'r')
    c=s.read()
    s.close()
    pygments.highlight(f"{c}", Python3Lexer(), ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True), "out.png")
    if 'doc'in input:
      await event.client.send_file(event.chat_id, "out.png", force_document=True)
      await event.delete()
      os.remove(a)
      os.remove('out.png')
    else:
      await event.client.send_file(event.chat_id, "out.png", force_document=False)
      await event.delete()
      os.remove(a)
      os.remove('out.png')
