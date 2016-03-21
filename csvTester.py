import csv
import argparse
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

classificationResults = {}

class CSVFetcher():
    def __init__(self, fileName):
        self.fileName = fileName + '.csv'


    def fetch(self):
        print("fetcher.fetch")
        with open(self.fileName, 'rb') as f:
            reader = csv.reader(f)
            for line in reader:
                yield line



#with open('housewife1000.csv', 'rb') as f:
#    reader = csv.reader(f, delimiter=',')
#    myList = list(reader)

if __name__ == "__main__":

    c1 = NaiveBayesClassifier(train)

    parser = argparse.ArgumentParser(
        description="Classify stories based on our NaiveBayesClassifier",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('filename', help="Data Input file")
    parser.add_argument('-w', '--write', type=str, help="Write to filename")
    args = parser.parse_args()

    args.filename = unicode(args.filename)
    fetcher = CSVFetcher(args.filename)

    myPos = 0
    myNeg = 0
    for story in fetcher.fetch():
        #print(count)
        x = c1.classify(story[3].decode('utf-8'))

        if (x == 'pos'):
            myPos +=1
            if(story[0] not in classificationResults):
                classificationResults[story[0]] = {'pos': 1}
            elif( 'pos' not in classificationResults[story[0]]):
                classificationResults[story[0]].update( {'pos': 1} )
            else:
                classificationResults[story[0]]['pos'] += 1
        else:
            myNeg += 1
            if(story[0] not in classificationResults):
                classificationResults[story[0]] = {'neg': 1}
            elif( 'neg' not in classificationResults[story[0]] ):
                classificationResults[story[0]].update( {'neg': 1} )
            else:
                classificationResults[story[0]]['neg'] += 1
        print(x)
    print('positive: ')
    print(myPos)
    print('negative: ')
    print(myNeg)

    if(args.write):
        outFile = open(args.write + '.csv', 'wb')
        outCSVWriter = csv.writer(outFile)

    for x in range(1836, 1922):

        if(args.write is None):
            if(str(x) in classificationResults):
                print("Year: " + str(x))
                if('pos' in classificationResults[str(x)]):
                    print("Positive: " + str(classificationResults[str(x)]['pos']))
                else:
                    print("Positive: 0" )
                
                if('neg' in classificationResults[str(x)]):
                    print("Negative: " + str(classificationResults[str(x)]['neg']))
                else:
                    print("Negative: 0")
        else:
            if(str(x) in classificationResults):
                year = str(x)
                positive = classificationResults[str(x)]['pos'] if ('pos' in classificationResults[str(x)]) else 0
                negative = classificationResults[str(x)]['neg'] if ('neg' in classificationResults[str(x)]) else 0
                entry = [year, positive, negative]
                outCSVWriter.writerow(entry)

