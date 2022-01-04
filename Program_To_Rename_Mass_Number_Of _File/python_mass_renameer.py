# Created by cybergreek0212204
 
# Program to rename bulk of your files at once 
# WARNING ! Use this python script on your own risk. I am not responsible for any of your loss
# Go through the code before you run the code to .... lower the chance of risk 
# of any of the loss .... and all the renamed can be renamed manually or with this script later
# IMPORTANT - All the files can be deleted if caused any problem eith the inputed argument,
# 
# This code is not safe to run and can cause any harm before any of your actions
# Go to 'main' function to understand the functioning properly 

# Completed
# Importing OS library
import os
from colorama import Fore, Back, Style
#TODO : make it a fully feached gnu utility which can take argument eith "--example"
def logo():
    print('   CYBERGREEK PRESENTS -   Mass_file_rename_automator ')
    print('               Created by - Arpan kumar    ')
    print('                            Personal use only...... \n\n\n ')


# This is the function to normally rename a file
try:
    # Try and except function is used to get rid of the error !!
    #  'The name of the file is already exists  .. '
    # And to skip the changes of rename of the file

    def rename(path, replacement, extension2, filename):
        my_source = os.path.join(path, filename)
        re = filename.replace(replacement, extension2)
        my_source2 = my_source.replace(filename, '')
        my_dest = my_source2 + re
        os.rename(my_source, my_dest)
        print('Replacement file : ', filename)
except Exception as Des:
    print(Des)
    exit

# noinspection PyArgumentList
try:
    # Here the code is tested successfully and here you don't get any error
    # Try except function is used
    def extension_remover(path, replacement, extension2):
        i = 0
        # We are listing the name and number of files in the specified directory
        for filename in os.listdir(path):
            if replacement in filename:
                print(i, '- ', filename)
                i += 1
        # Asking the user through manually input .....
        # If user wants to rename all the specified files 
        # or rename the files till any specifies directory indexes
        print('\n These are the total number of files with your replacement,')
        print('Do you want to rename all (1 - yes , 2- no ) :  ')
        a = int(input('Enter the number :  '))
        if a == 1:  # Method calling to rename all the files at once
            for filename in os.listdir(path):
                if replacement in filename:  # Listing only those files with the the extension which user wants
                    rename(path=path, replacement=replacement, extension2=extension2, filename=filename)

        elif a == 2:  # Method to rename particular number of files
            b = int(input('enter the number of files you want to rename :'))
            i = 0
            for filename in os.listdir(path):
                i += 1
                if i <= b:
                    if replacement in filename:  # Listing only those files with the the extension which user wants
                        rename(path=path, replacement=replacement, extension2=extension2, filename=filename)
        else:
            # If you enter any other number other than program wants 
            # Then you will get this line showed
            print('Enter the number correctly .......  To rename the files correctly ......')
except Exception as Fes:  # passing any other error occurred
    print(Fes)
    exit

try:
    # This is the function to rename the files with random and length of your want 
    def random_rename(path, extension, filename, length):
        i = 0
        import random
        ALPHABETS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'  # number of alphabets you can

        # use to get the random name ....

        # Function to get a random name 
        def random_char(y):
            zx = ''.join(random.sample(ALPHABETS, y))
            return zx

        # Here the final renaming of the file is done
        if extension in filename:
            my_source = os.path.join(path, filename)  # getting the path of the file specified
            my_source2 = my_source.replace(filename, '')  # removing the original filename to replace the new one
            my_dest = my_source2 + random_char(length) + extension  # getting the new name for the file
            os.rename(my_source, my_dest)
            print(i, 'Replacement file : ', filename)
            for _ in os.listdir(path):
                i += 1
except:
    pass

try:
    # this is the function to rename the file with custom name 
    def custom_rename(path, extension, filename, i, custom):
        if extension in filename:
            my_source = os.path.join(path, filename)  # getting the path of the file specified
            my_source2 = my_source.replace(filename, '')  # removing the original filename to replace the new one
            i1 = str(i)
            ef = str(custom) + i1 + str(extension)
            my_dest = my_source2 + ef  # getting the new name for the file
            os.rename(my_source, my_dest)
            print(i1, 'Replacement file : ', filename)
            for _ in os.listdir(path):
                i += 1
except:
    pass

