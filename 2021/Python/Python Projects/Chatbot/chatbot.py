import nltk
from nltk.chat.util import Chat,reflections
reflections = {
    "i am"      :  "you are",
    "i was"     :  "you were",
    "i "      :  "you",
    "i'm"      :  "you are",
    "i'd"      :  "you would",
    "i've"      :  "you have",
    "i'll"      :  "you will",
    "my"      :  "your",
    "you are"      :  "I am",
    "you were"      :  "I was",
    "you've"      :  "I have",
    "you'll"      :  "I will",
    "your"      :  "my",
    "yours"      :  "mine",
    "you"      :  "me",
    "me"      :  "you",
}
pairs=[
    [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"hi|hey|hello",
       ["Hello","Hey there",]
    ],
     [
      
       r"what is your name ?",
       ["I am a bot created by master Dhruval.you can call me Ultron!",]
    ],
     [
      
       r"how are you?",
       ["I am doing good n How about you?",]
    ],
     [
      
       r"sorry(.*)",
       ["Its alright","it's okay","never mind",]
    ],
     [
      
       r"I am fine",
       ["Great to hear that ,How can i help you today!",]
    ],
     [
       r"",
       ["Hello %1, How are you today ?"]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
     [
      
       r"my name is(.*)",
       ["Hello %1, How are you today ?",]
    ],
]
def chat():
    print("Hi! I am ULTRON created by master for you . ")
    chat=Chat(pairs,reflections)
    chat.converse()
if __name__=="__main__":
  chat()