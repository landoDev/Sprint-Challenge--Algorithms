'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # base case, out of letters to match 
    # there can't be a match cuz we are looking for 2 letters   
    if len(word) < 2:
        return 0 
    else:
        # crawl through the word to the next two and check again
        # recursively call the list excluding the last two, makes the array smaller
        if word[:2] == "th":
            return 1 + count_th(word[2:])
        # if there isnt a match, move over a single letter and check again
        else:
            return count_th(word[1:])
