memes_actuales = {
     "BRAINROTS":"son animales combinados con cosas",
     "AURA":"es cuando haces algo y te alegra mucho",
     "XD":"por dios",
     "WTF":"what that fuck",
     "OMG":"ay mi dios",
}
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
if word in memes_actuales.keys():
    print(memes_actuales[word])
else:
    print("esa palabra no esta en el diccionario")
    
     
