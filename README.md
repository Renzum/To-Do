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

### Removing an item from the To-Do list
Execute the script with the ```remove``` argument followed by the index of the job

### Examples:
Call the ```To-Do.py``` with arguments ```add [job]``` to add a new item to the To-Do list.
```shell
To-Do.py add Clean my home directory
```
```shell
#Output
TODO: added Clean my home directory
```

Call the ```To-Do.py``` to print the list of current To-Do's
```shell
To-Do.py
```
```shell
#Output
[1] Clean my home directory
[2] Do some squats
[3] Call mom
```

Call the ```To-Do.py``` with arguments ```remove [index]``` to remove a certain item from the to do list
```shell
To-Do.py remove 2
```
```shell
#Output
TODO: removed Do some squats
```
