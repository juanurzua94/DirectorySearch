# project1.py
# ICS 32 Fall 2017
'''This program iterates through files and directories based upon the users input. The search for files with desired consideration are based upon the inputted path,
the extension of the files, the contents of the files, the byte size of the files, or the name of the files. With the files in consideration, the user has the option
to update the time of the files, print out the first line of text of each file, or make a duplicate file in the same directory.'''

from pathlib import Path
import os

#This global list will contain all the files in consideration which are based
#upon the users input.

files_in_consideration = []

def get_files_in_dir(path: Path)-> None:
    '''This function returns all the files within the directory specified in the path argument'''
    directory = path
    list_of_files = []
    for file in directory.iterdir():
        if file.is_file() == True:
            list_of_files.append(file)
            list_of_files.sort()
    files_in_consideration.extend(list_of_files)
    
def get_subdir_and_files(path: Path)->None:
    '''This function obtains all the files found within the inputted directory as well as the files found
    within all of the subdirectories located within that directory. This function uses recursion to obtain the files found within
    all of the nested subdirectories. The files and direcories are sorted in lexicographic order within
    the global list named files_in_cosideration'''
    starting_dir = path
    file = []
    dire = []
    for counter in starting_dir.iterdir():
        if counter.is_file() == True:
            file.append(counter)
            file.sort()
        else:
            dire.append(counter)
            dire.sort()
    files_in_consideration.extend(file)
    if len(dire) > 0:
        for y in dire:
            get_subdir_and_files(y)
       
def connect_path(path: [str])-> list:
    '''This function connects the path found within the list in main if there are any spaces in the input. The
    reason for why the path will not be connected as one is due to the input by the user being stored into a list that uses
    the split function which breaks the input in seperate pieces into a list based off where a space is found in the input. '''
    base = path[1]
    counter = 2
    while counter != len(path):
        base += ' '
        base += path[counter]
        counter += 1
    new_list = [path[0], base]
    return new_list

def search_for_file(file: str)-> None:
    '''This function searches for a specific file inputted by the user in the list files_in_consideration.
    This function uses the method split() from os.path which breaks the head and the tail of the path into the list.
    The inputted file is then compared with the tail of the path to see if there is a match. If so, then the path
    is printed and stored within files_in_consideration.'''
    new_list = []
    for counter in files_in_consideration:
        x = os.path.split(counter)
        if file == x[1]:
            new_list.append(counter)
            print(counter)
    files_in_consideration.clear()
    files_in_consideration.extend(new_list)
            

def search_for_extension(ext: str)->None:
    '''This function searches through the list files_in_consideration for a file containing
    the ext that the user inputted. It does so by splitting the ext from the path(s) found within files_in_consideration using
    method splitext() from os.path. A comparison is then made and if the ext. matches that of the input, the path for that ext.
    is printed and stored in files_in_consideration.'''
    new_list = []
    if ext[0] != '.':
        ext = '.' + ext
    for counter in files_in_consideration:
        x = os.path.splitext(counter)
        if ext == x[1]:
            new_list.append(counter)
            print(counter)
    files_in_consideration.clear()
    files_in_consideration.extend(new_list)
            
def files_containing_text(words: str)-> None:
    '''This function opens all text based files found within files_in_consideration and searches to see if the files
    contain text that the user inputted. if so, then the path of that file is printed and stored within files_in_consideration.'''
    new_list = []
    for counter in files_in_consideration:
        try:
            z = open(counter, 'r')
            y = z.read()
            if words in y:
                new_list.append(counter)
                print(counter)
            z.close()
        except:
            continue
    files_in_consideration.clear()
    files_in_consideration.extend(new_list)
    
def get_lesser_than_bytes(number: str) -> None:
    '''This function uses os.path.getsize() to obtain the bytes of each file found within files_in_consideration. The bytes
    are then compared to the integer that the user inputted and if the files has less bytes than the integer, the path for the file
    is printed and stored in files_in_consideration.'''
    new_list = []
    less_than = int(number)
    for counter in files_in_consideration:
         if os.path.getsize(counter) < less_than:
             new_list.append(counter)
             print(counter)
    files_in_consideration.clear()
    files_in_consideration.extend(new_list)
    
        
