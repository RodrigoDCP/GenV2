# GenV2
This is a tool for basic audits.
![Texto alternativo de la imagen](IMG/V2/menu.PNG)

Generate passwords: it asks the user to input a series of words and the number of columns they want to create combinations. Then, all possible combinations are generated and saved to a file named "combinations.txt" in the same directory as the file.

Generate identities: it reads names and surnames from text files named "nombres.txt" and "apellidos.txt", and then generates 10 random identities with names, surnames, ages, and dates of birth. The generated names and surnames are chosen randomly from the text files.

Clear console: it clears the output console.

Quit: it exits the program.

The code uses Python libraries such as itertools, random, datetime, sys, and os to perform these operations. It also includes an ASCII banner at the top of the program

# Password generator.

To generate passwords, you only need to select option 1, which will take you to the password generator. You must input the words, letters, or numbers you want to combine or "concatenate", and to finish the character input, type "done". Then, you must specify the number of columns in which the combinations will be limited. Finally, everything will be saved in a text file as a password "

![Texto alternativo de la imagen](IMG/V2/PASS2.PNG)
![Texto alternativo de la imagen](IMG/V2/PASS3.PNG)


# Identity generator.

Here you will only need to select option 2, and it will automatically generate random and fake identities that you can use to create passwords together with the password generator, fill databases, obtain a quick identity or give it any other use.

![Texto alternativo de la imagen](IMG/V2/USER1.PNG)

# Install:
```bash
git clone https://github.com/RodrigoDCP/GenV2.git 
```

```bash                              
cd GenV2
```

```bash
python3 menu.py
```


