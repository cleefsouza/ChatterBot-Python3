# -*- coding: utf-8 -*-

# chatterBot
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

# operacional system biblioteca
import os

bot = ChatBot('Bot') # bot

bot.set_trainer(ListTrainer) # definindo metodo de treinamento

for arq in os.listdir('chat'):
    serie = open('chat/' + arq, 'r').readlines() # lendo arquivos de conversas
    bot.train(serie) # treinando

while True: # loop de conversação
    entrada = input('Você: ') # entrada do usuário
    saida = bot.get_response(entrada) # resposta do bot
    if (float(saida.confidence) > 0.5): # nível de confiança para responder: 5%
        print('Bot: ', saida)
    else:
        print('Bot: Não sei responder, por favor, me explique ...')
