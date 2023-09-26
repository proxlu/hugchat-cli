#!/bin/python3
# -*- coding: utf-8 -*-
#
# llama.py - by:proxlu
from hugchat import hugchat
from hugchat.login import Login
import sys
import subprocess

# Carregamento
print('Processando...')

# Faz login no huggingface
sign = Login("EMAIL_AQUI", "SENHA_AQUI")

# Pega toda entrada
arg = ' '.join(sys.argv[1:])

# Cria um chatbot
chatbot = hugchat.ChatBot(sign.login())

# Estrutura principal
if arg:
	try:
		saida_da_api = chatbot.chat(arg)
	except:
		pass
	# Comando a ser executado no terminal usando subprocess (com aspas simples)
	comando = ['trans', '-b', saida_da_api]

	# Execute o comando no terminal e suprime erros
	saida = subprocess.check_output(comando, stderr=subprocess.DEVNULL)
	saida_decodificada = saida.decode('utf-8')
	saida_corrigida = saida_decodificada.replace('u003d', '=')
	print()
	print('Llama:', saida_corrigida)
else:
	# Mensagem de introdução
	print()
	print('[\'Oi, me chamo Llama, vamos conversar!\']')
	print('\'s\' ou \'sair\' para sair')
	print('\'p\' ou \'protocolo\' para exibir o protocolo')
	print('\'l\' ou \'limpar\' para limpar a conversa')
	print('\'a\' ou \'ajuda\' para exibir novamente')
	print()
	# Chat
	while True:
		texto = input('Você: ')
		if texto.lower() == '':
			pass
		elif texto.lower() in ['s', 'sair']:
			break
		elif texto.lower() in ['p', 'protocolo']:
			print()
			print(chatbot.get_conversation_list())
			print()
		elif texto.lower() in ['l', 'limpar']:
			subprocess.call("clear", shell=True)
		elif texto.lower() in ['a', 'ajuda']:
			print()
			print('\'s\' ou \'sair\' para sair')
			print('\'p\' ou \'protocolo\' para exibir o protocolo')
			print('\'l\' ou \'limpar\' para limpar a conversa')
			print('\'a\' ou \'ajuda\' para exibir novamente')
			print()
		# Solicita resposta da api
		else:
			try:
				saida_da_api = chatbot.chat(texto)
			except:
				pass
			# Comando a ser executado no terminal usando subprocess
			comando = ['trans', '-b', saida_da_api]
			saida = subprocess.check_output(comando, stderr=subprocess.DEVNULL)
			saida_decodificada = saida.decode('utf-8')
			saida_corrigida = saida_decodificada.replace('u003d', '=')
			print()
			print('Llama:', saida_corrigida)

