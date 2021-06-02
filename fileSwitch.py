def ChangingFileData():
    fileA  = input("Enter file A")
    fileB = input("Enter File B")
    
    with open(fileA, 'r') as a:
        data_a = a.read()
        
    with open(fileB, 'r') as a:
        data_b = a.read()

    with open(fileA, 'w') as a:
        a.write(data_b)
 
    with open(fileB, 'w') as b:
        b.write(data_a)
 
ChangingFileData()