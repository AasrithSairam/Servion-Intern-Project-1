
#install packages
# pip install "chatterbot==1.0.0"
# pip install pytz
# import required packages
from chatterbot import ChatBot

from chatterbot.trainers import ChatterBotCorpusTrainer

# create ChatBot
chatBot = ChatBot('ChatBot')

# create ChatBot trainer
trainer = ChatterBotCorpusTrainer(chatBot)

# Train ChatBot with English language corpus
# you can train with different language
# or with your custom .yam file
trainer.train("chatterbot.corpus.english")
while True:
    query=input(">>>")
    print(chatBot.get_response(query))

