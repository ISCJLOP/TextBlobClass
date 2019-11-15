from textblob import TextBlob

eb=TextBlob('HELLO WORLD')
print (eb.translate(from_lang='en', to='es'))