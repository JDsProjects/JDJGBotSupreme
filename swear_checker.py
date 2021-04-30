bad_words= [ 
  "nigg",
  "damn",
  "hell",
  "shit",
  "shithead",
  "ass hat",
  'faggot',
  'retard',
  'bastard',
  'nigga',
  "hitler",
  "RenDev"
]
sexual_words =[
  "fuck",
  "cunt",
  "pussy",
  "ass",
  "penis",
  "dick",
  "vagina",
  "sex",
  "masturbate",
  "cum",
  "jack off",
  "skin flute",
  "coochie",
  "condom",
  "peen",
  "ejaculate",
  "semen",
  "sperm",
  "wet dream",
]

bad_word_list = sexual_words+bad_words

import DatabaseConfig
col = DatabaseConfig.db.server_settings

cmp_list = bad_words.append(sexual_words)


def filter_words(message, guild):
  doc = col.find_one({"ser_id":guild})
  endings = ["ing","er","ist","ed","en","tion",""]
  message = message.lower()
  words_found =[]
  for obj in cmp_list:
    slur_pass = 0
    if obj in doc["slur"]:
      slur_pass = 1
    if(slur_pass==0):
      for ends in endings:
        word = obj.lower() + ends.lower()
        if word in message:
          words_found.append(obj.lower())
  return words_found
def censor_message(message,guild):
  message = message.split(" ")
  words_found = filter_words(message,guild)
  new_mess = ""
  begin_bool = 1
  for word in message:
    for i in range(len(word)):
      censor = censor + "*"
    if(begin_bool):
      begin_bool = 0;
      if not (word.lower() in words_found):
        new_mess = new_mess + word
      else:
        new_mess = new_mess + censor
    else:
      if not (word.lower() in words_found):
        new_mess = new_mess + " " + word
      else:
        new_mess = new_mess + censor
  return new_mess


