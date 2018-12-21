ElectionCount is a program to be used to decide an election for a single 
seat under the Preferential Voting system used in the Western 
Australia Legislative Assembly (the Lower House).

*How to run:*
In your own python program:

```python
import ElectionCount

ElectionCount.main(candidates_file_name, ballots_file_name, optional)
```

* candidates_file_name: address to a text file with the candidates' names 
each separted with a new line.
* ballots_file_name: address to a text file with numbered preferences. 
1 being the highest preference in order of candidates, separated with a 
comma per preference and new line per vote.
* optional: set to true to enable preferential voting
