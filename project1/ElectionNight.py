"""
Name:               Joshua Ng
Student Number:     20163079
Version:            31/12/2022
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


def parse_vote(token):
    """
    Parses the numbered preferences.

    * Empty votes return 0. i.e. " ", "".
    * Non-digits return -1. i.e. "-3", "1 5" "not digits"
    :param token:   The string token to parse.
    :return:        An integer of the parsed vote.
    """
    token = token.strip()

    if not token:
        return 0

    if not token.isdigit():
        return -1

    return int(token)


def parse_paper(paper, number_of_candidates):
    """
    Parses a ballot paper's numbered preferences.

    Ballot paper's string format:
    * Comma separated integers
    * E.g. "14, 0, 2", "1, 2,, 4, 5".

    Error Messages:
    * "too long":   Number of preferences exceeds number of candidates.
    * "blank":      All zero or blank preferences.  E.g. ", , ", "0, 0", "0, "
    * "non-digits"  Use of negative or non-digits.  E.g. "pointless, 5, 5"

    :param paper:                   A string with the numbered preferences to be parsed.
    :param number_of_candidates:    The number of candidates.
    :return: If successful returns tuple of parsed ranked choices list and empty string.
             Otherwise, returns tuple of an empty list with an error message.
    """
    votes = [parse_vote(token) for token in paper.split(",")]

    if len(votes) > number_of_candidates:
        return [], "too long"

    if any(vote == -1 for vote in votes):
        return [], "non-digits"

    if all(vote == 0 for vote in votes):
        return [], "blank"

    return votes, ""


def get_papers(ballots_file, number_of_candidates):
    """
    Gets the ballot papers parsed from the file.

    Ballot paper format:
    * Each line is a separate ballot paper.

    :param ballots_file:            The file name of the file containing the ballot papers.
    :param number_of_candidates:    The number of candidates.
    :return:    A list of tuples with the parsed votes and its error status.
                If the file not found, an empty list is returned.
    """
    if os.path.isfile(ballots_file):
        with open(ballots_file, "r") as file_f:
            return [parse_paper(paper, number_of_candidates) for paper in file_f]

    print("File does not exist.")
    return []


def normalise_paper(paper, number_of_candidates):
    """
    Rescales the choice preferences to be normalised to a total of 1.
    List is padded with zeros in line with the number of candidates.
    For example:
    * normalise_paper([1,2,3,4], 4)     := [0.1, 0.2, 0.3, 0.4],
    * normalise_paper([2], 3)           := [1.0, 0.0, 0.0],
    * normalise_paper([0, 4, 496], 3)   := [0.000, 0.008, 0.992]
    :param paper:                   A string with the numbered preferences to be parsed.
    :param number_of_candidates:    The number of candidates.
    :return:    A list of normalised choice preferences.
    """
    total = sum(paper)
    papers = [float(vote)/total for vote in paper]

    for i in range(len(papers), number_of_candidates):
        papers.append(0.0)

    return papers


def normalise_papers(papers, number_of_candidates):
    """
    Normalises a list of ballot papers.
    E.g. normalise_papers([[2], [7, 2, 1]], 3) = [[1.0, 0.0, 0.0], [0.7, 0.2, 0.1]].
    :param papers:                  The ballot papers to be normalises.
    :param number_of_candidates:    The number of candidates.
    :return:    A list of normalised ballot papers.
    """
    return [normalise_paper(paper, number_of_candidates) for paper in papers]


def count_votes(candidates, papers):
    """
    Counts the ballot papers for each candidate. A list of lists containing the counts for the candidates
    cs from the ballot papers ps, in descending order of total number of votes.
    For example, count_votes(["A", "B", "C"], [[0.5, 0.5, 0], [0.05, 0.3, 0.65]])
    = [[0.8, "B"], [0.65, "C"], [0.55, "A"]].
    :param candidates:  A list of candidates.
    :param papers:      A list of ballot papers.
    :return:    A list of candidates with their total number of votes.
    """
    results = [[sum(votes), candidates[index]] for index, votes in enumerate(list(zip(*papers)))]
    results.sort(reverse=True)
    return results


def print_count(results):
    """
    Displays the election count results.
    :param results:     The election count results.
    """
    for candidate in results:
        print(" {0:0.2f} {1}".format(candidate[0], candidate[1]))


def main():
    """
    Prompts the user for the names of the necessary files, then conducts the
    election.
    """
    candidates_file = str(input("Please enter the candidates’ filename: \n"))
    candidates = get_candidates(candidates_file)

    if not candidates:
        return

    number_of_candidates = len(candidates)

    papers_file = str(input("Please enter the ballot papers’ filename: \n"))
    papers = get_papers(papers_file, number_of_candidates)
    formal_papers = [paper for paper, error in papers if not error]

    normal_papers = normalise_papers(formal_papers, number_of_candidates)
    results = count_votes(candidates, normal_papers)

    number_formal = len(formal_papers)
    number_informal = len(papers) - number_formal


    print("Nerdvanian election 2017\n")
    print("There were {} informal votes".format(number_informal))
    print("There were {} formal votes\n".format(number_formal))
    print_count(results)


if __name__ == "__main__":
    main()
