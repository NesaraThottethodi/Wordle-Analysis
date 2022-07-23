def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def count_words(words):
    myLength = len(words)
    print("Analyzing list of : " + str(myLength) + " words.")

def word_length_distribution(words, LIMIT):
    counts = {}
    for i in range(1,LIMIT):
        counts[i] = 0
    counts[str(LIMIT)+"+"] = 0
    mySet = set()

    for n in words:
        letterCount = len(n)
        if(letterCount == 5):
            mySet.add(n)
        if letterCount >=LIMIT:
            letterCount = str(LIMIT) + "+"
        counts[letterCount] += 1

    for wordLength,count in counts.items():
        print("Words of length " + str(wordLength) + " : " + str(count))
    return mySet

def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)

def analyze_frequencies(words):
    frequency_table = {}
    for x in char_range('a', 'z'):
        frequency_table[x]=0
    for n in words:
        for c in n:
            frequency_table[c] += 1
    return frequency_table

def two_word_score(goldenword, word):
    assert len(word) == 5
    assert len(goldenword) == 5
    w = word
    g = goldenword
    exact_match_list = []
    inexact_match_list = []
    remainder = []
    for i in range(0,5):
        if (w[i] == g[i]):
            exact_match_list.append(i)
            g[i] = 0
        else:
            remainder.append(i)
    for i in remainder:
        if (w[i] in g):
            inexact_match_list.append(i)
            n = g.index(w[i])
            g[n] = 0
    return exact_match_list, inexact_match_list

if __name__ == '__main__':
    english_words = load_words()
    # demo print
    print('fate' in english_words)
    count_words(english_words)
    five_letter_words = word_length_distribution(english_words,20)
    print(len(five_letter_words))
    ftab = analyze_frequencies(five_letter_words)
    print(sorted(ftab.items(),key=lambda item : item[1],reverse=True ))
    print(two_word_score(list("sushi"), list("suhus")))