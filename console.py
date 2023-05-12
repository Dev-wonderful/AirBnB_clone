#!/usr/bin/python3
"""HBNB command interpreter"""
import cmd
from models.__init__ import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
	"""the entry class for the cmd interpreter"""

	prompt = "(hbnb) "

	def do_quit(self, args):
		"""Quit command to exit the program"""
		return True

	def do_EOF(self, args):
		"""Signal to End the reading of input"""
		return True

	def class_dict(self):	
		class_dict = {'BaseModel': BaseModel}
		return class_dict

	def emptyline(self):
		"""Called when an empty line is entered in response to prompt"""
		pass

	def print_msg(self, msg=None):
		"""Called to handle error messages"""
		self.stdout.write("{}\n".format(msg))

	def do_create(self, args):
		"""Creates a new instance of a class"""
		class_dict = self.class_dict()
		if len(args) == 0:
			return self.print_msg("** class name missing **")
		elif args not in class_dict:
			return self.print_msg("** class doesn't exist **")
		new_instance = class_dict[args]()
		storage.save()
		return self.print_msg(new_instance.id)

	def do_show(self, args):
		"""prints the string representation og an instance"""
		obj = args.split()
		i = 0
		len_obj = len(obj)
		class_dict = self.class_dict()
		obj_dict = storage.all()
		if len_obj == 0:
			return self.print_msg("** class name missing **")
		elif obj[i] not in class_dict:
			return self.print_msg("** class doesn't exist **")
		elif len_obj == 1:
			return self.print_msg("**instance id missing **")
		class_name, obj_id = obj
		key = ".".join([class_name, obj_id])
		if key not in obj_dict:
			return self.print_msg("** no instance found **")
		instance_dict = obj_dict[key]
		instance = class_dict[class_name](instance_dict)
		return self.print_msg(instance)


if __name__ == '__main__':
	HBNBCommand().cmdloop()

