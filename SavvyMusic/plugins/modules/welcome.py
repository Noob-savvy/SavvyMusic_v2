from SavvyMusic import app
from pyrogram import filters
from pyrogram.errors import RPCError
from pyrogram.types import ChatMemberUpdated, InlineKeyboardMarkup, InlineKeyboardButton
from os import environ
from typing import Union, Optional
from PIL import Image, ImageDraw, ImageFont
from os import environ
import random
from pyrogram import Client, filters
from pyrogram.types import ChatJoinRequest, InlineKeyboardButton, InlineKeyboardMarkup
from PIL import Image, ImageDraw, ImageFont
import asyncio, os, time, aiohttp
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from asyncio import sleep
from pyrogram import filters, Client, enums
from pyrogram.enums import ParseMode
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from SavvyMusic.utils.Savvy_ban import admin_filter


random_photo = [
    "https://telegra.ph/file/3a35b86005e7b3c2d9310.jpg",
    "https://telegra.ph/file/2e7b72279b28105607667.jpg",
    "https://telegra.ph/file/87bae0c629ae73032ae77.jpg",
    "https://telegra.ph/file/f85e89871eb80c91f8a87.jpg",
    "https://telegra.ph/file/70c87e971a919a48e3e2b.jpg",
]
# --------------------------------------------------------------------------------- #

get_font = lambda font_size, font_path: ImageFont.truetype(font_path, font_size)
resize_text = (
    lambda text_size, text: (text[:text_size] + "...").upper()
    if len(text) > text_size
    else text.upper()
)

# --------------------------------------------------------------------------------- #

async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(46, font_path),
        fill=(255, 255, 255),
    )

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path

# --------------------------------------------------------------------------------- #

bg_path = "assets/userinfo.png"
font_path = "assets/font.ttf"

# --------------------------------------------------------------------------------- #

# Function to handle new members
async def handle_member_update(client: app, member: ChatMemberUpdated):
    chat = member.chat
    
    count = await app.get_chat_members_count(chat.id)
   
    if member.new_chat_member:
        user = member.new_chat_member.user
        try:
            if user.photo:
                # User has a profile photo
                photo = await app.download_media(user.photo.big_file_id)
                welcome_photo = await get_userinfo_img(
                    bg_path=bg_path,
                    font_path=font_path,
                    user_id=user.id,
                    profile_path=photo,
                )
            else:
                # User doesn't have a profile photo, use random_photo directly
                welcome_photo = random.choice(random_photo)

            # Welcome message for new members
            caption = (
            f"**𝐖ᴇʟᴄᴏᴍᴇ 𝐓ᴏ {member.chat.title}**\n"
            f"**𝐍ᴀᴍᴇ ✧{member.new_chat_member.user.mention}\n"
            f"**🔐𝐋ɪɴᴋ » @{chat.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**๏ 𝐌ᴇᴍʙᴇʀ 𝐈ᴅ »** `{member.new_chat_member.user.id}`\n"
            f"**๏ 𝐔sᴇʀɴᴀᴍᴇ » @{member.new_chat_member.user.username}**\n➖➖➖➖➖➖➖➖➖➖➖\n"
            f"**👥𝐓ᴏᴛᴀʟ 𝐌ᴇᴍʙᴇʀ 𝐍ᴏᴡ » {count}**"
            )
            button_text = "๏ 𝐕ɪᴇᴡ 𝐍ᴇᴡ 𝐌ᴇᴍʙᴇʀ ๏"
            add_button_text = "๏ 𝐀ᴅᴅ 𝐌ᴇ ๏"

            # Generate a deep link to open the user's profile
            deep_link = f"tg://openmessage?user_id={user.id}"
            add_link = f"https://t.me/{app.username}?startgroup=true"

            # Send the message with the photo, caption, and button
            await client.send_photo(
                chat_id=member.chat.id,
                photo=welcome_photo,
                caption=caption,
                reply_markup=InlineKeyboardMarkup([
                    [InlineKeyboardButton(button_text, url=deep_link)],
                    [InlineKeyboardButton(text=add_button_text, url=add_link)],
                ])
            )
        except RPCError as e:
            print(e)

# Connect the function to the ChatMemberUpdated event
@app.on_chat_member_updated(filters.group, group=10)
async def member_update_handler(client: app, member: ChatMemberUpdated):
    await handle_member_update(client, member)