# This function manages the work to .....
# Rename all the files with custom name ..
#  Or to Rename the specified number of files with custom name 
def custom_rename_limit(path, extension):
    print('Do you want to rename all (1 - yes , 2- no ) :  ')
    a = int(input('Enter the number :  '))
    # Enter the custom name for the file 
    custom = str(input('Enter the custom name for the file you want to rename :'))
    limit_check = len(custom)
    execute = False
    for filename in os.listdir(path):
        filename = list(filename)
        if list(custom) == filename[0: limit_check]:
            execute = True 
    if execute == True :
        print(Fore.RED + Back.GREEN +'CAUTION !!! THE CUSTOM CHARACTER ALREADY EXIST CHANGE THE THE CHARACTER OR YOUR FILE CAN BE DELETED ')
        print(Fore.RED + Back.GREEN + 'OR CHOOSE CUSTOM LIMIT' + Style.RESET_ALL)
        custom_rename_limit(path, extension)

    if a == 1:  # Renaming all the files with custom name
        print('The output for your custom name will be [custom1],[custom2]...... ')

        i = 0
        for filename in os.listdir(path):  # Initializing rename function
            i += 1
            custom_rename(path, extension, filename=filename, i=i, custom=custom)

    elif a == 2:  # renaming specifies number fo files with custom name
        print('The output for your custom name will be [custom1],[custom2]...... ')

        b = int(input('enter the number of files you want to rename :'))
        i = 0
        z = 0
        for filename in os.listdir(path):  # Initializing rename function
            i += 1
            if i <= b:
                z += 1
                custom_rename(path, extension=extension, filename=filename, i=z, custom=custom)
    else:
        print('Enter the number correctly .......  To rename the files correctly ......')

# This function manages the work to .....
# Rename all the files with random name ..
#  Or to Rename the specified number of files
def random_rename_limit(path, extension):
    print('Do you want to rename all (1 - yes , 2- no ) :  ')
    a = int(input('Enter the number :  '))
    # Enter the length of the random name here
    d = int(input('Enter the length of the random name : '))
    if a == 1:  # Renaming all the files with random name
        for filename in os.listdir(path):
            random_rename(path, extension, filename=filename, length=d)

    elif a == 2:  # renaming specifies number fo files with random name
        b = int(input('enter the number of files you want to rename :'))
        i = 0
        for filename in os.listdir(path):
            i += 1
            if i <= b:
                random_rename(path, extension, filename=filename, length=d)
    else:
        print('Enter the number correctly .......  To rename the files correctly ......')


# This function specifies you are going to use the
# random rename functions .....   or the
# Custom rename function ....
def total_rename(path, extension):
    print('Do want to rename the file with ( \n 1 - random characters \n 2.Custom characters')
    c = int(input(' Enter the number : '))
    try:
        if c == 1:  # calling the random rename functions
            i = 0
            for filename in os.listdir(path):
                if extension in filename:
                    print(i, '- ', filename)
                    i += 1
            print('\n These are the total number of files with your replacement,')
            random_rename_limit(path, extension)
        elif c == 2:  # Calling the Custom rename function
            i = 0
            for filename in os.listdir(path):
                if extension in filename:
                    print(i, '- ', filename)
                    i += 1
            print('\n These are the total number of files with your replacement,')
            custom_rename_limit(path, extension)
        else:
            print('Enter the number correctly .......  To rename the files correctly ......')
    except Exception as e:

        # If you are getting any error her it is your fault 
        # not of program :)
        print(e, f'Enter the number Correctly .... To run the program \n\n')


# This function control that which facility of the program you are going to use
# 1. Changing the extension
# 2. Just renaming the file with the name of of convenience
def main():
    while True:
            logo()
            try:
                ec = 'Do you want to just rename the Extension of the file or just want to just change all the names ..'
                print(ec)
                # Input the facility of the program you want to use
                gh = int(input('Choose 1. Rename the extension 2. Change the name of the file : 3. EXIT :- '))
                # Enter the path of the file till the containing folder in way variable 
                # Test path example
                # path = 'G:\Website templates\my final website template\Students Notes _ Physics For Future_files'
                if gh == 1:  # Calling the extension change facility
                    try:
                        way = str(input('Enter the destination of the files you want to rename : '))
                        replacement = str(input('Enter the extension you want to replace : '))
                        extension2 = str(input('Enter the new extension you want to change with : '))
                        extension_remover(path=way, replacement=replacement, extension2=extension2)
                    except:
                        pass
                elif gh == 2:  # Calling the rename facility
                    try:
                        way = str(input('Enter the destination of the files you want to rename : '))
                        # Here input the extension of the files you want to rename
                        extension = str(input('Enter the extension of the file you want to rename with the  " . " : '))
                        total_rename(way, extension)
                    except:
                        pass
                elif gh == 3:
                    break
            except BaseException as Eas:
                ez = ' Choose the option correctly.... to rename the files correctly......'
                print(f'\n \n Exception is :', Eas , '\n', '\n\n')
                exit
# Initialising the program
if __name__ == '__main__':
    try:
        
        # Initialising the main function 
        # to init() all the facilities of the code
        main()
    except Exception as r:
            print('Exception is : ' + str(r))
            print('\n Choose the options correctly .......')
            
