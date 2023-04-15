from typing import final
from telegram import Update
from telegram.ext import Application, CommandHandler,MessageHandler,filters,ContextTypes
API_KeY:final='6058673407:AAELh1DaUv9bMWKRBwg6NFhIT189fYzCAiM'
BOT_USERNAME:final='@Skin_Disease_Classification_bot'


async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Please send me the picture of infected area')

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Helo!I am a Bot created by team ExploringGeeks i use Artifical Intelligence to classify your skin disease")


# def handle_responses()

if __name__=='__main__':
    print('Starting Bot')
    app=Application.builder().token(API_KeY).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))

    #messages

    # app.add_handler(MessageHandler(filters.TEXT,han))
    print('polling')
    app.run_polling(poll_interval=3)