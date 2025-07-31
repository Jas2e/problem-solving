# Reverse Words in a String


# Problem Statement: Given a string s, reverse the words of the string.

# Examples:

# Example 1:
# Input: s=”this is an amazing program”
# Output: “program amazing an is this”

# Example 2:
# Input: s=”This is decent”
# Output: “decent is This”


def rev(s):
    s=s.strip() #Remove leading and tailing spaces
    s=' '.join(s.split()[::-1])

    return s


s="This is decent"

print(rev(s))


