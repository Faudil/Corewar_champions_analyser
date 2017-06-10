#!/usr/bin/python3

import sys
import os

instruct_tab = []
limit = 60
mode = 0
source_dir = ""

def is_tab(str):
    i = 0
    while i < len(str):
        if str[i] != '\t':
            return False
        i+= 1
    return True        

def epur_buffer(tab):
    i = 0
    while i < len(tab):
        if '#' in tab[i] and tab[i].index('#') > 0:
            tab[i] = tab[i][0:tab[i].index('#')]
        if tab[i].startswith('#') == True or tab[i].startswith('.') == True or is_tab(tab[i]) == True:
            tab.pop(i)
            i -= 1
        i += 1
    return tab

def test_lines(to_be_tested, champions):
    final = "File doesn't not match enought with any champion."
    verbose = False
    if ("-v" in sys.argv):
        verbose = True
    to_be_tested = epur_buffer(to_be_tested)
    for champion in champions:
        nb = 0
        if champion.endswith(".s"):
            file_tmp = open(source_dir + champion, "r")
            tmp = file_tmp.read().split('\n')
            tmp = epur_buffer(tmp)
            i = 0
            while i < len(to_be_tested) and i < len(tmp):
                if to_be_tested[i] == tmp[i]:
                    nb += 1
                i += 1
            percent = round((nb * 100) / len(to_be_tested), 2)
            if verbose == True:
                print("There are", nb, "occurences with", champion, "which is :", percent, "% of the tested file")
            elif (percent > limit):
                final = "This file is more than "+ str(limit) + "% equal to " + champion
    print(final)

def test_instruct(to_be_tested, champions):
    verbose = False
    final = "File doesn't not match enought with any champion."
    if ("-v" in sys.argv):
        verbose = True
    to_be_tested = epur_buffer(to_be_tested)
    for champion in champions:
        nb = 0
        if champion.endswith(".s"):
            file_tmp = open(source_dir + champion, "r")
            tmp = file_tmp.read().split('\n')
            tmp = epur_buffer(tmp)
            i = 0
            while i < len(to_be_tested) and i < len(tmp):
                for instruct in instruct_tab:
                    if instruct in to_be_tested[i] and instruct in tmp[i]:
                        nb += 1
                i += 1
            percent = round(nb * 100 / len(to_be_tested), 2)
            if verbose == True:
                print("There are", nb, "occurences with", champion, "which is :", percent, "% of the tested file")
            elif (percent > limit):
                final = "This file is more than " + str(limit) + "% equal to " + champion
    print(final)

def parse_config_file():
    global limit
    global mode
    global source_dir
    global instruct_tab
    try:
        cfg_file = open("config.cfg", "r")
        cfg = cfg_file.read()
    except:
        sys.stderr.write("config file not found")
        sys.exit(84)
    cfg_tab = cfg.split('\n')
    for line in cfg_tab:
        if line.startswith("instruct = ") == True:
            tmp = line[line.index('[') + 1:line.index(']')]
            instruct_tab = tmp.split(',')
        if line.startswith("percent = ") == True:
            limit = int(line[10:])
        if line.startswith("mode = ") == True:
            mode = 0 if line[7:] == "line" else 1
        if line.startswith("source = ") == True:
           source_dir = line[line.index('(') + 1:line.index(')')]

parse_config_file()
if (len(sys.argv) == 1):
    print("Please type -h as argument if you seek help")
    exit(1)
if (len(sys.argv) > 1 and sys.argv[1] == "-h"):
    print("The first argument has to be the file to be tested")
    print("The second argument can be -v to activate the verbose mode")
    exit(0)
try:
    champions = os.listdir(source_dir)
except:
    sys.stderr.write("Error " + source_dir + " folder not found please check the source variable in config.cfg")
    sys.exit(84)
for arg in sys.argv[1:]:
    if arg != '-v' and arg != '-h':
        print("File :", arg)
        try :
            file = open(arg, "r")
            to_be_tested = file.read().split('\n')
            file.close()
        except:
            sys.stderr.write("Failed to read tested file\n")
            sys.exit(84)
        if mode == 0:
            test_lines(to_be_tested, champions)
        if mode == 1:
            test_instruct(to_be_tested, champions)
