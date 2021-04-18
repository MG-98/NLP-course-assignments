import numpy as np


def Edit_distance(word1, word2, m, n):
    """
    This function build a table of the edit distance of the two strings
    :param word1: first word (misspelled word)
    :param word2: second word (true word)
    :param m: length of the first string
    :param n: length of the second string
    :return: Table of distances
    """
    distancetable = np.zeros((m + 1, n + 1))
    distancetable[0,:] = range(n+1) # string vs. space ==> import string
    distancetable[:,0] = range(m+1) # space vs. string ==> remove string

    for i in range(1,m + 1):
        for j in range(1, n + 1):

            # If last characters are same, no need for action
            if word1[i - 1] == word2[j - 1]:
                distancetable[i][j] = distancetable[i - 1][j - 1]

            # If last character are different, proceed with the minimum action value
            else:
                distancetable[i][j] = 1 + min(distancetable[i][j - 1],  # Insert
                                              distancetable[i - 1][j],  # Remove
                                              distancetable[i - 1][j - 1]+1)  # Replace
    return distancetable[m][n]


