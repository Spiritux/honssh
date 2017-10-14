import telegram
import os
from tgconf import *

def tgMessage(cadena, loglevel):
        #spi
        for el in destinatarios.keys():
                if destinatarios.get(el) >= loglevel:
                        bot.sendMessage(chat_id = el, text='[S]'+cadena) 

def tgBootMessage(cadena,loglevel):
        for el in destinatarios.keys():
                if destinatarios.get(el) >= loglevel:
                        bot.sendMessage(chat_id = el, text='[S]['+str(loglevel)+'][Sweet '+el+']'+cadena) 

def tgSendFile(tgFile):
        for el in destinatarios.keys():
                fd=open(path_to_folder_files+tgFile,'rb')
                bot.sendDocument(chat_id = el, document=fd)
                fd.close()
