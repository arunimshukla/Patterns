#Python program to write list sequence in a binary file

def binary_write():
    import pickle
    List = [10,20,30,40,50,60,-10,-20,-30]
    f=open('list.dat','wb')
    pickle.dump(list,f)
    print("Done!")
    f.close()
binary_write()
