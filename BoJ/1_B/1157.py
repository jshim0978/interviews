from collections import Counter

s = str(input())


s = s.upper()

freq = Counter(s).most_common()

if len(freq) == 1:
    print(freq[0][0])
    quit()
else:

    if freq[0][1] == freq[1][1] and freq[0][0] != freq[1][0]:
        print('?')
    else:
        print(freq[0][0])

