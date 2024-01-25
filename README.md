# genhash-small
Hash generation in less than 20 lines of python

Program Breakdown:
```python
#!/usr/bin/env python
# import needed modules
import hashlib
import sys
# create a global variable for the set of hashtypes
ALGOS = hashlib.algorithms_available

# if the -l argument is passed list the available hash types
if sys.argv[1] == '-l':
    print(ALGOS)
    sys.exit()
# if you don't pass required arguments or use the -h argument for help
# print the help message
elif len(sys.argv) < 3 or sys.argv[1] == '-h' or sys.argv[2] not in ALGOS:
    print('Usage: smallhash plaintext hashtype')
    print('-h for help\n-l to list available hashes')
    sys.exit()
# main
else:
    # assign arguments 1 and 2 to variables
    plainText = sys.argv[1]
    hashType = sys.argv[2]
    # create an object of hashText and assign it a value of the hashlib.new fiction
    # pass the hashlib fuction the hashType and plantext encoded in utf8
    # hash the plaintext and return hex as opposed to bytes
    hashText = hashlib.new(hashType, plainText.encode('utf8')).hexdigest()
    # print the hash to std out
    print(hashText)
    sys.exit()
```
