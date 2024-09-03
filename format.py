while True:

    ids = [] 

    while True:
        #print('\n')
        user = input('Enter Meter ID: ')
        
        if user == '':
            break
        else:
            ids.append(user)
            
    print('\n')
    print(','.join(ids))
    print('\n')
    print('\'' + '\',\''.join(ids) + '\'')
    print('\n')

# for x in ids:
    # print(x)
    
# use Ctrl+Z to terminate program
# make title?
# save into txt for easy reference?