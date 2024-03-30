import asyncio
from platform import python_version as pyver

from pyrogram import __version__ as pver
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from SAVVY.PICS import SAVVY_PIC as PICS
from SavvyMusic import SUPPORT_CHAT, app, OWNER_ID
import config

PHOTO = [
    "https://telegra.ph/file/d2a23fbe48129a7957887.jpg",
    "https://telegra.ph/file/ddf30888de58d77911ee1.jpg",
    "https://telegra.ph/file/268d66cad42dc92ec65ca.jpg",
    "https://telegra.ph/file/13a0cbbff8f429e2c59ee.jpg",
    "https://telegra.ph/file/bdfd86195221e979e6b20.jpg",
]

divu = [
    [
        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=OWNER_ID),
        InlineKeyboardButton(text="ꜱᴜᴘᴘᴏʀᴛ", url=f"https://t.me/{config.SUPPORT_CHAT}"),
    ],
    [
        InlineKeyboardButton(
            text="๏ 𝐀ᴅᴅ 𝐌ᴇ ๏",
            url=f"https://t.me/{app.username}?startgroup=true",
        ),
    ],
]



@app.on_message(filters.command("alive"))
async def restart(client, m: Message):
    await m.delete()
    accha = await m.reply("⚡")
    await asyncio.sleep(0.2)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ......")
    await asyncio.sleep(0.1)
    await accha.edit("ᴅɪɴɢ ᴅᴏɴɢ ꨄ︎ ᴀʟɪᴠɪɴɢ..")

    await accha.delete()
    await asyncio.sleep(0.3)
    umm = await m.reply_sticker(
        "CAACAgUAAxkDAAJHbmLuy2NEfrfh6lZSohacEGrVjd5wAAIOBAACl42QVKnra4sdzC_uKQQ"
    )
    await umm.delete()
    await asyncio.sleep(0.2)
    await m.reply_photo(
        random.choice(PICS),
        caption=f"""**ʜᴇʏ, ɪ ᴀᴍ 『[{config.MUSIC_BOT_NAME}](f"t.me/{app.username}")』**
   ━━━━━━━━━❀❀❀━━━━━━━━━━
  ⌬ **ᴍʏ ᴏᴡɴᴇʀ :** [𝕯𝖎𝖛𝖞𝖆𝖓𝖘𝖍𝖚](tg://user?id={OWNER_ID})
  
  ⌬ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pver}`
  
  ⌬ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{pyver()}`
   
  ⌬ **BOT VERSION:** `2.0`
    
  ⌬ **sᴜᴘᴘʀᴏᴛ ɢʀᴏᴜᴘ:** [sᴜᴘᴘᴏʀᴛ](https://t.me/savvy_robot_support)
   ━━━━━━━━━❀❀❀━━━━━━━━━━""",
        reply_markup=InlineKeyboardMarkup(divu),
    )
