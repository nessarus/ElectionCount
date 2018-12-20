import os.path

def getCandidates(f):
    candidates = []
    if os.path.isfile(f):
        infile = open(f, "r")
        for line in infile.readlines():
            if line not in ['\n', '\r\n']:
                candidates.append(line.strip())
        infile.close()
    else:
        print("file doesn't exist")
    return candidates

# returns the vote from s: parseVote("15") = parseVote(" 15 ") = 15.
# return 0 for an empty vote i.e. parseVote("") = parseVote(" ") = 0,
#-1 if there are any non-digits i.e. parseVote("-3") = parseVote("no") = parseVote("1 5") = -1,
def parseVote(s):
    s.strip()
    if s == "":
        return 0
    if s.isdigit():
        return int(s)
    return -1


# parsePaper(s, n) returns the votes from the ballot paper s in an
#    election with n candidates, plus an error message if appropriate.
# If s is formal, return the list of numbers found in s and the empty string.
#   i.e. parsePaper("14, , 2", 4) = ([14, 0, 2], "")
# If s is informal, return an empty list of numbers and the appropriate string below.
#   i.e. parsePaper(", , ", 4) = parsePaper("0, 0", 4) = ([ ], "blank"),
#   i.e. parsePaper("4, -8, 0", 4) = parsePaper("4, 7.8, 0", 4) = parsePaper("pointless,
#       5, 5", 4) = ([ ], "non-digits"),
#   i.e. parsePaper("1,2,,4,5", 4) = ([ ], "too long"). 
def parsePaper(s, n):
    #check if formal
    if isBlank(s, n):
        return ([], "blank")
    elif isNonDigits(s, n):
        return ([], "non-digits")
    elif isTooLong(s, n):
        return ([], "too long")
    else:
        return (s, "")

def isBlank(s, n):
    for vote in s.split(","):
        if vote.strip() != "":
            return false
    return true

def isNonDigits(s, n)
    




        