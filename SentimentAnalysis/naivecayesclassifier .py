import pandas as pd 
from IPython.display import display
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
# from nltk.tokenize
dateset = pd.read_csv(f'/media/saad/943851B3385194D8/DataEng/Python/ideas/SentimentAnalysis/train.csv',delimiter='\t')
print("max_rows value after the change : " + 
      str(pd.options.display.max_rows))
pd.set_option("display.max_rows", 5)
display(dateset)
print("max_rows value after the change : " + 
      str(pd.options.display.max_rows))
# text_counts = 
# x_train,x_test,y_train,y_test = train_test_split(text_counts)
# MNP = MultinomialNB()
# MNP.fit(x_train,Y)