from aiogram.types import Message

from aiogram.utils import executor


from loader import dp, bot


@dp.message_handler()
async def echo_message(message: Message):
    await message.answer(f"В данный момент идут технические работы. Напишите позже")


if __name__ == '__main__':
    executor.start_polling(dp)
