#!/usr/bin/python3

from sys import argv
from os import environ, path

"""
--A simple To-Do list program for use in the Shell--

Author: Karen Arzumanyan
Repository: https://www.github.com/Renzum/To-Do
Version: 1.0
"""

def print_help():
    """
    Prints the help message
    """
    print("Usage: todo [add|remove|help] [job]")
    print("add: Add a job to the todo list")
    print("remove: Remove a job at a given index from the todo list")
    print("help: Print this help message")
    print("No arguments: Print the todo list")
    print("The todo list is saved in the home directory of the user as .todo")

class ToDo:
    data_file = ''
    to_do_list = []
    def __init__(self):
        self.data_file = ToDo.get_data_file()
        self.read_to_do_file()

    def __del__(self):
        self.write_to_do_file()

    def read_to_do_file(self):
        try:
            file = open(self.data_file, 'r')
            for line in file:
                self.to_do_list.append(line.strip())
            file.close()
        except FileNotFoundError:
            try:
                file = open(self.data_file, 'w')
                file.close()
            except:
                print("Error creating file")
                exit(1)

    def write_to_do_file(self):
        try:
            file = open(self.data_file, 'w')
            for line in self.to_do_list:
                file.write(line + '\n')
            file.close()
        except FileNotFoundError:
            print("File not found")
            exit(1)

    def get_data_file():
        if path.exists(environ['PWD'] + '/.todo'):
            return environ['PWD'] + '/.todo'
        else:
            return environ['HOME'] + '/.todo'

    def print(self):
        if len(self.to_do_list) == 0:
            print("No To-Do's! Job well done!")
        else:
            print("Your To-Do list:")
            try:
                for index, job in enumerate(self.to_do_list):
                    print("[{}] {}".format(index + 1, job))
            except IndexError:
                print("Index out of range")
                exit(1)

    def add_todo(todo):
        #Concatenate all the words into a single string
        job = ''
        for word in todo:
            job += word + ' '

        #Add the job to the todo list
        try:
            self.to_do_list.append(job)
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
            item = self.to_do_list.pop(index - 1)
        except IndexError:
            print("Index out of range")
            exit(1)

        print(f"TODO: removed {item}")

def main(arguments):
    to_do = ToDo()
    if len(arguments) == 0:
        to_do.print()
        exit(0)
    else:
        if arguments[0] == "add":
            #Verify that the user has provided at least one arguments
            if len(arguments) == 1:
                print("No job specified")
                exit(1)
            else:
                #Add the job to the todo list
                to_do.add_todo(arguments[1:])
        elif arguments[0] == "remove":
            #Verify that the user has provided the index of the job to remove
            if len(arguments) == 1:
                print("No index specified")
                exit(1)
            else:
                #Remove the job at the given index
                to_do.remove_todo(arguments[1])
        elif arguments[0] == "help":
            print_help()
        else:
            print("Unknown command")
            exit(1)

if __name__ == "__main__":
    main(argv[1:])
