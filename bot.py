from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8726059130:AAHUDmAixom_xYoESxM4Wh6AMzw5w5j5BuE"

keyboard = ReplyKeyboardMarkup(
    [
        ["Подобрать уход", "Макияж"],
        ["Парфюм", "Доставка"],
        ["Возврат", "Консультант"]
    ],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я Люда, бот Avimi 💖\n"
        "Помогу подобрать косметику и отвечу на вопросы.",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "подобрать уход" in text:
        await update.message.reply_text(
            "Напиши, пожалуйста:\n"
            "1. Тип кожи\n"
            "2. Что хочешь подобрать\n"
            "3. Бюджет"
        )
    elif "макияж" in text:
        await update.message.reply_text(
            "Напиши, что тебе нужно: тон, тушь, помада, тени или полный набор 💄"
        )
    elif "парфюм" in text:
        await update.message.reply_text(
            "Какой аромат ты ищешь: сладкий, свежий, цветочный или вечерний? 🌸"
        )
    elif "доставка" in text:
        await update.message.reply_text(
            "Доставка доступна по условиям магазина Avimi. Напиши свой город, и я подскажу подробнее."
        )
    elif "возврат" in text:
        await update.message.reply_text(
            "Опиши проблему с заказом, и я подскажу, как оформить возврат."
        )
    elif "консультант" in text:
        await update.message.reply_text(
            "Хорошо 💌 Напиши свой вопрос одним сообщением, и его можно будет передать консультанту."
        )
    else:
        await update.message.reply_text(
            "Я пока в базовой версии 😊 Выбери кнопку в меню или напиши, что ищешь."
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
