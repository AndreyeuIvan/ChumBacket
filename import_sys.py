import sys

#sys.stderr.write('This is stderr text\n')
#sys.stderr.flush()
#sys.stdout.write('This is stdout text\n')

#print(sys.argv)

if len(sys.argv) > 0:
    print(int(sys.argv[0]+5))
