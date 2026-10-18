async def handle_update(update, telegram) -> None:
    if update.message is None or update.message.text is None:
        return  # не текст: стикер, фото и т.п. Пока пропускаем

    text = update.message.text
    chat_id = update.message.chat.id

    if text == "/start":
        await telegram.send_message(chat_id, "Привет!")
    else:
        await telegram.send_message(chat_id, f"Ты написал: {text}")