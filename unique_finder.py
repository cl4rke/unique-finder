
import sys

if len(sys.argv) < 2:
    print 'Usage:   python main.py <filename>'
    print 'Example: python main.py ~/Downloads/file.txt'
    sys.exit()

from sets import Set
topics = Set()
file = open(sys.argv[1])
for line in file:
    for element in line.split(';'):
        topics.add(element.strip())

print sorted(topics)

