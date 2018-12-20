Definition of a vote

Each voter casts one ballot paper in which they can assign any non-negative number of votes to each candidate. Each ballot paper is normalised to a value of 1 before being counted: so given four candidates, the ballot paper 

5, 0, 8, 7 

would be normalised to 

0.25, 0.00, 0.40, 0.35

Example ballot papers

Assume an election with four candidates. The votes for the candidates are separated by commas, and if there are fewer than four votes, the paper is (notionally) padded with zeroes. Each of the following papers is formal and is interpreted as stated. 

Formal votes:

"3, 5, 0, 2" normalises to [0.3, 0.5, 0.0, 0.2].
"3, 5, 0" normalises to [0.375, 0.625, 0.000, 0.000].
"3, 5" normalises to [0.375, 0.625, 0.000, 0.000].
"3" normalises to [1.0, 0.0, 0.0, 0.0].
",3, 5" normalises to [0.000, 0.375, 0.625, 0.000].
",3,, 5" normalises to [0.000, 0.375, 0.000, 0.625].
" ,, , 3" normalises to [0.0, 0.0, 0.0, 1.0].
Informal votes:
With n candidates, any paper containing more than n votes is informal.
Any paper casting no votes is informal, e.g.
""
","
"0,0,0,0"
Any paper without proper separators (i.e. commas) is informal, e.g. "1 2".
Negative votes are not allowed, e.g. "5, -6, 4" is informal.
Floating point votes are not allowed, e.g. "5, 6.7, 4" is informal.
Any paper containing anything other than whitespace, digits, and commas is informal.