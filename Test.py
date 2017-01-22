import sys
#from urllib2 import Request, build_opener
from urllib.request import urlopen
#from urllib import urlopen

#from urllib2 import urlopen
#from urllib.request import urlopen
#from urllib2.request import u

def main():
    print ("this is just a test")


#TODO: machine learning using python
def testURL():
    """
    this is the test url function for loading the print the words from the http response
    :return:
    """
    #request = Request("http://sixty-north.com/c/t.txt")
    with urlopen("http://sixty-north.com/c/t.txt") as story:
    #with build_opener().open(request) as story:
        story_words = []
        for line in story:
            #print (line)
            line_words =  line.split()
            for word in line_words:
                story_words.append(word)
        #print ("check words: " + story_words.)
        for word in story_words:
            print (word.decode("utf-8"))

#main()
#testURL()
