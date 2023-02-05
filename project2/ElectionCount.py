"""
Name:             Joshua Ng
Student Number:   20163079
version:          28/01/2023

ElectionCount is a program to be used to decide an election for a single
seat under the Preferential Voting system used in the Western
Australia Legislative Assembly (the Lower House).
"""
import os.path


def get_candidates(candidates_filename):
    """
    Gets a list containing the candidates' names from the file.

    Candidate file format:
    * If f doesn't exist an error message is printed.
    * One name per line.
    * No extraneous characters.
    * Disregard blank lines.

    :param candidates_filename: The file name containing the candidate names.
    :return:                    A list of candidate names.
    """
    if os.path.isfile(candidates_filename):
        with open(candidates_filename, "r") as file_f:
            return [name.strip() for name in file_f]

    print("File does not exist.")
    return []


def parse_vote(token, option=False):
    """
    Parses the numbered preferences. Option enables preferential voting.
    Return 0 for an empty vote (optional preferential voting).

    e.g.    parse_vote("15") = parseVote(" 15 ") = 15.
            parse_vote("", True) = parseVote(" ", True) = 0,
            parse_vote("", False) = parseVote("no") = parseVote("1 5") = -1

    :param token:   The token to be parsed.
    :param option:  True if optional preferential voting is enabled.
    :return:        The parsed vote. Returns -1 if there are any non-digits.
    """
    token = token.strip()

    if token:
        if token.isdigit():
            vote = int(token)
            if vote or option:
                return vote
    elif option:
        return 0

    return -1


def parse_paper(paper, number_of_candidates, option=False):
    """
    Parses the votes from the ballot paper together with error status.
    option enables preferential voting.

    i.e. ("3, 1, 2", 3)                     >> ([3, 1, 2], "")
    i.e. (", , ,", 4), ("0, 0", 4)          >> ([], "blank"),
    i.e. ("3, -8, 1", 3), ("3, 1.8, 2", 3)  >> ([], "non-digits"),
    i.e. ("1, 2, 3, 4, 5", 4)               >> ([], "too long"),
    i.e. ("6, 1, 2, 3, 4", 5)               >> ([], "too high")
    i.e. ("1, 1", 2)                        >> ([], "duplicate")
    i.e. ("1, , , ", 4, True)               >> ([1], "")

    :param paper:                   The paper to be parsed.
    :param number_of_candidates:    The number of candidates.
    :param option:                  Enables preferential votes.
    :return:    Formal papers returns a list of votes and the empty string.
                Informal papers return an empty list and an error message.
    """
    votes = [parse_vote(token, option) for token in paper.split(",")]

    if len(votes) > number_of_candidates:
        return [], "too long"

    unique_votes = set()
    blank_paper = True

    for vote in votes:
        if vote == -1:
            return [], "non-digits"

        if vote > number_of_candidates:
            return [], "too high"

        if vote != 0 and vote in unique_votes:
            return [], "duplicate"

        unique_votes.add(vote)

        if vote != 0:
            blank_paper = False

    if blank_paper:
        return [], "blank"

    return votes, ""


def get_papers(file, number_of_candidates, option=False):
    """
    Gets the ballot papers from the file f.
    Each line of the file is treated as a separate paper.
    If f doesn't exist, it will print error message and return the empty list.
    option enables preferential voting.

    For example:
    getPapers("smallfile.txt", 4) = [[1, 2, 3, 4], [1, 3, 2, 4]...
    getPapers("smallfile.txt", 4, True) = [[3,2,1], [...

    :param file:                    The ballot paper file.
    :param number_of_candidates:    The number of the candidates.
    :param option:                  Set true to enable preferential voting.
    :return:                        A list of parsed papers.
    """
    papers = []
    errors = []

    if os.path.isfile(file):
        file_f = open(file, "r")

        for line in file_f:
            paper, error = parse_paper(line, number_of_candidates, option)

            if error:
                errors.append(error)
                continue

            papers.append(paper)

        file_f.close()
    else:
        print("file doesn't exist")

    return papers, errors


