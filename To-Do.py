#!/usr/bin/python3

from sys import argv
import getopt
from os import environ

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
        try:
            for index, job in enumerate(to_do_list):
                print("[{}] {}".format(index, job))
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

    to_do_list.pop(index)

    print("TODO: remove todo number" . index)

def print_help():
    pass

def main(arguments):
    data_file = environ['HOME'] + '/todo.txt'
    #Read the todo list from the user data file
    read_to_do_file(data_file)
    if len(arguments) == 0:
        print_todo_list()
        exit(0)
    else:
        if arguments[0] == "add":
            add_todo(arguments[1:])
        elif arguments[0] == "remove":
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
