import sys

votes_count = {}

for line in sys.stdin:

    candidate, count = line.split(',')
    count = int(count)

    try:
        votes_count[candidate] = votes_count[candidate]+count
    except:
        votes_count[candidate] = count

for candidate in votes_count.keys():
    print(str(candidate)+" "+str(votes_count[candidate]))
