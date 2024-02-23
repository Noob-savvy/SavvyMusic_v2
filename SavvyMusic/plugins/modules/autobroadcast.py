import asyncio
import random
import datetime
from SavvyMusic import app
from SAVVY.PICS import SAVVY_PIC
from pyrogram import Client
from SavvyMusic.utils.database import get_served_chats
from config import AUTO_GCAST
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

AUTO_GCASTS = "{AUTO_GCAST}" if AUTO_GCAST else False


MESSAGE = f"""**๏ ᴛʜɪs ɪs ᴀᴅᴠᴀɴᴄᴇᴅ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs + ᴄʜᴀɴɴᴇʟs ᴠᴄ. 💌

 ᴘʟᴀʏ + ᴠᴘʟᴀʏ + ᴄᴘʟᴀʏ 

➥ sᴜᴘᴘᴏʀᴛᴇᴅ ᴡᴇʟᴄᴏᴍᴇ - ʟᴇғᴛ ɴᴏᴛɪᴄᴇ, ʙᴀɴ - ᴍᴜᴛᴇ, ʟʏʀɪᴄs, sᴏɴɢ - ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅ, sᴜʙsᴄʀɪᴘᴛɪᴏɴ ғᴏʀ ᴘʀᴏᴍᴏᴛɪᴏɴ, ᴇᴛᴄ... ❤️

➥ ᴄᴏɴᴛᴀᴄᴛ sᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ ғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ

🔐ᴜꜱᴇ » [/start](https://t.me/{app.username}?start=help) ᴛᴏ ᴄʜᴇᴄᴋ ʙᴏᴛ

➲ ʙᴏᴛ :** @{app.username}"""

BUTTON = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("๏ 𝐀ᴅᴅ 𝐌ᴇ ๏", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
        [
             InlineKeyboardButton("๏ 𝐒ᴜᴘᴘᴏʀᴛ ๏", url=f"https://t.me/savvy_robot_support")
        
        ]
    
      ] 
    
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(chat_id, random.choice(SAVVY_PIC), caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(5)  # Sleep for 5 second between sending messages
                except Exception as e:
                    pass  # Do nothing if an error occurs while sending message
    except Exception as e:
        pass  # Do nothing if an error occurs while fetching served chats

async def continuous_broadcast():
    while True:
        await send_message_to_chats()

        # Wait for 50000 seconds before next broadcast
        await asyncio.sleep(50000)

# Start the continuous broadcast loop if AUTO_BROADCAST is True
if AUTO_GCASTS:  
    asyncio.create_task(continuous_broadcast())

