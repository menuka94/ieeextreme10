owners_lists = []
def test(dogs, no_of_owners):
    global owners_lists
    per_group = len(dogs) / no_of_owners
    no_of_dogs = len(dogs)

    for i in range(no_of_owners):
        owners_lists.append([])

    for j in range(no_of_dogs):
        for owner_list in owners_lists:
            owner_list.append(dogs[j])
        j += 1

    for owner_list in owners_lists:
        print(owner_list)

test([3,5,1,1], 2)
test([30,40,20,41,50], 4)