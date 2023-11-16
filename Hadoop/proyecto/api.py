import wikipediaapi
import json
import os

opcion = [
    "Albert Einstein",
    "The French Revolution",
    "The Theory of Relativity",
    "DNA",
    "The Universe",
    "The History of the Earth",
    "The Human Brain",
    "Artificial Intelligence",
    "Climate Change",
    "Evolution",
    "Democracy",
    "Freedom of Speech",
    "Gender Equality",
    "Human Rights",
    "Poverty",
    "Hunger",
    "War",
    "Peace",
    "Life Expectancy",
    "Health",
    "Education",
    "Culture",
    "Art",
    "Literature",
    "Music",
    "Film",
    "Theatre",
    "Dance",
    "Basketball",
    "Germany"
]

def search(folder, opcion, number):
  wiki = wikipediaapi.Wikipedia(user_agent='Tarea3',language='en',extract_format=wikipediaapi.ExtractFormat.WIKI)
  page = wiki.page(opcion)
  if page.exists():
     isFile = os.path.isfile(f"./{folder}/search{number}.txt")
     if (isFile):
        os.remove(f"./{folder}/search{number}.txt")

     crear = open(f"./{folder}/search{number}.txt","wb") #open file in binary mode
     crear.write(str(page.text).encode('utf-8'))
     crear.close()

for i in range(30):
    if(i<15):
        search('1_15', opcion[i], i+1)
    else:
        search('16_30', opcion[i], i+1)
