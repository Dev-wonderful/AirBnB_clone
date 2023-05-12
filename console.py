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

	def emptyline(self):
		"""Called when an empty line is entered in response to prompt"""
		pass

	def print_msg(self, msg=None):
		"""Called to handle error messages"""
		self.stdout.write("{}\n".format(msg))
	def do_create(self, args):
		"""Creates a new instance of a class"""
		class_dict = {'BaseModel': BaseModel}
		if len(args) == 0:
			return self.print_msg("** class name missing **")
		elif args not in class_dict:
			return self.print_msg("** class doesn't exist **")
		new_instance = class_dict[args]()
		storage.save()
		return self.print_msg(new_instance.id)


if __name__ == '__main__':
	HBNBCommand().cmdloop()

