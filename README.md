# To-Do
A simple python program that provides an interactable To-Do list in the shell.

## Installation
Simply put the .py file into a directroy you wish. You can put it in a directory that is in your PATH to allow for quick execution.

## Storage
The file with the todo items is being stored in your home directory as a ```.todo``` file.
A more optimal solution is being looked into. Possible json storage is underway for further functionality support such as deadlines.

## Instruction
### Getting the list of the To-Do items
Simply execute the script without any arguments.
### Adding an item to the To-Do list
Execute the script with the ```add``` argument followed by the job you wish to be added.

Example:
```shell
#Add the job "Clean my home directory." to the To-Do list
To-Do.py add Clean my home directory
```

###Removing an item from the To-Do list
Execute the script with the ```remove``` argument followed by the index of the job

Example
```shell
#Print my To-Do list
To-Do.py

>[1] Clean my home directory
>[2] Do some squats
>[3] Call mom

#Remove do some squats from the To-Do list
To-Do.py remove 2

>TODO: removed Do some squats
```
