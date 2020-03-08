Port by MvUnknown

import asyncio
from telethon import events
from userbot import bot, CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern=r"^.fap (.*)")
async def fup(event):
    if event.fwd_from:
        return
    animation_interval = 0.3
    animation_ttl = range(0, 100)
    input_str = event.pattern_match.group(1)
    if input_str == "muth":
        await event.edit(input_str)
        animation_chars = [

            "8✊️===D",

            "8=✊️==D",

            "8==✊️=D",

            "8===✊️D",

            "8==✊️=D",

            "8=✊️==D",

            "8✊️===D",

            "8===✊️D💦",

            "8==✊️=D💦💦",

            "8=✊️==D💦💦💦"

        ]

        for i in animation_ttl:
            await asyncio.sleep(animation_interval)
            await event.edit(animation_chars[i % 8])

CMD_HELP.update({
        "muth": 
        ".fap \
          \nUsage: Animation fup a some anu.\n"
    })
