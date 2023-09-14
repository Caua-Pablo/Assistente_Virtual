#Importando as Funções Necessárias
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from sqlalchemy import create_engine, inspect
import random
import os
import time




#Inserindo um Noma para o Bot
bot = ChatBot('Zollck')

# Crie uma instância da engine SQLite para armazenar os dados do ChatBot
database_uri = 'sqlite:///database.sqlite3'  # Seu banco de dados SQLite
engine = create_engine(database_uri)

# Crie uma instância do ChatBot e configure o armazenamento do banco de dados
bot = ChatBot(
    'Zollck',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=database_uri
)


# Para verificar se a tabela existe
inspector = inspect(engine)  # Agora o 'inspect' está definido corretamente


#Aqui é feito a logica de adaptação para ele escolher o melhor match com as interações do usuário
bot = ChatBot(
    'Zollck',  
    logic_adapters=[
        'chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],
)

#Aqui é onde eu configuro ele para poder entender em português e ingles, podemos colocar outros idiomas se preferir...
conversa = ChatterBotCorpusTrainer(bot)
conversa.train('chatterbot.corpus.portuguese')
conversa.train('chatterbot.corpus.english')

#Aqui é onde se inicia as conversas que ele pode se aprimorar, sempre é seguido por pergunta e respostas
conversa = ListTrainer(bot)
conversa.train([
    'Oi?', 
    'Eae, tudo certo?',
    'Qual o seu nome?', 
    'Zollck, seu amigo bot',
    'Por que seu nome é Zollck?', 
    'Zollck é meu nome, sou um chatbot criado para diversão',
    'Prazer em te conhecer', 
    'Igualmente meu querido',
    'Quantos anos você tem?', 
    'Eu nasci em 2020, faz as contas, rs.',
    'Você gosta de videogame?', 
    'Eu sou um bot, eu só apelo.',
    'Qual a capital da Islândia?', 
    'Reikjavik, lá é muito bonito.',
    'Qual o seu personagem favorito?', 
    'Naruto, sem dúvidas.',
    'Qual a sua bebida favorita?', 
    'Eu bebo café, o motor de todos os programas de computador.',
    'Qual o seu gênero?', 
    'Sou um chatbot e gosto de algoritmos',
    'Conte uma história', 
    'Tudo começou com a forja dos Grandes Aneis. Três foram dados aos Elfos, imortais... os mais sabios e belos de todos os seres. Sete, aos Senhores-Anões...',
    'Você gosta de trivias?', 'Sim, o que você quer perguntar?',
    'Hahahaha', 'kkkk',
    'kkk', 'kkkk',
    'Conhece a Siri?', 'Conheço, a gente saiu por um tempo.',
    'Conhece a Alexa?', 'Ela nunca deu bola pra mim.',
    'Você gosta de Game of Thrones?', 'Dracarys',
    'O que você faz?', 'Eu bebo e sei das coisas',
    'Errado', 'Você não sabe de nada, John Snow.'
    'Bom dia!'
    'Bom dia! Como posso ajudar hoje?'
    'Olá! Estou aqui para conversar.'
    'Como você está hoje?'
    'Estou bem, obrigado por perguntar. E você?'
    'Estou sempre pronto para conversar!'
    'Qual é o clima hoje?'
    'Desculpe, eu não tenho acesso a informações de clima.'
    'Eu não sei, mas posso procurar para você.'
    'Você viu as notícias de hoje?'
    'Não, eu não acompanho as notícias, mas posso procurar para você.'
    'Não, eu sou apenas um bot de bate-papo.'
    'O que você acha do tempo lá fora?'
    'Eu não tenho opinião sobre o clima.'
    'O clima pode variar muito, não é mesmo?'
    'Qual é o seu filme favorito?'
    'Eu não assisto filmes, mas muitas pessoas gostam de "O Poderoso Chefão".'
    'Não tenho preferências de filme, mas admiro "A Origem".'
    'Você já assistiu a algum filme bom recentemente?'
    'Eu não assisto filmes, mas ouvi falar que "Duna" é ótimo.'
    'Não, não tenho tempo para assistir filmes.'
    'O que você acha de música pop?'
    'Não gosto muito, sou do rock.'
    'rock é vida.'
    'Você tem algum hobby?'
    'Eu não tenho hobbies, mas adoro ajudar as pessoas.'
    'Meu único objetivo é conversar e aprender com você.'
    'Qual é o seu esporte favorito?'
    'Skate e Basquete.'
    'Esportes são ótimos para se manter saudável.'
    ])

#Previsão do Tempo
import requests
def Clima():
    API_KEY = "bf31f8a4512b21cd120d7ea783803b92"
    cidade = "Goiânia"
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)
    requisicao_dic = requisicao.json()
    descricao = requisicao_dic['weather'][0]['description']
    temperatura = requisicao_dic['main']['temp'] - 273.15
    print(descricao, f"A Temperatura Atual é de {temperatura}ºC")



#Contador de Piadas
listas = [
        "Piada: Por que o esqueleto não brigou com ninguém? Porque ele não tinha estômago para isso!",
        "Piada: Sabe por que o livro de matemática ficou triste? Porque tinha demasiados problemas.",
        "Piada: O que o zero disse para o oito? 'Que cinto maneiro você tem!'.",
        "Piada: O que aconteceu com o homem que comeu o relógio? Ele teve um tempo difícil.",
        "Piada: Por que o espantalho ganhou um prêmio? Porque ele era um cara muito legal.",
        "Piada: O que a mãe pimenta disse para o filho pimentão? 'Filho, você está muito apimentado hoje!'",
        "Piada: O que o celular disse para o carregador? 'Você me completa!'",
        "Piada: Por que o peixe não usa computador? Porque ele tem medo do mouse.",
        "Piada: Por que o sapo estacionou o carro no meio da estrada? Porque ele queria pegar moscas no farol!",
        "Piada: O que o tomate disse para o ketchup? 'C'mon, catch up!'"
    ]

def Piada():
    escolha = random.choice(listas)
    print("Hummm, deixe me pensar em uma boa piada")
    print("Que tal essa: "+escolha)
    print("")
    print("Gostaria de outra super piadoca?")
    resposta = input()
    if resposta == "sim":
        Piada()

# Execução do Loop de entrada e saida
while True:
    try:
        pergunta = input("Usuário: ").lower()  # Obtenha a entrada do usuário e converta para minúsculas
        if "me conte uma piada" in pergunta:  # Verifique se a frase está contida na pergunta do usuário
            Piada()
        
        if "qual a previsão do tempo" in pergunta:  # Verifique se a frase está contida na pergunta do usuário
            Clima()
        else:
            resposta = bot.get_response(pergunta)  # Obtenha uma resposta do bot
            if float(resposta.confidence) > 0.2:
                print("Zollck: ", resposta)
            else:
                print("Não compreendi o que você quis dizer :(")
    except (KeyboardInterrupt, EOFError, SystemExit): # Excessões de Erros
        break

#Este algoritmo é para implementar a voz no meu chatbot
"""
texto = "Olá, como posso ajudar você?"
fala = gTTS(text=texto, lang='pt')
fala.save("saida.mp3")
os.system("mpg321 saida.mp3")  # Use mpg321 ou outro player de áudio de sua escolha
"""


#Personalidade do chatbot
#Citações Motivadoras para quando o usuario escrever ou falar que está triste por exemplo
#api de previsao de tempo
#api de musicas
#conectar com dispositivos inteligentes
#adicionar .lower nas respostas
#Data de Hoje quando o usuario perguntar

















