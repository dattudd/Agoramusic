from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐀dd me baby,"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["𝐀ԃ𝐃 𝐌ҽ 𝐌σ𝐈 𝐋ꪮꪜ𝐄"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["𝐇ҽʅ𝐏"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_[𝐎ɯɳҽ𝐑], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["𝐆ɾσυ𝐏"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["channel"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_7"],url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons
