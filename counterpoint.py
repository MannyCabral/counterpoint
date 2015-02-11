from random import choice

KEYS = ["Gb","G","G#",
        "Ab","A","A#",
        "Bb","B",
        "C","C#",
        "Db","D","D#",
        "Eb","E",
        "F","F#"]
ACCEPTABLE = (1,3,5,6)
REPEATABLE = (3,6)

"""
Depending on the key, certain fifth intervals are not 7 half notes apart,
so they aren't perfect 5ths and cannot be used in Species Counterpoint.
"""
def calculateTritoneIntervals(key):
    assert key in KEYS

    # TODO: FINISH THIS

"""
Adding the length of two intervals in Music Theory doesn't
work like how it does in normal math. Instead, the 1 acts like a 0.
So an interval of two is actually two notes right next ot each other.
Ex.
3 + 4 = 6
1 + 1 = 1
1 + 2 = 2

There's also a rollover when it gets to 8. So 8 and 1 are equivalent.
Ex.
1 + 8 = 1
3 + 7 = 2

To see this last one:
1 2 3 4 5 6 7 8 9
              1 2
"""
def addIntervals(i1,i2):
    newInterval = i1 + i2 - 1
    if (newInterval) > 7:
        return newInterval % 7
    else:
        return newInterval

"""
In Species Counterpoint, one of the rules is that an interval
between two instruments of 1 or 5 cannot be repeated, and an
interval of 3 or 6 can only be repeated once.
"""
def usesSameInterval(new,current,previous=None):
    assert len(new) == len(current)
    if previous != None:
        assert len(new) == len(previous)
        
    for i in xrange(len(new)):
        if new[i] in REPEATABLE:
            if previous != None and new[i] == current[i] == previous[i]:
                return True
        elif new[i] == current[i]:
            return True
    return False

"""
Returns list of all possible next vectors. Does not take into
account the possibility that this may be a dead end.
"""
def getNextVectors(vector, prevVector=None):
    nextVectors = []

    for nextVector in Vectors:
        if not usesSameInterval(nextVector,vector,prevVector):
            nextVectors += [nextVector]
    return nextVectors

"""
Creates a single random set of intervals that satisfies Species
Counterpoint rules.
"""
# TODO: Convert to notes instead of intervals
def generateMeasures(measures,seed=None):
    number = 4*measures
    if seed == None:
        seed = choice(Vectors)
        number -= 1

    sequence = [seed]
    while number > 0:
        if len(sequence) < 2:
            nexts = getNextVectors(sequence[-1],None)
        else:
            nexts = getNextVectors(sequence[-1],sequence[-2])
        
        if len(nexts) == 0:
            sequence = seqence[:-1]
            number += 1
        else:
            sequence += [choice(nexts)]
            number -= 1
    return sequence

""" Prints each object in the sequence on its own line. """
def printEach(sequence):
    for obj in sequence:
        print obj[:3]

# TODO: create a getVectors(n) function
# Vectors are of the form (ab, bc, ac, cd, bd, ad)
Vectors = []
# First voice
for AB in ACCEPTABLE:
    
    # Second voice
    for BC in ACCEPTABLE:
        
        # Third Voice
        AC = addIntervals(AB,BC)
        if not AC in ACCEPTABLE:
            continue
##        Vectors += [[AB,BC,AC]]

        #Fourth Voice
        for CD in ACCEPTABLE:
            BD = addIntervals(BC,CD)
            if not BD in ACCEPTABLE:
                continue
            
            AD = addIntervals(AB,BD)
            if not AD in ACCEPTABLE:
                continue

            Vectors += [[AB,BC,AC,CD,BD,AD]]


printEach(generateMeasures(4))

# TODO
# take into accounts chord notes
# doesn't jump more than a 4th
