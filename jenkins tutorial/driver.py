import sys
from add import add

argnumbers = len(sys.argv) - 1

if argnumbers == 2 :
    print("")
    print("The result is " + str(add(sys.argv[1], sys.argv[2])))
    print("")
    sys.exit(0)

if argnumbers != 2 :
    print("")
    print("You entered " + str(argnumbers) + " value/s.")
    print("")