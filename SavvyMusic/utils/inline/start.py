


from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP, OWNER_ID
from SavvyMusic import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(text=_["S_B_2"], callback_data="settings_helper"),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
                InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}"),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")]
            )
        if SUPPORT_GROUP:
            buttons.append(
                [InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")]
            )
    return buttons


from typing import Union
from pyrogram.types import InlineKeyboardButton

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [InlineKeyboardButton(text=_["S_B_8"], callback_data="settings_back_helper")]
    ]
    
    # Check if SUPPORT_CHANNEL and SUPPORT_GROUP are accessible
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append([
            InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"),
            InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")
        ])
    else:
        # Add SUPPORT_CHANNEL button if accessible
        if SUPPORT_CHANNEL:
            buttons.append([InlineKeyboardButton(text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}")])
        
        # Add SUPPORT_GROUP button if accessible
        if SUPPORT_GROUP:
            buttons.append([InlineKeyboardButton(text=_["S_B_3"], url=f"{SUPPORT_GROUP}")])
    
    # Add start group button
    buttons.append([
        InlineKeyboardButton(
            text=_["S_B_5"],
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
        )
    ])
    
    # Check if GITHUB_REPO and OWNER are accessible
    if GITHUB_REPO and OWNER:
        # Check if user privacy allows creating buttons with user_id
        if OWNER_ID and isinstance(OWNER, int):
            buttons.append([
                InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER),
                InlineKeyboardButton(text=_["S_B_6"], url=f"{GITHUB_REPO}")
            ])
        else:
            buttons.append([InlineKeyboardButton(text=_["S_B_6"], url=f"{GITHUB_REPO}")])
    else:
        # Check if user privacy allows creating buttons with user_id
        if OWNER_ID and isinstance(OWNER, int):
            buttons.append([InlineKeyboardButton(text=_["S_B_7"], user_id=OWNER)])
    
    # Add language button
    buttons.append([InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG")])
    
    return buttons
