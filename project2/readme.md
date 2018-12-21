ElectionCount is a program to be used to decide an election for a single 
seat under the Preferential Voting system used in the Western 
Australia Legislative Assembly (the Lower House).

**How to run:**  
In your own python program:

```python
import ElectionCount

ElectionCount.main(candidates_file_name, ballots_file_name, optional)
```

* candidates_file_name: address to a text file with the candidates' names 
each separted with a new line.
* ballots_file_name: address to a text file with numbered preferences. 
1 being the highest preference. File is read in order of candidates, 
separated with a comma per preference and new line per vote.
* optional: set to true to enable preferential voting

**Sample Input**
```python
import ElectionCount
ElectionCount.main("candidates.txt", "papers2.txt", True)
```  
  
**Sample Output**  
```
Count 1
8	Major Clanger
5	Soup Dragon
3	The Cloud
2	Froglet
1	Iron Chicken

Candidate Iron Chicken has the smallest number of votes and is eliminated from the count

Count 2
8	Major Clanger
5	Soup Dragon
4	The Cloud
2	Froglet

Candidate Froglet has the smallest number of votes and is eliminated from the count

Count 3
9	Major Clanger
6	Soup Dragon
4	The Cloud

Candidate The Cloud has the smallest number of votes and is eliminated from the count

Count 4
11	Major Clanger
8	Soup Dragon


Candidate Major Clanger is elected
```
