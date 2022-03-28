#!/usr/bin/python3

from sys import argv
import getopt

to_do_list = []

def print_todo_list():
    for i in range(len(to_do_list)):
        print("TODO: [" + str(i) + "] " + to_do_list[i])

def add_todo(todo):
    job = ''
    for word in todo:
        job += word + ' '

    try:
        to_do_list.append(job)
    except :
        print("Error adding todo")
        exit(1)

    print("TODO added: " + job)

def remove_todo(index):
    #Check if index is an integer
    try:
        index = int(index)
    except ValueError:
        print("Index must be an integer")
        exit(1)

    print("TODO: remove todo number" . index)

def print_help():
    pass

def main(arguments):
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

if __name__ == "__main__":
    read_to_do_file()
    main(argv[1:])
    write_to_do_file()
