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
    
    match option:
        case '1':
            print('Starting pattern:\n')
            j=0
            pairs=[]
            for i in range(-11, 12):
                if i == 0:
                   continue
                if i % 2 == 1 and i != 1 and i < 0 or i % 2 == 0 and i > 0:
                    j=i
                else:
                    pairs.append((j, i)) 
                print(j)
            print(pairs)
  
        case _: print('Not implemented yet!')
           
            

    
if __name__ == '__main__':
    main()