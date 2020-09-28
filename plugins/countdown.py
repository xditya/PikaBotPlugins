"""COMMAND : .cd, .scd, .padmin"""

from telethon import events

from datetime import datetime

from uniborg.util import ItzSjDude

import importlib.util

import asyncio

import random





@ItzSjDude(outgoing=True, pattern='(f?c)d ')

async def timer_blankx(e):

 txt=e.text[4:] + '\nDeleting in '

 j=86400

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k-50

  await asyncio.sleep(50)

 if e.pattern_match.group(1) == 'c':

  await e.delete()

 else:

  await e.edit(txt + 'NaN')


@ItzSjDude(outgoing=True, pattern='(f?s)cd ')

async def timer_blankx(e):

 txt=e.text[4:] + '\nDeleting in '

 j=10

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k-1

  await asyncio.sleep(1)

 if e.pattern_match.group(1) == 's':

  await e.delete()

 else:

  await e.edit(txt + 'NaN')




@ItzSjDude(outgoing=True, pattern="(f?p)an")

async def timer_blankx(e):

 txt=e.text[7:] + '\n\n`Promoting You As Admin In` '

 j=5

 k=j

 for j in range(j):

  await e.edit(txt + str(k))

  k=k-1

  await asyncio.sleep(1)

 if e.pattern_match.group(1) == 'f':

  await e.edit("`Successfully Promoted As Admin.` ")

