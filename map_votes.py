import csv
import sys, codecs

sys.stdin = codecs.getreader("latin-1")(sys.stdin.detach())
for row in csv.reader(iter(sys.stdin.readline, ''), delimiter=';'):
    try:
        if row[11] == '3':
            print(row[13]+","+ row[14])
    except:
        continue
