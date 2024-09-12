import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO)
bot = Bot(token="123455:asdajhsfbihbwoefn")
dp = Dispatcher()

id1 = "enter id1 as int"
id2 = "enter id2 as int"


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    print(message.from_user.username)
    await message.answer("бот активирован для вас")


@dp.message()
async def cmd_start(message: types.Message):
    await message.answer("принято")
    print(1)
    print(
        f"!!!{message.from_user.username, message.from_user.first_name, message.from_user.id}\n{message.text}"
    )
    await bot.send_message(
        int(id1),
        f"{message.from_user.username, message.from_user.first_name}\n{message.text}",
    )
    await bot.send_message(
        int(id2),
        f"{message.from_user.username, message.from_user.first_name}\n{message.text}",
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
