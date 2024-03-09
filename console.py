#!/usr/bin/python3

"""
Module for the HBNBCommand class and related functionality.

This module imports the cmd module for building interactive command-line interfaces,
the models module for accessing storage functionality, and the split function from the shlex module.
"""
import cmd
import models
from shlex import split


class HBNBCommand(cmd.Cmd):
    """
    Command-line interface for managing instances in the application.

    Attributes:
        prompt (str): The command prompt shown to the user.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Returns:
            bool: True to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program on EOF (Ctrl+D).

        Returns:
            bool: True to exit the program.
        """
        return True

    def emptyline(self):
        """
        Do nothing when an empty line is entered.
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.

        Args:
            arg (str): The arguments passed to the command.
        """
        args = split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        else:
            instance = models.storage.classes()[args[0]]()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id.

        Args:
            arg (str): The arguments passed to the command.
        """
        args = split(arg)
        if not args:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            """ key = f"{class_name}.{instance_id}" """
            key = class_name + "." + instance_id
            obj = models.storage.all()
            if key in obj:
                print(obj[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id.

        Args:
            arg (str): The arguments passed to the command.
        """
        args = split(arg)
        if not args or len(args) == 0:
            print("** class name missing **")
        elif args[0] not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            class_name = args[0]
            instance_id = args[1]
            """ key = f"{class_name}.{instance_id}" """
            key = class_name + "." + instance_id
            obj = models.storage.all()
            if key not in obj:
                print("** no instance found **")
            else:
                del obj[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name.

        Args:
            arg (str): The arguments passed to the command.
        """
        obj = models.storage.all()
        class_instances = []
        args = split(arg)
        class_name = args[0]
        if not args:
            for obj_id in obj:
                class_instances.append(str(obj[obj_id]))
            print(class_instances)
        elif class_name not in models.storage.classes():
            print("** class doesn't exist **")
        else:
            for obj_id in obj:
                if obj_id.split(".")[0] == class_name:
                    class_instances.append(str(obj[obj_id]))
            print(class_instances)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id by adding or updating attribute.

        Args:
            arg (str): The arguments passed to the command.
        """
        args = split(arg)
        obj = models.storage.all()
        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]
        if not args or len(args) < 1:
            print("** class name missing **")
        elif class_name not in models.storage.classes():
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{class_name}.{instance_id}" not in obj:
            print("** no instance found **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            instance_key = f"{class_name}.{instance_id}"
            instance = obj[instance_key]
            if attribute_name in instance.__dict__:
                value_type = type(instance.__dict__[attribute_name])
                attribute_value = value_type(attribute_value)
            setattr(instance, attribute_name, attribute_value)
            models.storage.save()


if __name__ == '__main__':
    """
    Entry point for the program.
    
    If this script is run directly, it initializes and starts the HBNBCommand command-line interface
    by calling the cmdloop() method of the HBNBCommand class.
    """
    HBNBCommand().cmdloop()
