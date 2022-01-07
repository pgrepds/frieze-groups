import re

def glideReflection(x, pairs):
    j=0
    start=-11
    end=12
    if pairs is not None and len(pairs) > 0:
        start=pairs[0][0]
        end=pairs[len(pairs) - 1][1]    
    newSequence=[]
    for i in range(start-(2*x), end-(2*x)+1):
        if i == 0:
            continue
        if i % 2 == 1 and i != 1 and i < 0 or i % 2 == 0 and i > 0:
            j=i
        else:
            # this fixes a weird special case which we haven't figured out yet.
            if i != 0 and j != 0:
                newSequence.append((j, i)) 
    return newSequence

def horizontalFlip(pairs):
    flippedSequence=[]
    reversedPairs=pairs[::-1]
    for p in reversedPairs:
        flippedSequence.append((p[1], p[0]))
    return flippedSequence

def visualize(pairs):                
    i=1
    for p in pairs:
        if i % 2 == 1:
            print('{}|{}'.format(p[0], p[1]), end='\t\t')
        i=i+1
    print()
    i=1
    for p in pairs:
        if i % 2 == 0:
            print('\t', end='')
        elif i % 2 == 1 and i != 1:
            print('\t    ', end='')
        if i % 2 == 0:
            print('{}|{}'.format(p[0], p[1]), end='')
        i=i+1   

def main():
    print('Simulating the 7 frieze groups.\n')
    print('Choose one of the following options and press enter:\n')
    print('<1> glide-reflection to the right, horizontal flip')
    print('<2> translation to the right')
    print('<3> glide-reflection to the right')
    print('<4> translation to the right, horizontal flip')
    print('<5> translation to the right, horizontal flip, vertical flip')
    print('<6> translation to the right, vertical flip')
    print('<7> translation to the right, rotate')
    
    option = input('')
    
    identity=[]
    match option:
        case '1':
            print('Starting pattern:\n')
            # we fix the starting state
            identity=glideReflection(0, [])
            visualize(identity)
            print()    
            print('You have the following action:')
            print('<1> Type gX for a glide-reflection to the right X times whereby X is any integer')
            print('<2> Type h for a horizontal reflection; notice that h is self-inverse.')
            print('<3> Type exit to exit the program.')
    
            pattern=identity
            x=input('')
            while x != 'exit':
                m = re.search(r'(g)(-\d+|\d+)', x)
                if m is not None:
                    gr=m.group(2)
                    pattern=glideReflection(int(gr), pattern)
                    visualize(pattern)
                    print('\n\n')
                elif x == 'h':
                    pattern=horizontalFlip(pattern)
                    visualize(pattern)
                    print('\n\n')
                x=input('')
        case _: print('Not implemented yet!')
    
if __name__ == '__main__':
    main()
    