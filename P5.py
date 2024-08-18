def main(): 
    furry_pets = ["dog", "cat", "ferret", "hamster", "bunny"]
    feathered_pets = ["canary", "parrot", "budgie", "hawk"]
    all_pets = furry_pets + feathered_pets
    new_pets =[]
    i = 0
    for item in all_pets:
        if item[i][0] == "c":
            new_pets.append(item)
    print("The pet store sells:", all_pets)
    print("These start with the letter c:", new_pets)
main()
