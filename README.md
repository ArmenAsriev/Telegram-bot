# Telegram Bot with Aiogram

This project is a Telegram bot built with Aiogram and SQLAlchemy that connects to a **PostgreSQL** or **SQLite** database. It supports user interactions, including both private and group messaging, with a middleware for database session management and pagination for data presentation.

## Project Features

- **User Interaction**: Supports private and group messaging, with different handlers for user and admin communication.
- **Database Integration**: Connects to PostgreSQL (or SQLite) for storing and managing data, with an asynchronous session handler.
- **Pagination**: Implements a simple paginator to manage large datasets and display them across multiple pages.
- **Middleware for Database Sessions**: Uses middleware to inject database sessions into handlers automatically.
- **Modular Code Structure**: The project is organized into multiple modules, each handling a specific part of the bot's functionality (e.g., handlers, middlewares, database).

## Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/ArmenAsriev/Telegram-bot.git
   cd telegram-bot-aiogram
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the bot:
   ```bash
   python app.py
   ```


# Телеграм-бот на Aiogram

Этот проект представляет собой телеграм-бота, построенного с использованием **Aiogram** и **SQLAlchemy**, который может подключаться как к базе данных **PostgreSQL**, так и к **SQLite**. Бот поддерживает взаимодействие с пользователями, включая частные и групповые сообщения, с использованием промежуточного ПО для управления сессиями базы данных и пагинации для отображения данных.

## Особенности проекта:
- **Взаимодействие с пользователями**: Поддерживает частные и групповые сообщения, с разными обработчиками для пользователей и администраторов.
- **Интеграция с базой данных**: Подключается к PostgreSQL (или SQLite) для хранения и управления данными с асинхронным обработчиком сессий.
- **Пагинация**: Реализует простой пагинатор для управления большими наборами данных и отображения их на нескольких страницах.
- **Промежуточное ПО для сессий базы данных**: Использует промежуточное ПО для автоматической инъекции сессий базы данных в обработчики.
- **Модульная структура кода**: Проект организован в несколько модулей, каждый из которых отвечает за определенную часть функционала бота (например, обработчики, промежуточное ПО, база данных).

## Установка:

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/ArmenAsriev/Telegram-bot.git
   cd telegram-bot-aiogram
   ```
2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
3.Запустите бота:
   ```bash
   python app.py
   ```
