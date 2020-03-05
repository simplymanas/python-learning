from nltk.chat.util import Chat, reflections
pairs = [[r"my name is (.*)", ["Hello %1. How are you doing today"]], ]

# pairs = {
#     "i am": "you are",
#     "i was": "you were",
#     "i": "you",
#     "i'm": "you are",
#     "i'd": "you would",
#     "i've": "you have",
#     "i'll": "you will",
#     "my": "your",
#     "you are": "I am",
#     "you were": "I was",
#     "you've": "I have",
#     "you'll": "I will",
#     "your": "my",
#     "yours": "mine",
#     "you": "me",
#     "me": "you",
# }


def firstChatBot():
    print("I AM A C R O N Y M - B O T")
    chatbot = Chat(pairs, reflections)
    chatbot.converse()

if __name__ == '__main__':
    firstChatBot()

