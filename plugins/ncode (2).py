import pygments, os, asyncio
from pygments.lexers import Python3Lexer
from pygments.formatters import ImageFormatter

@ItzSjDude(pattern=r"ncode")
async def coder_print(event):
	a = await event.client.download_media(await event.get_reply_message(), Var.TEMP_DOWNLOAD_DIRECTORY)
	s = open(a, 'r')
	c = s.read()
	s.close()
	pygments.highlight(f"{c}", Python3Lexer(), ImageFormatter(font_name="DejaVu Sans Mono", line_numbers=True), "out.png")
	await event.client.send_file(event.chat_id, "out.png", force_document=True)
	await event.client.send_file(event.chat_id, "out.png", force_document=False)
	await event.delete()
	os.remove(a)
	os.remove('out.png')