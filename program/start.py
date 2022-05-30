import asyncio

from datetime import datetime
from sys import version_info
from time import time

from config import (
    BOT_PHOTO,
    ALIVE_IMG,
    ALIVE_NAME,
    BOT_NAME,
    ASSISTANT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    DEV_NAME,
    UPDATES_CHANNEL,
)
from program import __version__
from driver.amort import user
from driver.filters import command, other_filters
from driver.decorators import sudo_users_only
from driver.database.dbchat import add_served_chat, is_served_chat
from driver.database.dbpunish import is_gbanned_user
from pyrogram import Client, filters, __version__ as pyrover
from pyrogram.errors import FloodWait, MessageNotModified
from pytgcalls import (__version__ as pytover)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ChatJoinRequest

__major__ = 0
__minor__ = 2
__micro__ = 1

__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(
    command(["staart", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_PHOTO}",
        caption=f"""**مرحبآ عزيزي ↤「 {message.from_user.mention()} 」**\n
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
**⌯ انا بوت {BOT_NAME} استطيع تشغيل الموسيقي والفيديو في محادثتك الصوتية**

**⌯ لتعلم طريقة تشغيلي بمجموعتك اضغط علي » طريقة التفعيل !

**⌯ لمعرفة الاوامر اضغط علي  » الاوامر !
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𓄹𝙳𝙴𝚅 𝚅𝙾𝚃𝙻𝚇𓄹", url=f"https://t.me/votlx"),
                    InlineKeyboardButton("𓄼𝙳𝙴𝚅 𝙺𝙸𝙽𝙰𝙽𓄹", url=f"https://t.me/K_in4"),
                ],
                [InlineKeyboardButton("𓄼طريقة التفعيل𓄹", callback_data="cbhowtouse")],
                [InlineKeyboardButton("𓄼الاوامــر𓄹", callback_data="cbcmds"),
                 InlineKeyboardButton("𓄼الــمــطــور𓄹", url=f"https://t.me/{OWNER_NAME}"),
                ],
                [
                    InlineKeyboardButton(
                        "𓄼جروب البوت𓄹", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "𓄼قناة البوت𓄹", url=f"https://t.me/{UPDATES_CHANNEL}"
                    ),
                ],
                [
                    InlineKeyboardButton("اضف البوت  لمجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )


@Client.on_message(
    command(["برمج السورس" ,"طور" ,"لمطور", "ورس", "لسورس", f"alive@{BOT_USERNAME}"]) & filters.group & ~filters.edited
)
async def alive(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))

    keyboard = InlineKeyboardMarkup(
            [
               [
                InlineKeyboardButton("𓄹𝙳𝙴𝚅 𝚅𝙾𝚃𝙻𝚇𓄹", url=f"https://t.me/votlx"),
                InlineKeyboardButton("𓄼𝙳𝙴𝚅 𝙺𝙸𝙽𝙰𝙽𓄹", url=f"https://t.me/K_in4"),
            ],
                [       
                    InlineKeyboardButton(
                        "⌯ 𝐃𝐈𝐀𝐌𝐎𝐍𝐃 𝐌𝐔𝐒𝐈𝐂 🎶 ⌯", url=f"https://t.me/T_8_T_T"
                    ),
                ],
                [
                    InlineKeyboardButton("اضف البوت  لمجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
        ]
    ) 

    alive = f"**⌯ اهلا بك يا  {message.from_user.mention()}   \n ⌯ في سورس دايموند ❤️ \n⌯ مطورين سورس دايموند ⬇️** "

    await message.reply_photo(
        photo=f"{ALIVE_IMG}",
        caption=alive,
        reply_markup=keyboard,
    )


@Client.on_message(command(["بوت", "وت"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_PHOTO}",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("انا موجود عزيزي 🙂❤️", url=f"http://t.me/{BOT_USERNAME}?start"),
            ],
            [
                InlineKeyboardButton(
                        DEV_NAME, url=f"https://t.me/{OWNER_NAME}"
                ),
            ],
            [
                    InlineKeyboardButton("اضف البوت  لمجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(command(["وامراغاني", f"وامر", f"لاوامراغاني", f"لاوا", f"اغاني", f"غاني"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"{BOT_PHOTO}",
        caption=f"""🙂╖ **مرحبآ عزيزي ↤「 {message.from_user.mention()} 」**\n🤖╢ **انا بوت {BOT_NAME}  🎵**\n🎧╜ **لمعرفة اوامر تشغيل اضغط علي  » الاوامر !**""",
        reply_markup=InlineKeyboardMarkup(
         [
            [
                InlineKeyboardButton("𓄹𝙳𝙴𝚅 𝚅𝙾𝚃𝙻𝚇𓄹", url=f"https://t.me/votlx"),
                InlineKeyboardButton("𓄼𝙳𝙴𝚅 𝙺𝙸𝙽𝙰𝙽𓄹", url=f"https://t.me/K_in4"),
            ],
            [InlineKeyboardButton("𓄼الاوامــر𓄹", callback_data="cbcmds"),
                ],
            [
                InlineKeyboardButton(
                    "⌯ 𝐃𝐈𝐀𝐌𝐎𝐍𝐃 𝐌𝐔𝐒𝐈𝐂 🎶 ⌯", url=f"https://t.me/T_8_T_T"
                ),
            ],
            [
                InlineKeyboardButton("اضف البوت  لمجموعتك ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ]
         ]
     )
  )


@Client.on_message(command(["ping", "ينج", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text("⚡ `PING!!`\n" f"⚡️ `{delta_ping * 1000:.3f} ms`")



@Client.on_message(command(["uptime","قت_تشغيل", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )


@Client.on_chat_join_request()
async def approve_join_chat(c: Client, m: ChatJoinRequest):
    if not m.from_user:
        return
    try:
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)
    except FloodWait as e:
        await asyncio.sleep(e.x + 2)
        await c.approve_chat_join_request(m.chat.id, m.from_user.id)


@Client.on_message(filters.new_chat_members)
async def new_chat(c: Client, m: Message):
    chat_id = m.chat.id
    if await is_served_chat(chat_id):
        pass
    else:
        await add_served_chat(chat_id)
    ass_uname = (await user.get_me()).username
    bot_id = (await c.get_me()).id
    for member in m.new_chat_members:
        if member.id == bot_id:
             return await m.reply(
                "**🤖╖• مـرحـبــا أنا بوت ميوزك🎵**\n"
                "**🌐╢• وظيفتي تشغيل وتحميل الاغاني**\n**✅╢• لتفعيل البوت عليك اتباع مايلي .**\n**🔘╢• أضِف البوت إلى مجموعتك .**\n**⚡️╢• ارفعهُ » مشرف + اكتب `انضم`**\n**🎧╢• لأستخدام البوت اغاني وفيديو كول**\n**🎥╜• اكتب » `تشغـيل` +اسم الاغنيه.**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("𓄼الاوامــر𓄹", callback_data="cbcmds"),
                        ],
                        [
                            InlineKeyboardButton(
                        "اضف البوت  لمجموعتك ➕",
                        url=f'https://t.me/{BOT_USERNAME}?startgroup=true'),
                        ],
                    ]
                )
            )


chat_watcher_group = 5
