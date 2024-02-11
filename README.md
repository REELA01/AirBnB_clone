
# 0x00. AirBnB clone - The console

## Introduction
The aim of the project is to built the console which is command interpreter to manage objects abstraction between objects and how they are stored.

## Storage
all the classes are handled by the Storage engine in the FileStorage Class.

## Installation
```bash
git clone https://github.com/REELA01/AirBnB_clone.git
```

## Execution
In interactive mode

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```
in Non-interactive mode

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```
## Testing using Python Unit Tests
1- unittest module

2- File extension .py

3- Files and folders star with ```bash test_```

4- Organization:for ```bash models/base.py```, unit tests in: ```bash tests/test_models/test_base.py```

5-Execution command

```bash python3 -m unittest discover tests```

or: 
```bash 
python3 -m unittest tests/test_models/test_base.py
```
### run test in non_interactive mode
```bash
python3 -m unittest discover tests
```
### run test in interactive mode
```bash
echo "python3 -m unittest discover tests" | bash
```
## Working

1- Start the console in interactive mode:

```bash 
$ ./console.py
(hbnb)
```
2- Quit the console:

```bash
(hbnb) quit
$
```
or : ctrl + d to EOF (andoffile)

3- Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```
## Commands

1- Create

Creates a new instance of a class, saves it (to the JSON file) and prints the id

```bash
create <class>
```
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb)
```
2- Show

Prints the string representation of an instance based on the class name and id

```bash
show <class> <id>
```
```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```
3- Destroy

Deletes an instance based on the class name and id (save the change into the JSON file).

```bash
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```
4- all

Prints all string representation of all instances based or not on the class name.

```bash
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
```
5- update

Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).

```bash
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401)}
```
6- count

to retrieve the number of instances of a class

```bash
(hbnb) BaseModel.count()
2
```

