from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from app.keyboards import start_keyboard, game_keyboards, news_keyboards
import random


router = Router()


@router.message(CommandStart())
async def start(message: Message):
    await message.answer("Выберите один вариант", reply_markup=start_keyboard)


@router.message(F.text == "Игра")
async def game(message: Message):
    await message.answer("Выберите", reply_markup=game_keyboards)


@router.message(F.text.in_({"Камень", "Ножницы", "Бумага"}))
async def game_start(message: Message):
    if message.text == "Камень":
        await message.answer("Вы проиграли!")
    elif message.text == "Ножницы":
        await message.answer("Вы выиграли!")
    elif message.text == "Бумага":
        await message.answer("Ничья!")
    else:
        await message.answer("Выберите кнопку.")


@router.message(F.text == "Рандомайзер")
async def random_(message: Message):
    lucky_number = random.choice(["Вы победили", "Вы проиграли", "Ничья"])
    await message.answer(f"{lucky_number}")


@router.message(F.text == "Наши новости")
async def news(message: Message):
    await message.answer("Выберите кнопку", reply_markup=news_keyboards)


@router.message(lambda message: message.text in {"О нас", "Адресс", "Наши курсы"})
async def news_(message: Message):
    if message.text == "О нас":
        await message.answer("Наша компания учит программистов")
    elif message.text == "Адресс":
        await message.answer("Наш адресс Томирис")
    elif message.text == "Наши курсы":
        await message.answer("Наши курсы предлагают\nBackend\nFrontend\nDesigner.")