#g the resulting .csv file from your answers to part one of the Sentiment Classifier project, create a scatterplot of the Number of Retweets vs the Net Score using Excel, Google Sheets, or another software package of your choosing. Review the Introductory video for this project if you are unsure of how the graph should look, approximately. Be sure to correctly label your axes and give it a meaningful title! You will upload a screenshot of your scatterplot for submission, and review 3 other submissions to check other students work.

projectTwitterDataFile = open("project_twitter_data.csv","r")fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.
resultingDataFile = open("resulting_data.csv","w")
 classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to used strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)
positive_words = []
with open("positive_words.txt") as pos_f:", ".", "!", ":", ";", '#', '@']
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(strSentences):s' % i, '')
    strSentences = strip_punctuation(strSentences)



    listStrSentences= strSentences.split()

    count=0s' % i, '')
    for word in listStrSentences:


        for positiveWord in positive_words:
            if word == positiveWord:lit()
                count+=1
    return count

negative_words = []
with open("negative_words.txt") as pos_f:


    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':lit()
            negative_words.append(lin.strip())


def get_neg(strSentences):
    strSentences = strip_punctuation(strSentences)

    listStrSentences = strSentences.split()

    count=0
    for word in listStrSentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count+=1
    return count


def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord)
)
nt,pos_count,neg_count,score']
def writeInDataFile(resultingDataFile):
    resultingDataFile.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    resultingDataFile.write("\n")

    linesPTDF =  projectTwitterDataFile.readlines()
    headerDontUsed= linesPTDF.pop(0)
    for linesTD in linesPTDF:
        listTD = linesTD.strip().split(',')
        resultingDataFile.write("{}, {}, {}, {}, {}".format(listTD[1], listTD[2], get_pos(listTD[0]), get_neg(listTD[0]), (get_pos(listTD[0])-get_neg(listTD[0]))))
        resultingDataFile.write("\n")



writeInDataFile(resultingDataFile)
projectTwitterDataFile.close()- neg_count[i])
resultingDataFile.close()

###############################################
id for id in i))

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']_count[i]) + str(neg_count[i]) + str(pos_count[i] + neg_count[i])
# list of positive words to usets, Number of Replies, Positive Score, Negative Score, Net Score")
positive_words = []
with open("positive_words.txt") as pos_f:d in res)
    for lin in pos_f: 'w') as csvFile:
        if lin[0] != ';' and lin[0] != '\n':


            positive_words.append(lin.strip())
