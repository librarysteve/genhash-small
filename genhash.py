#!/usr/bin/env python
import hashlib
import sys
ALGOS = hashlib.algorithms_available

if sys.argv[1] == '-l':
    print(ALGOS)
    sys.exit()
elif len(sys.argv) < 3 or sys.argv[1] == '-h' or sys.argv[2] not in ALGOS:
    print('Usage: smallhash plaintext hashtype')
    print('-h for help\n-l to list available hashes')
    sys.exit()
else:
    plainText = sys.argv[1]
    hashType = sys.argv[2]
    hashText = hashlib.new(hashType, plainText.encode('utf8')).hexdigest()
    print(hashText)
    sys.exit()
