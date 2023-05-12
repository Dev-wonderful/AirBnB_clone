#!/usr/bin/python3
"""HBNB command interpreter"""
import cmd


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


if __name__ == '__main__':
	HBNBCommand().cmdloop()

