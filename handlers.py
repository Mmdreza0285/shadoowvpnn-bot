from aiogram import types, Dispatcher
from keyboards import menu_fa, menu_en

async def start(message: types.Message):
    await message.answer("زبان خود را انتخاب کنید:", reply_markup=menu_fa)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])