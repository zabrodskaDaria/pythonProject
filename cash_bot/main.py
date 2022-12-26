import config
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType

# log
logging.basicConfig(level=logging.INFO)

#init
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

#prices
PRICE = types.LabeledPrice(label="Подписка на один месяц", amount=5*100)

#buy
@dp.message_handler(commands=['buy'])
async def buy(message: types.Message):
    if config.PAYMENS_TOKEN.split(':')[1] == 'TEST':
        await bot.send_message(message.chat.id, "Тестовый платеж!")

    await bot.send_invoice(message.chat.id,title="Подписка на бота",
                           description="Активаия подписки на бота на один месяц")

#echo
@dp.message_handler()
async def echo(message: types.Massage):
    await message.answer(message.text)

#run long-polling
if __name__=="__main__":
    executor.start_polling(dp, skip_updates=False)