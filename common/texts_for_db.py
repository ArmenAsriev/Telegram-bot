from aiogram.utils.formatting import Bold, as_list, as_marked_section

# Заглушки для категорий и текстов
categories = ['Ваш текст', 'Ваш текст']  # Пример: ['Еда', 'Напитки']

# Описание для информационных страниц
description_for_info_pages = {
    "main": "Ваш текст",  # Пример: "Добро пожаловать!"
    "about": "Ваш текст",  # Пример: "Пиццерия Такая-то.\nРежим работы - круглосуточно."
    "payment": as_marked_section(
        Bold("Ваш текст"),  # Пример: Bold("Варианты оплаты:")
        "Ваш текст",  # Пример: "Картой в боте"
        "Ваш текст",  # Пример: "При получении карта/кеш"
        "Ваш текст",  # Пример: "В заведении"
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("Ваш текст"),  # Пример: Bold("Варианты доставки/заказа:")
            "Ваш текст",  # Пример: "Курьер"
            "Ваш текст",  # Пример: "Самовынос (сейчас прибегу заберу)"
            "Ваш текст",  # Пример: "Покушаю у Вас (сейчас прибегу)"
            marker="✅ ",
        ),
        as_marked_section(Bold("Ваш текст"), "Ваш текст", "Ваш текст", marker="❌ "),  # Пример: Bold("Нельзя:"), "Почта", "Голуби"
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Ваш текст',  # Пример: 'Категории:'
    'cart': 'Ваш текст'  # Пример: 'В корзине ничего нет!'
}

