'''

NEXT STEP: 
            Compile information about each user

NEXT STEP:
           Find all text in a webpage,(not just posts), compile into a seperate NLTK text
             the latter can be used to compare results from the posts-only nltk text

NEXT STEP:
the list append is inserting a list into a list. you need to add only the elements.google it

HALF DONE STEP:
           Find all posts, append into one NLTK text
           seek <blockquote class="postcontent restore ">
   

DONE STEP: ignore hrefs that start with http, since you use the base url to append.

DONE STEP: "# add test for ascii characters only"
             urlopen function does not take unicode chars ? what !
    ANSWER: just generalize the try except to catch any exceptions
    
DONE STEP: JUST HIT f11, without "ctrl"  to run in debug mode
figure out python debugging process in eclipse    
    
DONE STEP: add some more filters    
    
DONE STEP: Filter the links to go through using some more criteria. READ THE LinKS FirST
            print into the debug printer !!!
    
DONE STEP: Write code to manage which pages have been visited and what is the next page to visit
            DONT process anything yet, just visit.
            
            

DONE STEP: web crawlers that already exist and see if you can use it !!
https://webarchive.jira.com/wiki/display/Heritrix/Heritrix;jsessionid=BFD261FA4A2F179FC97CCF9ED0279FFA
    
    ANS: Effort taken to learn it and use it, is large for this project. In future larger project,
    it would make more sense
            

DONE STEP: Why is debug printer global not accessible in bsoup processor.
            Also, when you include LFDM main in bsoup proc, why does it complain about the bsoup
            instantiation? Circular references ??
            
            ANS: Circular reference. 
            Solution: You can pass a specific object's function, as an argument. So give the 
            printing function to other classes.
            

DONE STEP: When returning hyperlinks, ignore those that dont have atleast one "\" in them.
         Those without, are usually links to home page, or search page. Write a support function
         to do this (outside the debug printer class), that uses regex
                     
DONE STEP: TEST IF THE LIST OF HREFS WAS RETURNED PROPERLY         

DONE STEP: in soup processor, complete function get all hyperlinks, to give to the main code for looping
            the links will be appended with the base website name, to get the full website link.
            Check if visited and then insert into sets to avoid duplication.

DONE STEP: print logging/debugging info to a text file in a folder. Allow for many text files
with names of the same format


//------------------------- DESIGN NOTES---------------------------

# what is the first iteration of lfdm
    # What does the lf contain
        # Sections for HWQS, HW, Ra2, Shades, LED , all products
 so there needs to be a start, and then biforcation hierarchy 
 avoid loops
        # Posts, keywords, dates+time, usernames. Build a database with all this info.
 All the data needs to be mapped/linked together. Similar to wordnets meronyms, and holonyms
        # Just general data gathering, not too website specific. Use NLTK to generate stats, collocations etc.
 AVOID LOGIN AND PASSWORD ROUTES ! (how to enter login and password in python -> Later)

Only notes:

To do

   1) loop through N = 50 urls
        
        WRITE bsoup processor to
        
            o) Before going into each thread, the precursor page has number of replies and views. That could be a
                POWERFUL indicator of interest
        
            a) Find posts in html, create posts object skeleton
            b) process meta data of posts and save in object. time date user.
            c) process content of posts and save content specifics
                i) determine what can be saved and useful for mining. 
                    WHAT STATISTICS 
            d) save data in .txt files (pseudo database)
                i) design schema
                ii) design folder hierarchy
                ii) test saving
   
   2) Implement multi-threading and understand how to share data across threads.
       Each Thread is a biforcation from a page. there is a fixed pool to draw threads from 
       Before each thread is assigned a new url, it checks a Set of "visited URLs", to avoid repeats
   
   3) Implement nltk processing for collocations,bigrams, words occuring only once, etc.
   
   4) Implement login and password access



'''