from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu_fa = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("🎛 دریافت سرور رایگان"),
    KeyboardButton("💠 دریافت لینک رفرال"),
    KeyboardButton("📤 اهدا سرور"),
    KeyboardButton("📩 تماس با پشتیبانی")
)

menu_en = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("🎛 Get Free Server"),
    KeyboardButton("💠 Get Referral Link"),
    KeyboardButton("📤 Donate Server"),
    KeyboardButton("📩 Contact Support")
)