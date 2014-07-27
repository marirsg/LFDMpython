'''
LFDM_bsoupProcessor: This class takes in the bsoup object of a lutron forum web page,
and processes it.

GOAL: BUILD DATA TO SHOW HOW KEYWORDS SHOW UP OVER TIME AND GEOGRAPHY

The current processing of a webpage will include

1) Process posts
    a) Meta data of the post
        i) The time+date of post   -> will be associated to the post data structure?
        ii) Who posted it.-> We will increment the "numberOfPosts" for the user's "profile object"(see below) 
                We will create a dictionary of users. Essentially an map, with username as key.
                The value will be a user object that will contain information about the user (for any further processing)
    b)Process the content of the post        
        i) Did it contain any keywords that we are currently using. HVAC, 3rd party integration,shades,etc.
            Need a separate dictionary of Lutron products
                HOW TO WRITE A NLTK DICTIONARY
        ii) DO LATER, Look for critical feedback, and save context where you find the words like [r'suck', r'horrible',
             USE NLTK for synonyms. Build map, key is the date/time, values are user and feedback object.
                    
'''

import types;
import os;
import time;
from urllib import urlopen;
import copy

from bs4 import BeautifulSoup as Bsoup;
import nltk;
from nltk import word_tokenize 


class LutronSoupProcessor:

    printingFunction = ""; #dummy placeholder    
    
    def __init__(self,bSoupObject,printerFunction):
        print "creating a Lfdm_bsoup_processor"
        self.bSoupObjectForProcessing = Bsoup(bSoupObject.prettify());
        self.bSoupOriginal =  Bsoup(bSoupObject.prettify());
        self.printingFunction = printerFunction;
        self.allPostTokens = [];
        self.processBsoup();
        
        
        
        
    def __del__(self):
        print "deleting a Lfdm_bsoup_processor"
        #do cleanup as this will be used in a thread
        
    def processBsoup(self):
        '''This will be called from the constructor immediately. It will parse the html file to extract data'''
        #find all the relevant post tags, and take the text or contents from within the tag.
        allPosts = self.bSoupOriginal.find_all("blockquote");
        #then use nltk to extract the text from the smaller string object containing all the text
        
        for singlePost in allPosts:
            postText = singlePost.get_text();
            tokenizedText = word_tokenize(postText);
            self.allPostTokens.extend(tokenizedText);
            self.allPostTokens.append("\n");            
         
#=============================================================================    
    def getAllHyperlinks(self):
        '''All the hyperlinks in the HTML file will be returned '''
        listOfHrefsToReturn = [];                        
        allHrefs = self.bSoupOriginal.find_all("a",href = True);        
        #extract the href content and append to a list
        for webLink in allHrefs:            
            listOfHrefsToReturn.append(webLink['href']);
        #self.printDebugInformation("whoot whoot! ");            
        return listOfHrefsToReturn;
#=============================================================================
    def getTokenizedTextOfPosts(self):
        return self.allPostTokens;    
#=============================================================================        
    def printDebugInformation(self,textPassedIn):
        '''imports the main file, just to access its debug printer variable, then
        uses it to print the debug information'''
        self.printingFunction(textPassedIn);
#=============================================================================
    
        
        