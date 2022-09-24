import telegram
from telegram import *
from telegram.ext import *
import os

# AL INICIARSE EL BOT
destinatarios = []
def auth(adms):
    if adms.__contains__(' '):
        adms=f"{adms}".replace(' ','')
    for adm in adms.split(','):
        adm = int(adm)
        destinatarios.append(adm)
    print(destinatarios)

# DECIDE SI EL MENSAJE ES DE UN ADMINISTRADOR O ES DE UN USUARIO
def clasifique(update,context):
    print(update.message.chat.id)
    if not update.message.chat.id in destinatarios:
        send2admins(update,context)
    if update.message.chat.id in destinatarios:
        reply2users(update,context)

# ENVIAR MENSAJE A LOS ADMINISTRADORES
def send2admins(update,context):
    for adm in destinatarios:
        bot.forward_message(chat_id=adm,from_chat_id=update.message.chat.id,message_id=update.message.message_id)
# ENVIAR RESPUESTA A LOS USUARIOS
def reply2users(update,context):
    if str(update.message.reply_to_message) != 'None': # SI RESPONDES A UN MENSAJE
        chat1 = update.message.reply_to_message.chat.id
        chat2 = update.message.reply_to_message.forward_from.id
        sms = update.message.message_id
        bot.copy_message(chat_id=chat2,from_chat_id=chat1,message_id=sms)
    else: # SI NO RESPONDES A UN MENSAJE
        bot.sendMessage(chat_id=update.message.chat.id,text='BOT: Error tienes que responder a un mensaje para poder enviarle tu respuesta')

# TOKEN
if __name__ == '__main__':
    token = '5751727310:AAGdsE5pFJSMu5hfvXJhlf2FyiXa5Ow2MOM'
    administradores = '952546654'
    bot = telegram.Bot(token=token)
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher

# Despachadores
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.all,callback=clasifique))

# Para Ejecutar el Bot
    auth(administradores)
    updater.start_polling()
    print("Ejecutando el bot @" + bot.username)
    updater.idle()