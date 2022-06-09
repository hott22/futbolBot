from config import TOKEN
from telegram.ext import CommandHandler, MessageHandler, filters, ApplicationBuilder
from bots_commands import *

app = ApplicationBuilder().token(TOKEN).build()
filter_text = ['+', '-', '+1', '-1']

app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.Text(filter_text), callback=run))
app.add_handler(MessageHandler(filters.TEXT, callback=log))

print('start')
app.run_polling(stop_signals=None)
