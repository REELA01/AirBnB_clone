#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
from shlex import split
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def option(argg):
    cur_b = re.search(r"\{(.*?)\}", argg)
    br = re.search(r"\[(.*?)\]", argg)
    if cur_b is None:
        if br is None:
            return [i.strip(",") for i in split(argg)]
        else:
            lexx = split(argg[:br.span()[0]])
            rett = [i.strip(",") for i in lexx]
            rett.append(br.group())
            return rett
    else:
        lexx = split(argg[:cur_b.span()[0]])
        rett = [i.strip(",") for i in lexx]
        rett.append(cur_b.group())
        return rett


class HBNBCommand(cmd.Cmd):
    """define the command interpreter"""

    prompt = "(hbnb) "

    __clss = {
        "BaseModel",
        "User",
        "Place",
        "State",
        "City",
        "Amenity",
        "Review"
        }

    def do_quit(self, arg):
        """Quit command for exit"""
        return True

    def do_EOF(self, arg):
        """EOF exit"""
        print("")
        return True

    def do_create(self, arg):
        """create new instance of basemodel calss"""
        arg_1 = option(arg)
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
        else:
            print(eval(arg_1[0])().id)
            storage.save()

    def do_show(self, arg):
        """string repressntation of instance"""
        arg_1 = option(arg)
        dict_1 = storage.all()
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
        elif len(arg_1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_1[0], arg_1[1]) not in dict_1:
            print("** no instance found **")
        else:
            print(dict_1["{}.{}".format(arg_1[0], arg_1[1])])

    def do_destroy(self, arg):
        """deletes an inctance bt the clss name"""
        arg_1 = option(arg)
        dict_1 = storage.all()
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
        elif len(arg_1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_1[0], arg_1[1]) not in dict_1.keys():
            print("** no instance found **")
        else:
            del dict_1["{}.{}".format(arg_1[0], arg_1[1])]
            storage.save()

    def do_all(self, arg):
        """print all string represnation of all instance"""
        arg_1 = option(arg)
        if len(arg_1) > 0 and arg_1[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
        else:
            oblis = []
            for ob in storage.all().values():
                if len(arg_1) > 0 and arg_1[0] == ob.__class__.__name__:
                    oblis.append(ob.__str__())
                elif len(arg_1) == 0:
                    oblis.append(ob.__str__())
            print(oblis)

    def do_update(self, arg):
        """update the instance"""
        arg_1 = option(arg)
        dict_1 = storage.all()

        if len(arg_1) == 0:
            print("** class name missing **")
            return False
        if arg_1[0] not in HBNBCommand.__clss:
            print("** class doesn't exist **")
            return False
        if len(arg_1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_1[0], arg_1[1]) not in dict_1.keys():
            print("** no instance found **")
            return False
        if len(arg_1) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_1) == 3:
            try:
                type(eval(arg_1[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_1) == 4:
            obj = dict_1["{}.{}".format(arg_1[0], arg_1[1])]
            if arg_1[2] in obj.__class__.__dict__.keys():
                val_t = type(obj.__class__.__dict__[arg_1[2]])
                obj.__dict__[arg_1[2]] = val_t(arg_1[3])
            else:
                obj.__dict__[arg_1[2]] = arg_1[3]
        elif type(eval(arg_1[2])) == dict:
            obj = dict_1["{}.{}".format(arg_1[0], arg_1[1])]
            for ke, val in eval(arg_1[2]).items():
                if (ke in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[ke]) in {str, int, float}):
                    val_t = type(obj.__class__.__dict__[ke])
                    obj.__dict__[ke] = val_t(val)
                else:
                    obj.__dict__[ke] = val
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
