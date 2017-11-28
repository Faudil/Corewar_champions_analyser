# Corewar_champions_analyser

Anti-cheating autograder for Corewar championship by *Faudil PUTTILI*

To install the anti-cheating autograder you have to chmod and execute install.sh
which whill clone a champions repo (classics one like 42 or Octobre rouge) from github.
You can add or use yours by simply pasting there source file in the folder source (declared in the config file).

There is a configuration file which has 4 variables :
     
     mode = which is the mode of analysis (line by line) or instruction occurence mode (default = line).
      
     instruct = which is an array of instructions to analize in  instruct mode. (default = list of epitech corewar instructions)
     
     source = which is the source directory where all the references files are (default = champions/).
     
     percent = which is the minimum percentage of lines/instructs equal to (default = 60).

To use the anti-cheat autograder you just have to write names of files you want to test as first argument
and it will compare it and tell you with which file there are enought occurences to have doubt if the code is handmade.

You can type -v as argument and it will activate the verbose mode.

Example :
	./antiCheat 
	./antiCheat test_folder/*.s
-> To test every files in the folder test_folder
