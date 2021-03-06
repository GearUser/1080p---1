#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *
from .funcn import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    ed = dt.now()
    v = ts(int((ed - uptime).seconds) * 1000)
    ms = (ed - stt).microseconds / 1000
    p = f"ðPÉªÉ´É¢ = {ms}ms"
    await event.reply(v + "\n" + p)


async def start(event):
    await event.reply(
        f"âð `{event.sender.first_name}`, \nDEPLOYED ON VPS FOR [ANIMEXT]( https://t.me/joinchat/RSJAb24o_OoFJu83 ).",
        buttons=[
            [Button.inline("âððð¡", data="ihelp")],
            [
                Button.url("ð¥ððµð®ð»ð»ð²ð¹", url=" https://t.me/joinchat/RSJAb24o_OoFJu83 "),
                Button.url("ðð¢ðªð¡ðð¥", url="https://t.me/sidd_2005"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**ENCODER**\n\n+PRIVATE"
    )


async def ihelp(event):
    await event.edit(
        "**ENCODER**\n\n+PRIVATE",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"`{event.sender.first_name}`, \nWORKING",
        buttons=[
            [Button.inline("âððð¡", data="ihelp")],
            [
                Button.url("ðððð¡ð¡ðð", url=" https://t.me/joinchat/RSJAb24o_OoFJu83 "),
                Button.url("ð¨âð»ððð©ððð¢ð£ðð¥", url="https://t.me/sidd_2005"),
            ],
        ],
    )
