#!/usr/bin/python
#PYTHON_ARGCOMPLETE_OK

import argparse
import argcomplete

# Global parameters
VERSION = '0.1.2'
VERBOSE = False

class simpleCLI(object):
	commands = {}

	def __init__(self):
		self._parser = argparse.ArgumentParser(
			formatter_class=argparse.ArgumentDefaultsHelpFormatter
		)
		argcomplete.autocomplete(self._parser) 

		self.flags = {}
		self.commands = {}

	def __call__(self,args):
		for flag in self.flags:
			self._parser.add_argument('--'+flag,dest=flag,action='store_true')

		self._parser.add_argument('command',choices=self.commands.keys(),action='store',help='Select a command.')
		self._parser.add_argument('arguments', metavar='args', type=str, nargs='+', help='Arguments to pass to the command.')

		# Parse arguments
		args = self._parser.parse_args()
		for flag in self.flags:
			self.flags[flag] = vars(args)[flag]
		self.commands[args.command].__call__(*args.arguments)


	def registerFlag(self,flag, default_value=False):
		self.flags[flag] = default_value

	def registerCommand(self,command):
		self.commands[command.__name__] = command
		simpleCLI.commands[command.__name__] = command

# Custom parsing action to generate new functionalities dynamically
class FunctionCallAction(argparse.Action):
	 def __call__(self, parser, namespace, value, option_string=None):
			 setattr(namespace, self.dest, simpleCLI.commands[value])