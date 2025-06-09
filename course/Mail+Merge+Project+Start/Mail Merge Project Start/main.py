#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as file:
    lines = file.readlines()
    with open("./Input/Names/invited_names.txt") as name_file:
        names = name_file.readlines()
        for name in names:
            lines[0]=lines[0].replace("[name]",name.strip())
            with open(f"./Output/ReadyToSend/letter_to_{name.strip()}.txt",mode="w") as write_file:
                for line in lines:
                    write_file.write(line)

            lines[0]=lines[0].replace(name.strip(),"[name]")