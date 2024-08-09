
import os
import random

import telebot
from PIL import Image
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = '7449140946:AAHZGm7WJXLlJZ18wFpLfIA-3nsK2kFvAMM'
botPredskazatel = telebot.TeleBot(API_TOKEN)

IMAGE_FOLDER = 'images'
# Список картинок и их описаний
images = [
    {"filename": "1.png", "description": ""},
    {"filename": "2.png", "description": ""},
    {"filename": "3.png", "description": ""},
    {"filename": "4.png", "description": ""},
    {"filename": "5.png", "description": ""},
    {"filename": "6.png", "description": ""},
    {"filename": "7.png", "description": ""},
    {"filename": "8.png", "description": ""},
    {"filename": "9.png", "description": ""},
    {"filename": "10.png", "description": ""},
    {"filename": "11.png", "description": ""},
    {"filename": "12.png", "description": ""},
    {"filename": "13.png", "description": ""},
    {"filename": "14.png", "description": ""},
    {"filename": "15.png", "description": ""},
    {"filename": "16.png", "description": ""},
    {"filename": "17.png", "description": ""},
    {"filename": "18.png", "description": ""},
    {"filename": "19.png", "description": ""},
    {"filename": "20.png", "description": ""},
    {"filename": "21.png", "description": ""},
    {"filename": "22.png", "description": ""},
    {"filename": "23.png", "description": ""},
    {"filename": "24.png", "description": ""},
    {"filename": "25.png", "description": ""},
    {"filename": "26.png", "description": ""},
    {"filename": "27.png", "description": ""},
    {"filename": "28.png", "description": ""},
    {"filename": "29.png", "description": ""},
    {"filename": "30.png", "description": ""},
    {"filename": "31.png", "description": ""},
    {"filename": "32.png", "description": ""},
    {"filename": "33.png", "description": ""},
    {"filename": "34.png", "description": ""},
    {"filename": "35.png", "description": ""},
    {"filename": "36.png", "description": ""},
    {"filename": "37.png", "description": ""},
    {"filename": "38.png", "description": ""},
    {"filename": "39.png", "description": ""},
    {"filename": "40.png", "description": ""}
]
# Проверка и корректировка размеров изображения
def check_image_dimensions(image_path):
    with Image.open(image_path) as img:
        width, height = img.size
        if width < 10 or height < 10 or width > 10000 or height > 10000:
            new_width = min(max(width, 10), 10000)
            new_height = min(max(height, 10), 10000)
            img = img.resize((new_width, new_height))
            img.save(image_path)


# Обработчик команды /start
@botPredskazatel.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Да", callback_data="yes"))
    first_mess = f"{message.from_user.first_name} {message.from_user.last_name}, привет! И, добро пожаловать!\n" \
                 f"Ты оказался здесь не случайно, этот бот волшебный и обладает метазнаниями о происходящем\n" \
                 f"Хочешь расскажу немного о том, что ждет тебя сегодня?"
    botPredskazatel.send_message(message.chat.id, first_mess, reply_markup=markup)

# Обработчик нажатий на Inline кнопки
@botPredskazatel.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "yes" or call.data == "more":
        # Выбираем случайную картинку
        image = random.choice(images)
        image_path = os.path.join(IMAGE_FOLDER, image['filename'])
        check_image_dimensions(image_path)

        markup = InlineKeyboardMarkup()
        #markup.add(InlineKeyboardButton("Описание", callback_data=f"description_{image['filename']}"))

        markup.add(InlineKeyboardButton("Хочу еще предсказание", callback_data="more"))
        markup.add(InlineKeyboardButton("Информация о создателе", callback_data="artist"))
        with open(image_path, 'rb') as photo:
            botPredskazatel.send_photo(call.message.chat.id, photo, reply_markup=markup)
    elif call.data.startswith("description_"):
        # Извлекаем URL картинки из callback_data
        filename = call.data.split("_", 1)[1]
        # Находим описание картинки по URL
        description = next((img["description"] for img in images if img["filename"] == filename), "Описание не найдено")
        botPredskazatel.send_message(call.message.chat.id, description)
    if call.data == "artist":
        artist_mess = f"Создатель дизайна карт - художница Матильда\n" \
                      f"https://matilllda.ru/"
        botPredskazatel.send_message(call.message.chat.id, artist_mess)



botPredskazatel.infinity_polling()