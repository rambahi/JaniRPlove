from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from PROMUSIC import app
from PROMUSIC.utils.database import add_served_chat, delete_served_chat
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from PROMUSIC.utils.database import get_assistant
import asyncio
from PROMUSIC.misc import SUDOERS
from PROMUSIC.core.userbot import Userbot
from pyrogram import Client, filters
from pyrogram.errors import UserAlreadyParticipant
from PROMUSIC import app
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)
from PROMUSIC import app
from PROMUSIC.utils.database import get_assistant, is_active_chat


@app.on_message(filters.command("clone"))
async def clones(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://i.ibb.co/k3cw8XS/IMG-20250103-174108-968.jpg",
        caption=f"""**♥️You Are Not Sudo User So You Are Not Allowed To Clone Me.**\n**♥️Click Given Below Button And Host Manually Otherwise Contact Owner Or Sudo Users For Clone.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "❮Oᴡɴᴇʀ❯", url=f"https://t.me/Legend_mickey"
                    )
                ]
            ]
        ),
    )


# --------------------------------------------------------------------------------- #
