'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC      
    # Base Case to check if no word

    if (len(word) == 0): 
        return 0 
    
    # check if the first two letters in the word contains 'th' compare the next pair recursively
    elif word[:2] == "th":
        return count_th(word[1:]) + 1

    # continue recursively till base case is evoked.
    else: 
        return count_th(word[1:])
