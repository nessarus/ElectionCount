##    Name:             Joshua Ng
##    Student Number:   20163079
##    version:          18/5/2017

##    project2.py is a program to be used to decide an election for a single 
##    seat under the Preferential Voting system used in the Western 
##    Australia Legislative Assembly (the Lower House).

import os.path

##    getCandidates(f) returns a list containing the candidates' names from 
##    the file f.The names will be one per line with no extraneous 
##    characters. Disregard any blanklines in f. If f doesn't exist, it prints
##    an error message and return an empty list. For example, 
##    getCandidates("candidates.txt") = ["Major Clanger", "Soup Dragon", 
##    "Froglet", "Iron Chicken", "The Cloud"].
##    >>> getCandidates(f) returns ["Major Clanger", "...], || print(error), []
def getCandidates(f):
    candidates = []
    if os.path.isfile(f):
        file_f = open(f, "r")
        for names in file_f:
            if names not in ['\n', '\r\n']:
                candidates.append(names.strip())
        file_f.close()
    else:
        print("file doesn't exist")
    return candidates

##    storeCandidateData returns a dictionary assigning 1,2,3,...etc to
##    each Candidates' data.
##    e.g. storeCandidateData(["Major Clanger", "...]) returns
##    [(1, 'Major Clanger'), (2, ...]
def storeCandidateData(candidates):
    data = {}
    for i in range(0, len(candidates)):
        data[i+1] = candidates[i]
    return data

##    parseVote(s, option) returns the vote from s. option enables
##    Optional Preferential Voting.
##    Return 0 for an empty vote (Optional Preferential Voting). 
##    Returns -1 if there are any non-digits. 
##    e.g. 	parseVote("15") = parseVote(" 15 ") = 15. 
##            parseVote("", True) = parseVote(" ", True) = 0, 
##            parseVote("", False) = parseVote("no") = parseVote("1 5") = -1,
def parseVote(s, option=False): 
    vote = s.strip()
    if (vote == "") & option:
        return 0
    elif not vote.isdigit():
        return -1
    else:
        return int(s)

##    parsePaper(s, n) returns the votes from the ballot paper s in an 
##    election with n candidates, plus an error message. option enables
##    Optional Preferential Voting.
##    If s is formal, it returns the list of numbers found in s and the empty 
##    string. If s is informal, return an empty list of numbers and the
##    appropriate string below. 
##    i.e. parsePaper("3, 1, 2", 3) = ([3, 1, 2], "")
##    i.e. parsePaper(", , ,", 4) = parsePaper("0, 0", 4) = ([ ], "blank"),
##    i.e. parsePaper("3, -8, 1", 3) = parsePaper("3, 1.8, 2", 3) = parsePaper
##    ("pointless, 2, 1", 1) = ([ ], "non-digits"),
##    i.e. parsePaper("1,2,3,4,5", 4) = ([ ], "too long"),
##    i.e. parsePaper("6,1,2,3,4",5) = ([ ], "out of bounds")
##    i.e. parsePaper("1, 1", 2) = ([ ], "duplicate")
##    i.e parsePaper("1, , , ", 4, True) = ([1, 0, 0, 0], "")
##
##    parsePaper(s,n): >> ([14, 0, 2], ""), >> ([ ], "blank"), 
##                     >> ([ ], "non-digits"), >> ([ ], "too long")
##                     >> ([ ], "too large"), >> ([ ], "duplicate")
def parsePaper(s, n, option=False): 
    ballot = s.split(",")
    len_ballot = len(ballot)
    votes = []
    blank_vote = 0
    
    if len_ballot > n:
        return ([], "too long")
    
    for vote in ballot:
        parse_vote = parseVote(vote) #parseVote(s): " " >> 0, "no" >> -1, "9" >> 9
        if parse_vote == -1:
            return ([], "non-digits")
        elif parse_vote == 0:
            blank_vote+=1
            votes.append(0)
        else:
            votes.append(parse_vote)

    if blank_vote == len_ballot:
        return ([], "blank")
    
    return (votes, "")




        