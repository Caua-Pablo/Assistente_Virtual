#Importando as Funções Necessárias
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#Inserindo um Noma para o Bot
bot = ChatBot('Zollck')

#Aqui é onde será criado o repositorio do banco de dados para ser salvos as interações
bot = ChatBot(
    'Zollck',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

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
    'Gandalf, o mago.',
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
    'Música pop é muito popular, muitas pessoas gostam.'
    'Música pop pode ser divertida de vez em quando.'
    'Você tem algum hobby?'
    'Eu não tenho hobbies, mas adoro ajudar as pessoas.'
    'Meu único objetivo é conversar e aprender com você.'
    'Qual é o seu esporte favorito?'
    'Eu não pratico esportes, mas muitas pessoas gostam de futebol.'
    'Esportes são ótimos para se manter saudável.'
    ])

while True:
    try:
        resposta = bot.get_response(input("Usuário: "))
        if float(resposta.confidence) > 0.2:
            print("Zollck: ", resposta)
        else:
            print("Não compreendi o que você quis dizer :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break


#Este algoritmo é para implementar a voz no meu chatbot

#from gtts import gTTS
import os
# Texto que você deseja converter em fala
texto = "Olá, como posso ajudar você?"
# Crie um objeto gTTS
fala = gTTS(text=texto, lang='pt')
# Salve o arquivo de áudio
fala.save("saida.mp3")
# Reproduza o áudio (você pode precisar de um player de áudio)
os.system("mpg321 saida.mp3")  # Use mpg321 ou outro player de áudio de sua escolha

#testando
#Contador de piadas
#Personalidade do chatbot
#Citações Motivadoras para quando o usuario escrever ou falar que está triste por exemplo
#api de previsao de tempo
#api de musicas
#conectar com dispositivos inteligentes
#teste