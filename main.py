from typing import final
from telegram import Update
import logging
import requests
from telegram.ext import Application, CommandHandler,MessageHandler,filters,ContextTypes

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

API_KeY:final='6058673407:AAELh1DaUv9bMWKRBwg6NFhIT189fYzCAiM'
BOT_USERNAME:final='@Skin_Disease_Classification_bot'


async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Please send me the picture of infected area')

async def help_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Helo!I am a Bot created by team ExploringGeeks i use Artifical Intelligence to classify your skin disease")


# Define a handler for image messages
async def detect_allergy(update:Update, context:ContextTypes.DEFAULT_TYPE):
    print('i am here')
    if update.message.photo:
        # Get the file ID of the photo
        file_id = update.message.photo[-1].file_id

        # Download the image from Telegram
        file = context.bot.getFile(file_id)
        image_url = file.file_path
        image = requests.get(image_url).content

        # Perform skin allergy detection on the image (replace this with your own detection logic)
        # ... (your allergy detection code here)
        # result = your_allergy_detection_function(image)

        # Send the result to the user
        await update.message.reply_text('Allergy detected: ')

    else:
        # If the message doesn't contain an image, prompt the user to send an image
        await update.message.reply_text('Please send me an image to detect allergies.')

# Create an error handler function
def error(update:Update, context:ContextTypes.DEFAULT_TYPE):
    logging.error('Update "%s" caused error "%s"', update, context.error)



if __name__=='__main__':
    print('Starting Bot')
    app=Application.builder().token(API_KeY).build()

    app.add_handler(CommandHandler('start',start_command))
    app.add_handler(CommandHandler('help',help_command))
    app.add_handler(MessageHandler(filters.PHOTO, detect_allergy))
    app.add_error_handler(error)

    print('polling')
    app.run_polling(poll_interval=3)