def ordered_paper(paper):
    """
    Creates a list of candidates in voter's preferred order.
    The list is ordered from most preferred to least.

    For example:
    [2,4,5,3,1]                 >> [4,0,3,1,2]
    [4,5,0,3,1]                 >> [4,3,0,1]

    :param paper:   The list of the voter’s candidate preferences.
    :return:        A list of candidates in order of the voter's preference.
    """
    preferences = [(preference, index) for index, preference in enumerate(paper) if preference]
    preferences.sort()
    ordered = [index for preference, index in preferences]
    return ordered


def ordered_papers(papers):
    """
    Creates a list of ordered papers.
    
    For example:
    [[2,4,5,3,1], [4,5,0,3,1]]      >>  [[4, 0, 3, 1, 2], [4, 3, 0, 1]]

    :param papers:      A list of ballot papers.
    :return:            A list of ordered papers
    """
    papers = [ordered_paper(paper) for paper in papers]
    return papers


def count_votes(candidates, totals, papers):
    """
    Tallies and sets the ballot papers into the respective candidates
    For example:
    candidates  = {0: [], 1:[], 2:[], 3:[], 4:[]}
    totals      = {0:0, 1:0, 2:0, 3:0, 4:0}
    papers      = [[0,2,3,4,1], [3,1,3,2,0]]
    candidates  >> {0: [[0, 2, 3, 4, 1]], 1: [], 2: [], 3: [[3, 1, 4, 2, 0]], 4: []}

    :param candidates:  A dictionary of candidates and their ballot papers.
    :param totals:      A dictionary of candidates and their total votes.
    :param papers:      A list of voter papers.
    """
    for paper in papers:
        paper = [vote for vote in paper if vote in candidates]
        if paper:
            candidates[paper[0]].append(paper)

    for candidate, candidate_papers in candidates.items():
        totals[candidate] = len(candidate_papers)


def print_count(totals, names):
    """
    Displays the total tally of votes for each candidate.

    :param totals:              A dictionary of candidates and their total votes.
    :param names:               The candidates' names.
    """
    count = list(totals.items())
    count.sort(key=lambda item: item[1], reverse=True)
    count = ["{0}\t{1}".format(total, names[candidate]) for candidate, total in count]
    print(*count, sep="\n")
    print()


def print_candidate(name, win):
    """
    Prints the winner or the eliminated candidates.
    :param name:    The candidates' names.
    :param win:     Print if the candidate won the election.
    """
    if win:
        print("Candidate {} is elected".format(name))
    else:
        print("Candidate {} has the smallest number of votes and is "
              "eliminated from the count\n".format(name))


def main(candidates_filename, ballots_filename, optional=False):
    """
    Handles processing an election count request.

    :param candidates_filename:     The candidate filename.
    :param ballots_filename:        The ballot filename.
    :param optional:                Enable preferential voting.
    """
    # get candidates
    names = get_candidates(candidates_filename)

    if not names:
        print("no candidates")
        return
    
    number_of_candidates = len(names)

    # get papers
    papers, errors = get_papers(ballots_filename, number_of_candidates, optional)

    if not papers:
        print("no votes")
        return

    # count votes
    papers = ordered_papers(papers)
    candidates = {index: [] for index, name in enumerate(names)}
    totals = {candidate: 0 for candidate in candidates}
    count = 1

    while len(papers) > 0:
        print("Count {}".format(count))
        count_votes(candidates, totals, papers)
        print_count(totals, names)

        # Check if candidate has <50% of eligible votes.
        total_votes = sum([len(papers) for candidate, papers in candidates.items()])
        highest = max(totals, key=totals.get)

        if totals[highest] > total_votes // 2:
            print_candidate(names[highest], True)
            break

        # Find the lowest candidates
        lowest = min(totals, key=totals.get)
        lowest_total = totals[lowest]
        lowest = [candidate for candidate, total in totals.items() if total == lowest_total]

        # Check for a tie
        if len(totals) == len(lowest):
            for candidate, total in totals:
                print_candidate(names[candidate], True)
            break

        # Check if there are only two candidates.
        if len(totals) < 3:
            print_candidate(names[highest], True)
            break

        # Print eliminated candidates.
        for low in lowest:
            print_candidate(names[low], False)

        # Update pool of eligible votes to be recounted.
        papers = [paper for low in lowest for paper in candidates[low]]
        for low in lowest:
            candidates.pop(low)
            totals.pop(low)
        count += 1

    print("Number of informal votes {}.".format(len(errors)))


if __name__ == "__main__":
    main("candidates.txt", "papers2.txt", True)

