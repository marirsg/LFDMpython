'''
List of functions designed to help the main code and classes, like functions to output
debugging data and order of events
'''

import os;
import time;
import re;

g_debugOutTxtLocation = "\\Debugging1.txt";

class DebugOutput:

    def __init__(self):        
        currentFileDirectory = os.path.dirname(os.path.realpath(__file__));        
        try:
            debugFileLocation = currentFileDirectory + g_debugOutTxtLocation;        
            self.debugFileHandle = open(debugFileLocation, "w");              
        except IOError:
            print "The debug File location was incorrect or is not working";
        except Exception as mistake:
            print mistake;
#========end init

    def __del__(self):
        self.debugFileHandle.flush();
        self.debugFileHandle.close();
    
#========end del

    def addMessageToDebugOutput(self, debugMessage):        
        try:            
            self.debugFileHandle.write(debugMessage);
            self.debugFileHandle.flush();        
        except IOError:
            print "The debug File location was incorrect or is not working";
        except Exception as mistake:
            print mistake;
    
#=========end function addMessageToDebugOutput =============================

#=========end class debug output =====================================


def filteringHrefLists(hrefList):
    filteredHrefList = [];
    for href in hrefList:
        if regexEvaluationOfSingleHref(href):                   
            filteredHrefList.append(href);#only insert those that have atleast one "\" in them
    return filteredHrefList;

def returnListWithLeadingStringInEachEntry(inputList,leadingString):
    returnList = [];
    for entry in inputList:
        entry = leadingString + entry
        returnList.append(entry);
    return returnList;

def regexEvaluationOfSingleHref(inputHref):
    '''
        remove links that do not have atleast one "/" 
        or start with "member". Not visiting member pages for now    
    '''
    if len(re.findall(r'(.+)/(.+)',inputHref)) > 0 and not \
            len((re.findall(r'member',inputHref))) > 0 and \
            len(re.findall(r'(.+)\.php(.*)',inputHref))>0 and \
            len(re.findall(r'^http.*$',inputHref)) == 0:                 
         return True;
    else:        
        return False;
