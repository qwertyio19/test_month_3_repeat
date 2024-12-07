from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboard = ReplyKeyboardMarkup(
    keyboard = [
       [KeyboardButton(text = "Игра"), KeyboardButton(text = "Наши новости")]
    ], resize_keyboard=True, one_time_keyboard=True
)


game_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "Камень"), KeyboardButton(text = "Ножницы"), KeyboardButton(text = "Бумага")],
        [KeyboardButton(text = "Рандомайзер")]
    ], resize_keyboard=True
)


news_keyboards = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text = "О нас"), KeyboardButton(text = "Адресс"), KeyboardButton(text = "Наши курсы")]
    ], resize_keyboard=True
)