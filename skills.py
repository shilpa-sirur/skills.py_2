# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(input_string):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of times
    that word appears in the string as values.


    For example:

        >>> print_dict(count_unique("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time:

        >>> print_dict(count_unique("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different:

        >>> print_dict(count_unique("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}

    """
    unique_words = {}

    for word in input_string.split():
        if word in unique_words:
            unique_words[word] += 1
        else:
            unique_words[word] = 1
    return unique_words 
       
def find_common_items(list1, list2):
    """Produce the set of common items in two lists.

    Given two lists, return a list of the common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    For example:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    If an item appears more than once in both lists, return it each
    time:

        >>> sorted(find_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 1, 2, 2]

    (And the order of which has the multiples shouldn't matter, either):

        >>> sorted(find_common_items([1, 1, 2, 2], [1, 2, 3, 4]))
        [1, 1, 2, 2]

    """

    new_list = []
    for i in range(len(list1)):
        for k in range(len(list2)):
	   if list1[i] == list2[k]:
				# print " The two numbers are common"
	       new_list.append(list2[k])
    return new_list


def find_unique_common_items(list1, list2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items shared between
    the lists.

    IMPORTANT: you may not not 'if ___ in ___' or the method 'index'.


    Just like `find_common_items`, this should find [1, 2]:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 2]))
        [1, 2]

    However, now we only want unique items, so for these lists, don't show
    more than 1 or 2 once:

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [1, 1, 2, 2]))
        [1, 2]

    """

    new_list = []
    for i in range(len(list1)):
        for k in range(len(list2)):
            if list1[i] == list2[k]:
                new_list.append(list2[k])
	for j in range(len(new_list) - 1):
            if new_list[j] == new_list[j+1]:
	       new_list.pop(j)
    return new_list


def get_sum_zero_pairs(input_list):
    """Given a list of numbers,
    return list of x,y number pair lists where x + y == 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.


    For example:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list:

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself):

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1, 0]) )
        [[-2, 2], [-1, 1], [0, 0]]

    """

    new_list = []
    abs_list=[]
    for i in range(len(input_list)):
        for k in range(len(input_list)):
	   sum = input_list[i] + input_list[k]
	   abs_sum = abs(input_list[i]) + abs(input_list[k])
    	   if (sum == 0 and input_list[i] <= 0):
    	       if abs_sum not in abs_list:
    	           new_list = new_list + [[input_list[i], input_list[k]]]
    	           abs_list.append(abs_sum)
    return new_list	
    
def remove_duplicates(words):
    """Given a list of words, return the list with duplicates removed
    without using a Python set.

    For example:

        >>> sorted(remove_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(remove_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

    """

    new_list = []
    for i in range(len(words)):
        if words[i] not in new_list:
	   new_list.append(words[i])	
    return new_list

def encode(phrase):
    """Given a phrase, replace all "e" characters with "p",
    replace "a" characters with "d", replace "t" characters with "o",
    and "i" characters with "u". Return the encoded string.

    For example:

        >>> encode("You are a beautiful, talented, brilliant, powerful musk ox.")
        'You drp d bpduouful, odlpnopd, brulludno, powprful musk ox.'
    """
    output=""
    for i in phrase:
        output=phrase.replace("e", "p").replace("a", "d").replace("t", "o").replace("i", "u")
    return output



def sort_by_word_length(words):
    output=[]
    wordlist=[]
    mylist=sorted(words,key=len)
    newwordlength=0
    for i in range(len(mylist)):
        wordlength=len(mylist[i])
        if i < len(mylist) -1:
            newwordlength=len(mylist[i+1])
            newwordpos=i+1
            wordlist.append(mylist[i])
        else:
            wordlist.append(mylist[i])
            t = tuple( [wordlength,wordlist])
            output.append(t)

        if wordlength != newwordlength:
				#wordlist.append(mylist[newwordpos])    
            t = tuple( [wordlength,wordlist])
            output.append(t)
            wordlist=[]
    return output



def get_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak equivalent.
    Words that cannot be translated into Pirate-speak should pass through
    unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    madam       proud beauty
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    lawyer      foul blaggart
    the         th'
    restroom    head
    my          me
    hello       avast
    is          be
    man         matey

    For example:

        >>> get_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words:

        >>> get_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'

    """

    english_list_keys = ['sir','hotel','student','boy','madam','professor','restaurant','your,excuse','students','are','lawyer','the','restroom','my','hello','is','man']
    pirate_talk_list_values =['matey','fleabag in', 'swabbie','proud','beauty','foul blaggart','galley','yer','arr','swabbies','be','foul blaggart,th','head','me','avast','be','matey']    
    eng2pirate = {}
    output = phrase
    for i in range(len(english_list_keys)):
        eng2pirate[english_list_keys[i]] = pirate_talk_list_values[i]
    #print eng2pirate

    for k in phrase.rstrip().split():
        #print k

        if k in eng2pirate :
            x = eng2pirate[k]
            #print x

            output = output.replace(k,x)
    
    return output

#print get_pirate_talk("my student is not a man")            
#print get_pirate_talk("my student is not a man!")   
# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
    """Given an input string, return a list of letter(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the letters in the returned
    list should be alphabetical.

    For example:
        >>> adv_get_top_letter("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example:
        >>> adv_get_top_letter("Shake it off, shake it off. Shake it off, Shake it off.")
        ['f']

    Spaces do not count as letters.

    """

def adv_get_top_letter(input_string):
    list1 = list(input_string)
    print list1
    list2 = []
    max_count = 0
    for i in range(len(list1)):
        if list1[i] not in list2:
	   list2.append(list1[i])
    	   max_count += 1
    return list2

def adv_alpha_sort_by_word_length(words):
    """    
    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--a number that is a word-length,
    and the list of words of that word length. In addition to ordering
    the list by word length, order each sub-list of words alphabetically.
    Now try doing it with only one call to .sort() or sorted(). What does the
    optional "key" argument for .sort() and sorted() do?

    For example:

        >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

    """

    output=[]
    wordlist=[]
    mylist=sorted(words,key=len)
    newwordlength=0
    for i in range(len(mylist)):
        wordlength=len(mylist[i])
        if i < len(mylist) -1:
            newwordlength=len(mylist[i+1])
            newwordpos=i+1
            wordlist.append(mylist[i])
        else:
            wordlist.append(mylist[i])
            t = tuple( [wordlength,wordlist])
            output.append(t)

        if wordlength != newwordlength:
                #wordlist.append(mylist[newwordpos])    
            t = tuple( [wordlength,sorted(wordlist)])
            output.append(t)
            wordlist=[]
    return output

##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
