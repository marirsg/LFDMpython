'''Main class of LDFM, goes through the pages and collects data '''

#=================================================================================
#------------ standard python libs
import os;
import time;
from urllib import urlopen;
#------------ support libraries
from bs4 import BeautifulSoup as Bsoup;
import nltk;
#------------ my classes

import LFDM_bsoupProcessor; 
import SupportFunctions;



#=============================GLOBAL VARIABLES=============================================
''' DO NOT include single context variables'''
baseSearchUrl = "https://forums.lutron.com/"
startSearchUrl = "https://forums.lutron.com/forumdisplay.php/30-HomeWorks-QS";
searchTokens = ['thermostats','third party','third-party']
debugPrinter = SupportFunctions.DebugOutput();


#===========================================================================================

#start of the search, and the website's base name.
'''print " Enter the base url website that you would like to "
userInput = raw_input();
if userInput != "":
    startSearchUrl = userInput;''' 

#============================================================================
#  "search for" items in a list
'''print "Enter the items that you would like to search for seperated by \',\' or space. Eg: Dimmers,Thermostats,Fixtures"
print "The more coherent/related your list is, the more relevant the search data will be"
userInput = raw_input();
if userInput != "":
    searchTokens = nltk.word_tokenize(userInput);
    searchTokens = [token for token in searchTokens if token != ','];'''
#============================================================================
# keywords to prioritize in a list
'''
print "Enter the keywords that you would like the data miner to look out for. This will help in prioritizing information"
print "Seperate keywords by space or \',\'"
keywordItems = raw_input();
keywordTokens = nltk.word_tokenize(keywordItems);
keywordTokens = [token for token in keywordTokens if token != ','];
print keywordTokens;
'''
#============================================================================
#delay between search pages (seconds, based on robots,.txt)

print "if the website that is being data mined has a robot.txt spec with delay between page requests, then enter value"
print "else just hit enter and the default value is 3 seconds between page requests"
interRequestDelay = 1;

'''
WHAT IS THIS FOR ? CHANGING INTER REQUEST DELAY? could be useful
while 1:
    try:
        userInput = raw_input();
        userInputinInt = int(userInput);
        break;
    except Exception as e:
        print "plz enter a valid value"
        print e;
   ''' 

#============================================================================
# Number of webpages or 0, for all webpages.

#============================================================================

#initialize search variables
urlLinksVisited = [];#list of strings of websites that have been mined
pendingUrlLinks = [];#list of strings of websites that are WAITING to be mined
allPostTokens = [];
nextUrlLink = startSearchUrl;
moreToGo = True;

#=====================MAIN LOOP
while moreToGo:
    #open the 'nextUrlLink' in a try except
    lutron_soup = "";
    #debugPrinter.addMessageToDebugOutput(nextUrlLink+"\n");
    try:
        # add test for ascii characters only
        openFileHandle = urlopen(nextUrlLink);                
        lutron_soup = Bsoup(openFileHandle.read());
        
        # create a new instance of a class to handle the processing of the soup                                    
    except Exception as expt:
        print "the \"try\" failed";
    finally:
        openFileHandle.close();
    
    if lutron_soup != "":
        bSoupProcessor = LFDM_bsoupProcessor.LutronSoupProcessor(lutron_soup,debugPrinter.addMessageToDebugOutput);
        allPostTokens.extend(bSoupProcessor.getTokenizedTextOfPosts());
        filteredHrefList = SupportFunctions.filteringHrefLists(bSoupProcessor.getAllHyperlinks());    
        fullHrefList = SupportFunctions.returnListWithLeadingStringInEachEntry(filteredHrefList,baseSearchUrl);
    
    urlLinksVisited.append(nextUrlLink);
    unvisitedHrefList = [x for x in fullHrefList if x not in urlLinksVisited];
    pendingUrlLinks = list(set(pendingUrlLinks+unvisitedHrefList));    
    
    print 'end reached of one url'
    print len(urlLinksVisited);
    print len(unvisitedHrefList);
    print len(pendingUrlLinks);
    if (len(urlLinksVisited) > 10):
        moreToGo = False;
    elif (len(pendingUrlLinks)>0):
        nextUrlLink = pendingUrlLinks.pop(0);
    else:
        moreToGo = False;
    
#     for aLink in pendingUrlLinks:
#         aLink = aLink +'\n'
#         debugPrinter.addMessageToDebugOutput(aLink);
                        
    #determine if moreToGo?and find the nextUrlLink and set it.
    
    time.sleep(interRequestDelay);#necessary for robots/agents
#=====================END MAIN WHILE LOOP

''' Great we have all the tokens, now make the nltk text
'''

asciiPostTokens = [];
for postToken in allPostTokens:
    postToken = postToken.encode('ascii','ignore');
    asciiPostTokens.append(postToken);

postsNltkText = nltk.Text(asciiPostTokens);
print postsNltkText.concordance('pendant');

debugPrinter.addMessageToDebugOutput(" ".join(asciiPostTokens));
print "testing branch"




