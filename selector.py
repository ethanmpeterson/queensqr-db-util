def selectFrom(arr):
    for i, o in enumerate(arr):
        print("\n-------------------------\n")
        print("index = " + str(i) + "\n")
        print(o)
        print("\n-------------------------\n")
    print("Type the index number of the item you would like to select")
    ans = input("answer: ")
    return arr[int(ans)] 