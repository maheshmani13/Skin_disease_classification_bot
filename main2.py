import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import joblib
import numpy as np
import tensorflow




# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define bot token
TOKEN = '6058673407:AAELh1DaUv9bMWKRBwg6NFhIT189fYzCAiM'

# Create a function to handle /start command
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Welcome to Skin Allergy Detector! Please send me an image of your skin to detect allergies.')

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Helo!I am a Bot created by team ExploringGeeks i use Artifical Intelligence to classify your skin disease')


# Create a function to handle user messages
def detect_allergy(update, context):
    # Check if the message contains an image
    print('hi')
    if update.message.photo :
        # Get the file ID of the photo
        file_id = update.message.photo[-1].file_id

        # Download the image from Telegram
        file = context.bot.getFile(file_id)
        image_url = file.file_path
        image = requests.get(image_url).content

        # Perform skin allergy detection on the image (replace this with your own detection logic)
        # ... (your allergy detection code here)
        # result = your_allergy_detection_function(image)
        classifier = joblib.load('model_joblib.pkl')
        img = image.resize((200,200))
        imageToMatrice = np.asarray(img)
        image = imageToMatrice.reshape(120000)
        image = image/255.0
        
        y_pred = classifier.predict(image.reshape(1,200,200,3))
        maximum = np.amax(y_pred)
        index = int(np.where(y_pred == maximum)[1])
        disease = "can't classify"
        
        if(index==1):
            disease = 'eczema'
        if(index==2):
            disease = 'actinic_keratosis_basal_cell_carcinoma'
        if(index==3):
            disease = 'atopic_dermatitis'
        if(index==4):
            disease = 'melanoma_skin_cancer_moles'
        if(index==5):
            disease = 'ringworm_candidiasis_fungal'
        if(index==6):
            disease = 'urticaria_hives'
        if(index==7):
            disease = 'seborrheic_keratoses_and_benign_tumors'
        if(index==8):
            disease = 'psoriasis_lichen_related'

        # Send the result to the user
        context.bot.send_message(chat_id=update.effective_chat.id, text=f'Allergy detected:' + disease)
    else:
        # If the message doesn't contain an image, prompt the user to send an image
        context.bot.send_message(chat_id=update.effective_chat.id, text='Please send me an image to detect allergies.')

def showerror(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Please send me an image to detect allergies.')

# Create an error handler function
def error(update, context):
    logging.error('Update "%s" caused error "%s"', update, context.error)

# Create the main function to start the bot
def main():
    # Create an instance of the Updater class with the bot token
    updater = Updater(token=TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help))
    dispatcher.add_handler(MessageHandler(Filters.text, showerror))
    dispatcher.add_handler(MessageHandler(Filters.photo, detect_allergy))
    dispatcher.add_error_handler(error)

    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl-C is pressed
    updater.idle()

if __name__ == '__main__':
    main()
