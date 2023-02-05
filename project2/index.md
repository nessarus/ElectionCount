# Project 2: Election Night Revisted – The Real Deal
You are to construct a Python program containing your solution to the problem described below. You must submit your program electronically using cssubmit. No other method of submission is allowed.

You are expected to have read and understood the University’s guidelines on academic conduct. In accordance with this policy, you may discuss with other students the general principles required to understand this project, but the work you submit must be the result of your own effort. Plagiarism detection, and other systems for detecting potential malpractice, will therefore be used. Besides, if what you submit is not your own work then you will have learnt little and will therefore, likely, fail the final exam.

You must submit your project before the submission deadline listed above. Following UWA policy, a late penalty of 5% will be deducted for each day (or part day), after the deadline, that the assignment is submitted. However, in order to facilitate marking of the assignments in a timely manner, no submissions will be allowed after 5 days following the deadline.

## Overview
In Project1, you were asked to create a Python program to decide a small election for the mythical country of Nerdvana. The method being used to decide that election was, essentially, first past the post voting. That is, the votes for each candidate are counted and the candidate with greatest number of votes wins the election. The only difference is that in the Nerdvana system the votes will be fractional.

For Project 2 you are to write a Python program to decide an election for a single seat under the Preferential Voting system used in the Western Australia Legislative Assembly (the Lower House). Similar systems are used for Lower House elections in most Australian states and for the House of Representatives in the Federal Parliament.

## Background
The conduct of elections in Western Australia is governed by the [Electoral Act of 1907](http://www8.austlii.edu.au/cgi-bin/viewdoc/au/legis/wa/consol_act/ea1907103/s144.html). However, unless you are REALLY keen, you are better off looking instead at the Wikipedia entry for [Instant Runoff Voting](https://en.wikipedia.org/wiki/Instant-runoff_voting#Australia). In Australia, the system is known as Preferential Voting. Optional Preferential Voting is a variant of Preferential Voting that will also be relevant to this Project.

The main thing you need to know is that under Preferential Voting, for a vote to be “formal” an elector has to number all of the squares corresponding to candidates on the ballot paper. Squares are to be numbered from 1, corresponding to the most favoured candidate, followed by 2, for the next most favoured candidate, then 3 for the next most preferred after that, and so on, until all the squares are numbered. No number can be missed out. Thus, if there are 5 candidates, all of the numbers from 1 to 5 must be used (once only!). No other marks are allowed, e.g. ticks, crosses or other letters/symbols.

## Deciding the Election
The following algorithm is used to decide who has won the election. The number of papers remaining after informal votes have been removed is the pool of “elegible votes”.

1. In the first step, the first preferences from all the votes are counted. If a candidate secures an absolute majority (i.e. minimum 50% of the elegible votes, plus 1) of the eligible votes, that candidate is declared elected and no further counting is done.
2. If no candidate has secured an absolute majority, the candidate with smallest tally is eliminated from further counting, and that candidate’s second preferences are added to the counts of the remaining candidates.
3. If a candidate now has an absolute majority the votes, that candidate is declared elected. Otherwise, Step 2 is repeated: The candidate with smallest number of votes is eliminated and the next-preference votes redistributed among the remaining candidates. That is, for each vote associated with the eliminated candidate the current top preference (for the eliminated candidate) is removed and the next preference is instead associated with the next most favoured candidate. However, if the next most favoured candidate has also been eliminated, the preference is popped and the preference after that should be used, and so on. If all the preferences for a papers have been used, the vote is regarded as “spent”, and discarded.
4. In the event of a tie for smallest count, the Act provides for the Returning Officer, i.e. person in charge of the count, to, first, recount and then, if the tie remains, to make a random choice among the candidates who have equal smallest counts. For this Project, however, please choose for elimination the candidate nearest the top of the list of candidates. (This provides reproducible behaviour when testing.)

## Optional Preferential
Optional Preferential Voting is to also be modelled in this Project. Optional Preferential Voting is simply the voting method that allows incomplete ballots to be accepted, so long as at least one candidate receives a vote. In other words, if there are 5 candidates in the election for a seat, an elector can number, say, 3 squares, so long as no two squares have the same number and no numbers from 1 to 3 are missing. Note that with optional preferential, it is possible that, when it comes down to the final two candidates, neither may have more than 50% of the eligible votes, so the candidate with the greater number of votes is declared elected.

## Your Program
* Your program must contain a definition for the function `main`, starting with: `def main(candidates_file_name, ballots_file_name, optional=False):`
As in Project1, `main` will be used to call your code during automated testing. However, in this case, the call to `main` will also be used to provide the file-name for the file of candidates names and the file-name of the file of ballots. **Your program should therefore NOT call `input()`.**
* The file containing names of candidates is exactly as per Project1: one name per line.
* The votes, i.e. papers, will be in a comma separated file, e.g.`1,3,4,5,2` indicating that Candidate 1 has the first preference, Candidate 5 has the second preference, Candidate 2 has the third preference, etc. Other lines will look like:  
`2,1,3,5,4`  
`1,3,4,5,2`  
`3,5,2,4,1`  
`1,4,5,2,3`  
If optional preferential voting is allowed, these votes are also formal:  
`2,1,3,,`  
`,2,1,,3`  
* After the winner has been declared, there must also be a statement about the number of informal votes

## Sample files
At the start of the semester (prior to the recent WA election) I wrote to the Western Ausralian Electoral Commission and was promised files containing votes from a real election once the processing of the election had completed, but thus far they have not arrived. When they arrive, I shall make them available here. In the meantime, here is a sample candidates file (will look rather familiar) and a sample set of ballot papers. The output of your program should look like this.

## Submission
Submit a **single .py file** containing all of your functions via cssubmit.

## Assessment
Your submission will be assessed on

How your program performs over a series of input-output tests.
clarity: whether your code is clear to read and well-constructed.