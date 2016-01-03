
import sys

if len(sys.argv) < 2:
    print 'Usage:   python unique_finder.py <filename>'
    print 'Example: python unique_finder.py ~/Downloads/file.txt'
    sys.exit()

from sets import Set
topics = Set()
file = open(sys.argv[1])
for line in file:
    for element in line.split(';'):
        topics.add(element.strip())

print sorted(topics)

