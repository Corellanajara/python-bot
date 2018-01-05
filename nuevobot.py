from chatterbot import ChatBot

chatbot = ChatBot(
    'Charlie',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

# Get a response to an input statement
while 1:
    mensaje = raw_input("user : ")
    print("bot: ")
    chatbot.get_response(mensaje)
