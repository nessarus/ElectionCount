"""
Short test file for Project 1, Election Night. 

We do not claim that this file is a complete testing scheme: 
its primary purpose is to check the spelling of the function names. 
You should supplement the tests in this file with your own tests. 
The correctness of your program is your responsibility. 

Author: Lyndon While 
Date: 3/4/14
Version 1.15 
"""
import ElectionNight as Project1
import os.path


# A non-existent file
nonfile = "nofile.txt"


def hackb(xs):
    if xs == [] or xs[-1][1] != "blank":
        return xs
    else:
        return xs[:-1]


def test_get_candidates():
    f = "candidates.txt"
    if os.path.exists(f):
        return [(Project1.get_candidates(x), y) for (x, y) in
                [(f, ["Major Clanger", "Soup Dragon", "Froglet", "Iron Chicken", "The Cloud"])
                , (nonfile, [])]]
    else:
        print("You need to download file", f, end="\n\n")
        return [] 


def test_parse_vote():
    return [(Project1.parse_vote(x), y) for (x, y) in
            [("", 0), ("no", -1), ("27", 27)]]


def test_parse_paper():
    return [(Project1.parse_paper(x, y), z) for (x, y, z) in
            [(",,, ",      4, ([],         "blank"))
            ,("  3,4,5  ", 2, ([],         "too long"))
            ,("4,-4,4",    3, ([],         "non-digits"))
            ,("4,5, 16",   6, ([4, 5, 16], ""))
            ,("9876",      8, ([9876],     ""))]]


def test_get_papers():
    f = "smallfile.txt"
    if os.path.exists(f):
        nd = ([], "non-digits")
        b  = ([], "blank")
        tl = ([], "too long")
        return [(hackb(Project1.get_papers(x, 4)), y) for (x, y) in
                [(f, [([1,2,3,4], ""), b, ([0,23,0], ""), nd, nd, ([4,0,4,4], ""), tl])
                ,(nonfile, [])]]
    else:
        print("You need to download file", f, end = "\n\n")
        return []


def test_normalise_paper():
    return [(Project1.normalise_paper(x, y), z) for (x, y, z) in
            [([2,1,5], 3, [0.25, 0.125, 0.625])
            ,([8,2],   4, [0.8,  0.2,   0,    0])
            ,([7],     4, [1,    0,     0,    0])]]


def test_normalise_papers():
    return [(Project1.normalise_papers(x, y), z) for (x, y, z) in
            [([[2,1,5], [8,2]], 3, [[0.25,0.125,0.625], [0.8,0.2,0]])]]


def test_count_votes():
    return [(Project1.count_votes(cs, ps), x) for (cs, ps, x) in
            [(["A", "B", "C"], [[0,0,1], [0,1,0], [0,0,1]], [[2,   "C"], [1,   "B"], [0,   "A"]])
            ,(["A", "B", "C"], [[0.7, 0.2, 0.1]],           [[0.7, "A"], [0.2, "B"], [0.1, "C"]])]]


def test_print_count():
    return []


def test_main():
    return []


def msg(f, z):
    bs = [x == y for (x, y) in z]
    if bs == []:
        s = "untested"
    elif all(bs):
        s = "all " + str(len(bs)) + " test(s) correct"
    else:
        zs = [k for k in range(len(bs)) if not bs[k]]
        s = "These tests incorrect: " + str(zs)[1:-1]
    print("%20s" % (f + ":"), s)


msg("get_candidates",   test_get_candidates())
msg("parse_vote",       test_parse_vote())
msg("parse_paper",      test_parse_paper())
msg("get_papers",       test_get_papers())
msg("normalise_paper",  test_normalise_paper())
msg("normalise_papers", test_normalise_papers())
msg("count_votes",      test_count_votes())
msg("print_count",      test_print_count())
msg("main",             test_main())
print()
input("Hit Enter to finish: ")
