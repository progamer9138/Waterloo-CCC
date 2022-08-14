needle = input()
haystack = input()

# if the length of needle is longer than haystack, print 0
if len(needle) > len(haystack):
    print(0)
else:
    # find counts of each letter in the needle
    needle_counts = {}
    for letter in needle:
        if letter in needle_counts:
            needle_counts[letter] += 1
        else:
            needle_counts[letter] = 1

    results = set()
    counts = {}

    for i in range(len(needle)):
        if haystack[i] in counts:
            counts[haystack[i]] += 1
        else:
            counts[haystack[i]] = 1

    if counts == needle_counts:
        results.add(haystack[0:len(needle)])

    counts[haystack[0]] -= 1
    if counts[haystack[0]] == 0:
        del counts[haystack[0]]

    #count = 0

    # sliding window
    for i in range(1, len(haystack) - len(needle) + 1):
        if haystack[i+len(needle)-1] in counts:
            counts[haystack[i+len(needle)-1]] += 1
        else:
            counts[haystack[i+len(needle)-1]] = 1
        if counts == needle_counts:
            #count += 1
            results.add(haystack[i:i + len(needle)])
        counts[haystack[i]] -= 1
        if counts[haystack[i]] == 0:
            del counts[haystack[i]]

    print(len(results))