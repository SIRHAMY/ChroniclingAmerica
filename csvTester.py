import csv
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob


train = [
    ('I love a houseife.', 'pos'),
    ('Housewives are good.', 'pos'),
    ('A housewife is a worthy occupation.', 'pos'),
    ('A housewife keeps a family strong.', 'pos'),
    ('I feel very good about a housewife.', 'pos'),
    ('I am proud to be a housewife','pos'),
    ('housewife is the best work.', 'pos'),
    ('We need Housewives.', 'pos'),
    # ('I am proud to be a housewife.', 'pos'),
    ('Housewife loves their family.', 'pos'),
    ('Housewife loves their husband.', 'pos'),
    ('I hate housewives.', 'neg'),
    ('I do not like a housewife.', 'neg'),
    ('Housewives are not good.', 'neg'),
    ('A housewife is bad.', 'neg'),
    ('We do not need Housewives.', 'neg'),
    ('Stop leting women be a housewife.', 'neg'),
    ('A housewife is lazy.', 'neg'),
    ('All a housewife does is clean', 'neg'),
    ('All a housewife does is cook', 'neg'),
    ('I am not proud to be a housewife.', 'neg'),
    ('Houswife is good', 'pos'),
    ('Housewife is bad', 'neg')

]

c1 = NaiveBayesClassifier(train)

with open('housewife1000.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    myList = list(reader)
myPos = 0
myNeg = 0
for story in myList:
    #print(count)
    x = c1.classify(story[3].decode('utf-8'))
    if (x == 'pos'):
        myPos +=1
    else:
        myNeg += 1
    print(x)
print('positive: ')
print(myPos)
print('negative: ')
print(myNeg)
