from textblob import TextBlob
file=open('text.txt')
t=file.read()
print(t)
trad=TextBlob(t)
print (trad.translate(from_lang='en', to='es'))