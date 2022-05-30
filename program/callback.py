
from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    BOT_PHOTO,
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" **مرحبآ عزيزي ↤「 [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) 」**\n
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
**⌯ انا بوت {BOT_NAME} استطيع تشغيل الموسيقي والفيديو في محادثتك الصوتية**

**⌯ لتعلم طريقة تشغيلي بمجموعتك اضغط علي » طريقة التفعيل !

**⌯ لمعرفة الاوامر اضغط علي  » الاوامر !
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰ .
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𓄹𝙳𝙴𝚅 𝚅𝙾𝚃𝙻𝚇𓄹", url=f"https://t.me/votlx"),
                    InlineKeyboardButton("𓄼𝙳𝙴𝚅 𝙷𝙰𝚂𝚂𝙰𝙽𓄹", url=f"https://t.me/D_bb_D"),
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
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f""" طريقة تفعيل البوت:-
 ⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
 1 ↤ ضيف البوت إلى مجموعتك
 2 ↤ ارفع بوت ادمن 
 3 ↤ بعد كدا اكتب `تحديث` او `/reload` لتحديث بيانات المشرفين
 3 ↤ بعد كدا اكتب  `انضم`  او `/userbotjoin` لدعوة حساب المساعد او ضيف حساب ده `@{ASSISTANT_NAME}`إلى مجموعتك 
 4 ↤ قبل استخدام امر تشغيل تاكد من الكول مفتوح
 5 ↤ لو كانت فيه مشكلة ف تشغيل اكتب `غادر`   من ثم  اكتب `انضم`    

 ⌯ لو عندك اي سوال او استفسار كلمنا ↤ @D_bb_D او @votlx
 ⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ قناة سورس دايموند ميوزك 🎵  @t_8_t_t
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**⇦ قم بالضغط علي الزر الذي تريده لمعرفه الاوامر  !**

⌯ __قناة سورس دايموند ميوزك 🎵  @t_8_t_t  __""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("𓄼اوامــر تشغيل𓄹", callback_data="cbadmin"),
                    InlineKeyboardButton("𓄼اوامــر انجليزي𓄹", callback_data="cbvamp"),
                ],[
                    InlineKeyboardButton("𓄼اوامــر تحميل والمطور𓄹", callback_data="cbsudo"),
                ],
                [
                    InlineKeyboardButton("🔙 رجوع", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ | لتحميل اغاني أرسل ↞ ⊰ `تحميل + اسم اغنية` ⊱
⌯ | لتحميل فيديوهات ↞ ⊰ `تحميل_فيديو + اسم فيديو` ⊱
⌯ | لبحث عنه باليوتيوب  ↞ ⊰ `بحث` ⊱
⌯ | لبحث عن  كلمات.  ↞ ⊰ `كلمات` ⊱
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ |  لإظهار حالة البوت بينج  أرسل ↞ ⊰ `بينج` ⊱
⌯ | لاظهار وقت تشغيل البوت أرسل ↞ ⊰ `وقت_تشغيل` ⊱
⌯ | لإظهار معلومات البوت أرسل ↞ ⊰ `السورس ` ⊱
⌯ | لإظهار مطورين البوت أرسل ↞ ⊰ `المطور` ⊱
⌯ | لمسح جميع الملفات المستخدمه أرسل ↞ ⊰ `مسح` ⊱
⌯ | لتنظيف جميع الملفات المحمله أرسل ↞ ⊰ `تنضيف` ⊱
⌯ | لرؤيه معلومات السيرفر  البوت أرسل ↞ ⊰ `السيرفر` ⊱
⌯ | لتحديث البوت لاخر اصدار من السورس أرسل ↞ ⊰ `ترقيه` ⊱
⌯ | لاعادة تشغيل البوت أرسل ↞ ⊰ `ريستارت` ⊱
⌯ | لمغادره الحساب المساعد لجميع جروبات أرسل ↞ ⊰ `غادرالجميع` ⊱
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ قناة سورس دايموند ميوزك 🎵  @t_8_t_t
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""  ⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ | لتشغيل صوتية في المكالمة أرسل ↞ ⊰ `تشغيل +اسم الأغنيةاو رابط` ⊱

⌯ | لتشغيل فيديو في المكالمة  ↞ ⊰ `فيديو +اسم الفديواو رابط` ⊱

⌯ | لتشغيل فيديو مباشر في المكالمة  ↞ ⊰ `فيديو_مباشر+رابط+جودة 360 - 480- 720 ` ⊱

⌯ | لأيقاف الاغنية  ↞ ⊰ `ايقاف`⊱   او   ⊰ `انهاء` ⊱

⌯ | لأيقاف الاغنية او الفيديو مؤقتآ  ↞ ⊰`موقت`⊱ او  ⊰ `وقف` ⊱

⌯ | لمتابعه تشغيل الاغنية ↞  ⊰ `متابعه` ⊱     او    ⊰ `كمل` ⊱

⌯ | لتخطي الاغنية  ↞ ⊰ `سكب`⊱ او ⊰ `تخطي` ⊱

⌯ | لعرض قائمه تشغيل  ↞  ⊰ `قائمه` ⊱

 ⌯ | لكتم البوت ↞  ⊰ `سكوت` ⊱ 

⌯ | الغاء الكتم البوت  ⊰ `الغاء الكتم` ⊱ 
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ قناة سورس دايموند ميوزك 🎵  @t_8_t_t
__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ | لتحميل اغاني أرسل ↞ ⊰ `تحميل + اسم اغنية` ⊱
⌯ | لتحميل فيديوهات ↞ ⊰ `تحميل_فيديو + اسم فيديو` ⊱
⌯ | لبحث عنه باليوتيوب  ↞ ⊰ `بحث` ⊱
⌯ | لبحث عن  كلمات.  ↞ ⊰ `كلمات` ⊱
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ |  لإظهار حالة البوت بينج  أرسل ↞ ⊰ `بينج` ⊱
⌯ | لاظهار وقت تشغيل البوت أرسل ↞ ⊰ `وقت_تشغيل` ⊱
⌯ | لإظهار معلومات البوت أرسل ↞ ⊰ `السورس ` ⊱
⌯ | لإظهار مطورين البوت أرسل ↞ ⊰ `المطور` ⊱
⌯ | لمسح جميع الملفات المستخدمه أرسل ↞ ⊰ `مسح` ⊱
⌯ | لتنظيف جميع الملفات المحمله أرسل ↞ ⊰ `تنضيف` ⊱
⌯ | لرؤيه معلومات السيرفر  البوت أرسل ↞ ⊰ `السيرفر` ⊱
⌯ | لتحديث البوت لاخر اصدار من السورس أرسل ↞ ⊰ `ترقيه` ⊱
⌯ | لاعادة تشغيل البوت أرسل ↞ ⊰ `ريستارت` ⊱
⌯ | لمغادره الحساب المساعد لجميع جروبات أرسل ↞ ⊰ `غادرالجميع` ⊱
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ قناة سورس دايموند ميوزك 🎵  @t_8_t_t
""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbvamp"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
 »⊰`/mplay   + اسم الأغنيةاو رابط`⊱
 »⊰`/vplay + فيديو +اسم الفديواو رابط`⊱  
 »⊰`/stream + صوت مباشر+رابط+جودة 360 - 480- 720`⊱
 »⊰`/vstream  + لتشغيل فيديو مباشر في المكالمة`⊱  
 »⊰`/stop  « لايقاف التشغيل`⊱
 »⊰`/resume « لاستئناف التشغيل`⊱ 
 »⊰`/skip   « تخطي الئ التالي`⊱
 »⊰`/pause « ايقاف التشغيل موقتآ`⊱  
 »⊰`/vmute « لكتم البوت`⊱ 
 »⊰`/vunmute  « لرفع الكتم عن البوت`⊱
 »⊰`/playlist  « تظهر لك قائمة التشغيل`⊱
 »⊰`/video  «  الاسم  تنزيل فيديو من`⊱
 »⊰`/song +  «  الاسم تنزيل صوت من`⊱
 »⊰`/volume  « + الرقم لضبط مستوئ الصوت`⊱
 »⊰`/reload  « لتحديث البوت و قائمة المشرفين`⊱
 »⊰`/userbotjoin  « لاستدعاء حساب المساعد`⊱
 »⊰`/userbotleave «  لطرد حساب المساعد`⊱
 »⊰`/ping « إظهار حالة البوت بينغ`⊱
 »⊰`/alive   إظهار معلومات البوت  (في المجموعه)`⊱
⊱┉┉┉⊶𓄼•ᴍᴜѕɪᴄ ᴅɪᴀᴍᴏɴᴅ •𓄹⊷┉┉┉⊰
⌯ قناة سورس دايموند ميوزك 🎵  @t_8_t_t__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙رجوع", callback_data="cbcmds")]]
        ),
    )
           

@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **الإعدادات** {query.message.chat.title}\n\n⏸ : ايقاف التشغيل موقتآ\n▶️ : استئناف التشغيل\n🔇 : كتم الصوت\n🔊 : الغاء كتم الصوت\n⏹ : ايقاف التشغيل",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("⌯ اغلاق ⌯", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ قائمة التشغيل فارغه", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 المسؤول الوحيد الذي لديه إذن إدارة الدردشات الصوتية يمكنه النقر على هذا الزر !", show_alert=True)
    await query.message.delete()
