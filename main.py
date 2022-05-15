from wordcloud import WordCloud
import Parser
import sys
from helper import stopWordsGetter

STOPWORDS = stopWordsGetter()


name = sys.argv[1]
inputFilePath = sys.argv[2]
imageName = sys.argv[3]
print(sys.argv)
p = Parser.Parser(inputFilePath,name)
text = p.parse()
updatedText = text.lower()
wordCloud = WordCloud(width=800,height=800,stopwords=STOPWORDS,background_color="white").generate(updatedText)
wordCloud.to_file(imageName)

