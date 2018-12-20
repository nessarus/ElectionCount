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

##    parsePaper(s, n, option) returns the votes from the ballot paper s in an 
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
##    i.e. parsePaper("6,1,2,3,4",5) = ([ ], "too high")
##    i.e. parsePaper("1, 1", 2) = ([ ], "duplicate")
##    i.e parsePaper("1, , , ", 4, True) = ([1], "")
##
##    parsePaper(s,n): >> ([3, 1, 2], ""), >> ([ ], "blank"), 
##                     >> ([ ], "non-digits"), >> ([ ], "too long")
##                     >> ([ ], "too high"), >> ([ ], "duplicate")
def parsePaper(s, n, option=False): 
    ballot = s.split(",")
    len_ballot = len(ballot)
    votes = []
    blank_vote = 0
    
    if len_ballot > n:
        return ([], "too long")
    
    for vote in ballot:
        parse_vote = parseVote(vote, option)
        if parse_vote == -1:
            return ([], "non-digits")
        elif parse_vote > n:
            return ([], "too high")
        elif parse_vote in votes:
            return ([], "duplicate")
        elif parse_vote == 0:
            blank_vote+=1
            votes.append(0)
        else:
            votes.append(parse_vote)

    if blank_vote == len_ballot:
        return ([], "blank")
    
    return (votes, "")

##    getPapers(f, n, option) returns a list containing the ballot papers from 
##    the file f, in  an election with n candidates. Each line of the file 
##    is treated as a separate paper. If f doesn't exist, it will print error 
##    message and return the empty list. option enables Optional Preferential
##    Voting. For example:
##    getPapers("smallfile.txt", 4) = [[1, 2, 3, 4], [1, 3, 2, 4]...
##    getPapers("smallfile.txt", 4, True) = [[3,2,1], [...
def getPapers(f, n, option=False):
    papers = []
    if os.path.isfile(f):
        file_f = open(f, "r")
        for line in file_f:
            paper = []
            paper = parsePaper(line, n, option)
            if paper[0] != []:
                papers.append(paper[0])
        file_f.close()
    else:
        print("file doesn't exist")
    return papers

##    orderedPaper(p) returns a list of candidates in order of the 
##    voter’s preferences. For example:
##    orderedPaper([2,4,5,3,1]) >> [5,1,4,2,3]
##    orderedPaper([4,5,0,3,1]) >> [5,4,1,2]
##    @param p is the list of the voter’s preferences
##    @returns list of candidates
def orderedPaper(p):
    ordered = []
    preferences = []
    
    for i in range(len(p)):
        if p[i] != 0:
            preferences.append((p[i],i))
    preferences.sort()

    for i in range(len(preferences)):
        ordered.append(preferences[i][1]+1)
    
    return ordered

##    orderedPapers(ps) returns an ordered list of papers, ps. E.g. 
##    orderedPapers([[2,4,5,3,1], [4,5,0,3,1]]) = [[5, 1, 4, 2, 3],
##    [5, 4, 1, 2]]
def orderedPapers(ps):
    papers = []
    for p in ps:
        papers.append(orderedPaper(p)) 
    return papers

##    countVotes(cs, cv, ps) updates the dictionary, cs, of candidates’ 
##    lists of votes with the ballot papers ps. The total votes for each
##    candidate, cv, will also be updated.
##    For example, a = {1: [], 2:[], 3:[], 4:[], 5:[]}
##    b = {1:0, 2:0, 3:0, 4:0, 5:0}
##    countVotes(a, b, [[1,3,4,5,2], [4,2,5,3,1]])
##    list(a.items()) = [(1, [[1, 3, 4, 5, 2]]), (2, []), (3, []), (4,
##    [[4, 2, 5, 3, 1]]), (5, [])]
def countVotes(cs, cv, ps): 
    for p in ps:
        while p != []:
            if not p[0] in cs:
                p.pop(0)
            else:
                cs[p[0]].append(p)
                break
    for c in cs:
        cv[c] = len(cs[c])

##    printCount(c, n, win) displays the election count c, i.e. the result
##    from countVotes.  win parameter determines if winner is printed.
##    n is the number of counts.
def printCount(c, n, win):
    print("Count {}".format(n))
    for i in range(len(c)):
        print("{0}     {1}".format(c[i][0], c[i][1]))
    print()
    if(win == False):
        print("Candidate {} has the smallest number of votes and is "
              "eliminated from the count".format(c[len(c)-1][1]))
        print()
    if(win == True):
        print("Candidate {} is elected".format(c[0][1]))
        

##    main will require the file-name for the file of candidates names 
##    and the file-name of the file of ballots option enables Optional 
##    Preferential Voting.
def main(candidates_file_name, ballots_file_name, optional=False):
    candidates = getCandidates(candidates_file_name)
    if candidates == []:
        print("no candidates")
        return
    number_candidates = len(candidates)
    candidate_names = storeCandidateData(candidates)
    candidate_voters = storeCandidateData([0]*number_candidates)
    candidate_total_votes = []
    for i in candidates:
        candidate_total_votes.append([i, 0])
    
    


    papers = getPapers(ballots_file_name, number_candidates, optional)
    if papers == []:
        print("no votes")
        return

main()

##    ordered_papers = orderedPapers(ps)
##    results = countVotes(candidates, normal_papers)
##
##    number_formal = len(formal_papers)
##    number_informal = len(papers) - number_formal
##        
##    print("Nerdvanian election 2017\n")
##    print("There were {0} informal votes".format(number_informal))
##    print("There were {0} formal votes\n".format(number_formal))
##    printCount(results)




        