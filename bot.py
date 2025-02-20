import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

TOKEN = "8195956492:AAHYjupt0B6FnWfs-nMe5yuuzNle7ppiioU"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Створення кнопок
keyboard = InlineKeyboardMarkup(row_width=1)
buttons = [
    InlineKeyboardButton("Проблеми з бонусами", callback_data="bonus_issues"),
    InlineKeyboardButton("Проблеми зі зняттям коштів", callback_data="withdraw_issues"),
    InlineKeyboardButton("Проблеми з депозитом", callback_data="deposit_issues"),
    InlineKeyboardButton("Зв'язок з оператором", callback_data="contact_operator")
]
keyboard.add(*buttons)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Оберіть проблему:", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data in ["bonus_issues", "withdraw_issues", "deposit_issues", "contact_operator"])
async def handle_buttons(callback_query: types.CallbackQuery):
    responses = {
        "bonus_issues": "Якщо у вас проблеми з бонусами, перевірте умови акції та зверніться до підтримки.",
        "withdraw_issues": "Проблеми зі зняттям коштів можуть бути пов'язані з лімітами або верифікацією. Перевірте умови.",
        "deposit_issues": "Якщо депозит не зарахувався, переконайтеся, що платіж успішно проведено у вашому банку.",
        "contact_operator": "Зв'язатися з оператором можна через онлайн-чат або за телефоном підтримки."
    }
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, responses[callback_query.data])

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
