


with open("Input/Letters/starting_letter.txt") as starting_letter:
    letter = starting_letter.read()
    #print(letter)

with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()
    #print(names_list)




for i in names_list:
    i = i.strip('\n')
    dispatched = letter.replace('[name]', i)


    with open(f"Output/ReadyToSend/letter_to_{i}.txt", "w") as f:
        f.write(dispatched)