def get_greater_than_bytes(number: str) -> None:
    '''This function uses os.path.getsize() to obtain the bytes of each file found within files_in_consideration. The bytes
    are then compared to the integer that the user inputted and if the files has more bytes than the integer, the path for the file
    is printed and stored in files_in_consideration.'''
    new_list = []
    greater_than = int(number)
    for counter in files_in_consideration:
        if os.path.getsize(counter) > greater_than:
             new_list.append(counter)
             print(counter)
    files_in_consideration.clear()
    files_in_consideration.extend(new_list)

        
        

def get_first_line_of_text()->None:
    '''This function goes through each text based file found within files_in_consideration and outputs the first line found within
    those files.'''
    for x in files_in_consideration:
        try:
            counter = 0
            y = open(x, 'r')
            z = y.readline().strip()
            print(z)
        except:
            print('NOT TEXT')
            continue
        
def duplicate_file()->None:
    '''This function goes through each file found within files_in_consideration and makes a duplicate copy of each file and places them
    within the same directory the original copy is found. .dup is added to the end of the duplicate files.'''
    for counter in files_in_consideration:
        z = os.path.split(counter)
        file = Path(z[1] + '.dup')
        path = Path(z[0])
        path = path / file
        path.touch()

def touch_files()-> None:
    '''This function goes through each file found within files_in_consideration and uses the method touch() from class Path on them.
    This modifies the time for each file.'''
    for counter in files_in_consideration:
        counter.touch()
        
def get_first_option()-> None:
    '''This function recieves input from the user which is a letter (either D or R) and a path. If the path contains
    any spaces then function connect_path is called which connects the input into one entity.If D is inputted then all the files
    within the path will be in consideration. If R is inputted then all the files, subdirectories, and files within those subdirectories will be in
    consideration. If the input doesnt follow this format then ERROR is printed and the user is then given another attempt at the input.'''
    while True:
        option = input()
        inputted_information = option.split()
        if len(inputted_information) > 2:
            inputted_information = connect_path(inputted_information)
        if len(inputted_information) < 2:
            print("ERROR")
            continue
        path = Path(inputted_information[1])
        if path.exists() == False:
            print("ERROR")
            continue
        if inputted_information[0] == 'D':
            get_files_in_dir(path)
        elif inputted_information[0] == 'R':
            get_subdir_and_files(path)
        else:
            print("ERROR")
            continue
        for counter in files_in_consideration:
            print(counter)
        break
    



def get_second_option()->None:
    '''This function recieves the second input from the user. If the input contains more than 2 words then connect path is called
    to connect the 2nd word and any word after into one entity. If the input doesnt follow as formatted then ERROR is printed and the user
    is then given another attempt at the input.'''
    while True:
        option = input()
        inputted_information = option.split()
        if len(inputted_information) > 2:
            inputted_information = connect_path(inputted_information)
        try:
            if inputted_information[0] == 'A':
                pass
            elif inputted_information[0] == 'N':
                search_for_file(inputted_information[1])
            elif inputted_information[0] == 'E':
                search_for_extension(inputted_information[1])
            elif inputted_information[0] == 'T':
                files_containing_text(inputted_information[1])
            elif inputted_information[0] == '<':
                get_lesser_than_bytes(inputted_information[1])
            elif inputted_information[0] == '>':
                get_greater_than_bytes(inputted_information[1])
            else:
                print("ERROR")
                continue
        except:
            print("ERROR")
            continue
        break
    

def get_last_option()->None:
    '''This function recieves the final input from the user(T, D, or F). If the input doesnt match any of the conditions,
    then an ERROR is printed and the user is given another attempt to input. If there are no files in consideration, then the program
    ends using return.'''
    if len(files_in_consideration) == 0:
        return
    
    while True:
        option = input()
        if option == 'F':
            get_first_line_of_text()
            break
        elif option == 'D':
            duplicate_file()
            break
        elif option == 'T':
            touch_files()
            break
        else:
            print("ERROR")
            
        
if __name__ == '__main__':
    get_first_option()
    get_second_option()
    get_last_option()
