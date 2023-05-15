#!/usr/bin/python3
"""HBNB command interpreter"""
import cmd

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class HBNBCommand(cmd.Cmd):
    """the entry class for the cmd interpreter"""

    prompt = "(hbnb) "
    class_dict = {'Amenity': Amenity,
                  'BaseModel': BaseModel,
                  'City': City,
                  'Place': Place,
                  'Review': Review,
                  'State': State,
                  'User': User}

    def do_all(self, args):
        """print all instances based on a class name or not"""
        class_dict = self.class_dict
        obj_dict = storage.all()
        all_instances = []
        class_instances = []
        if len(args) == 0:
            for key in obj_dict:
                instance = obj_dict[key]
                all_instances.append(str(instance))
            return self.print_msg(all_instances)
        else:
            if args not in class_dict:
                return self.print_msg("** class doesn't exist **")
            for key in obj_dict:
                instance_dict = obj_dict[key].to_dict()
                if instance_dict["__class__"] == args:
                    instance = obj_dict[key]
                    class_instances.append(str(instance))
            return self.print_msg(class_instances)

    def do_create(self, args):
        """Creates a new instance of a class"""
        class_dict = self.class_dict
        if len(args) == 0:
            return self.print_msg("** class name missing **")
        elif args not in class_dict:
            return self.print_msg("** class doesn't exist **")
        new_instance = class_dict[args]()
        # storage.new() has already been called in the new instance
        storage.save()
        return self.print_msg(new_instance.id)

    def do_destroy(self, args):
        """Delete an existing instance"""
        obj = args.split()
        while True:
            passed, instance_data = self.instance_check(obj)
            if passed:
                all_objs, key = instance_data[1:]
                del all_objs[key]
                storage.save()
            break

    def do_EOF(self, args):
        """Signal to End the reading of input"""
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_show(self, args):
        """prints the string representation og an instance"""
        obj = args.split()
        while True:
            passed, instance_data = self.instance_check(obj)
            if passed:
                return self.print_msg(instance_data[0])
            break

    def do_update(self, args):
        """Updates an existing instance attribute or adds new attribute"""
        attr_list = args.split()
        len_attr = len(attr_list)
        # print(self.instance_check(attr_list))
        check, instance_data = self.instance_check(attr_list)
        if check:
            if len_attr < 3:
                return self.print_msg("** attribute name is missing **")
            elif len_attr < 4:
                return self.print_msg("** value missing **")
            instance = instance_data[0]
            attribute_name, attribute_value = attr_list[2:4]
            if attribute_value[0] == '"' and attr_list[-1] is attribute_value:
                if attribute_value[-1] == '"':
                    attribute_value = attribute_value[1:-1]
                else:
                    attribute_value = attribute_value[1:]
            else:
                for value in attr_list[4:]:
                    attribute_value = " ".join([attribute_value, value])
                    if value[-1] == '"':
                        attribute_value = attribute_value[1:-1]
                        break
                    elif attr_list[-1] is value:
                        attribute_value = "".join([attribute_value, '"'])
                        attribute_value = attribute_value[1:-1]
            setattr(instance, attribute_name, attribute_value)
            # obj_dict[key] = instance.to_dict()
            instance.save()

    def emptyline(self):
        """Called when an empty line is entered in response to prompt"""
        pass

    def instance_check(self, obj):
        """Check and return an instance"""
        i = 0
        len_obj = len(obj)
        class_dict = self.class_dict
        all_objs = storage.all()
        if len_obj == 0:
            self.print_msg("** class name missing **")
            return False, None
        elif obj[i] not in class_dict:
            self.print_msg("** class doesn't exist **")
            return False, None
        elif len_obj == 1:
            self.print_msg("** instance id missing **")
            return False, None
        class_name, obj_id = obj[:2]
        key = ".".join([class_name, obj_id])
        if key not in all_objs:
            self.print_msg("** no instance found **")
            return False, None
        instance = all_objs[key]
        return True, [instance, all_objs, key]

    def print_msg(self, msg=None):
        """Called to handle messages"""
        self.stdout.write("{}\n".format(msg))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
