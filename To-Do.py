#!/usr/bin/python3

from sys import argv
from os import environ

"""
--A simple To-Do list program for use in the Shell--

Author: Karen Arzumanyan
Repository: https://www.github.com/Renzum/To-Do
Version: 1.0
"""

to_do_list = []

#Read the todo list from the user data file
def read_to_do_file(path):
    #Read the file at the given path
    #Add each line to the todo list
    try:
        file = open(path, 'r')
        for line in file:
            to_do_list.append(line.strip())
        file.close()
    except FileNotFoundError:
        try:
            file = open(path, 'w')
            file.close()
        except:
            print("Error creating file")
            exit(1)
    pass

#Write the todo list to the user data file
def write_to_do_file(path):
    try:
        file = open(path, 'w')
        for line in to_do_list:
            file.write(line + '\n')
        file.close()
    except FileNotFoundError:
        print("File not found")
        exit(1)
    pass

#Print the todo list in an [index] [job] format
def print_todo_list():
    if len(to_do_list) == 0:
        print("No To-Do's! Job well done!")
    else:
        print("Your To-Do list:")
        try:
            for index, job in enumerate(to_do_list):
                print("[{}] {}".format(index + 1, job))
        except IndexError:
            print("Index out of range")
            exit(1)

#Add a list of words to the todo list as a single item
def add_todo(todo):
    #Concatenate all the words into a single string
    job = ''
    for word in todo:
        job += word + ' '

    #Add the job to the todo list
    try:
        to_do_list.append(job)
    except :
        print("Error adding todo")
        exit(1)

    print("TODO added: " + job)

#Remove a job from the todo list at a given index
def remove_todo(index):
    #Check if index is an integer
    try:
        index = int(index)
    except ValueError:
        print("Index must be an integer")
        exit(1)

    try:
        item = to_do_list.pop(index - 1)
    except IndexError:
        print("Index out of range")
        exit(1)

    print(f"TODO: removed {item}")

def print_help():
    print("Usage: todo [add|remove|help] [job]")
    print("add: Add a job to the todo list")
    print("remove: Remove a job at a given index from the todo list")
    print("help: Print this help message")
    print("No arguments: Print the todo list")
    print("The todo list is saved in the home directory of the user as .todo")

def main(arguments):
    data_file = environ['HOME'] + '/.todo'
    #Read the todo list from the user data file
    read_to_do_file(data_file)
    if len(arguments) == 0:
        print_todo_list()
        exit(0)
    else:
        if arguments[0] == "add":
            #Verify that the user has provided at least one arguments
            if len(arguments) == 1:
                print("No job specified")
                exit(1)
            else:
                #Add the job to the todo list
                add_todo(arguments[1:])
        elif arguments[0] == "remove":
            #Verify that the user has provided the index of the job to remove
            if len(arguments) == 1:
                print("No index specified")
                exit(1)
            else:
                #Remove the job at the given index
                remove_todo(arguments[1])
        elif arguments[0] == "help":
            print_help()
        else:
            print("Unknown command")
            exit(1)

    #Write the todo list to the user data file
    write_to_do_file(data_file)

if __name__ == "__main__":
    main(argv[1:])
