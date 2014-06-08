#!/usr/bin/python
#PYTHON_ARGCOMPLETE_OK

import argparse
import argcomplete
from functools import wraps

def cli_command(command):
	command.cli = True
	return command

class simpleCLI(object):
	def __init__(self):
		self._parser = argparse.ArgumentParser(
			formatter_class=argparse.ArgumentDefaultsHelpFormatter
		)
		argcomplete.autocomplete(self._parser)

		self.flags = {}
		self.commands = {}

		for attr, value in self.__class__.__dict__.iteritems():
			if getattr(value, 'cli', False):
				self.commands[value.__name__] = value

	def __call__(self,args):
		for flag in self.flags:
			self._parser.add_argument('--'+flag,dest=flag,action='store_true')

		self._parser.add_argument('command',choices=self.commands.keys(),action='store',help='Select a command.')
		self._parser.add_argument('arguments', metavar='args', type=str, nargs='*', help='Arguments to pass to the command.')

		# Parse arguments
		args = self._parser.parse_args()
		for flag in self.flags:
			self.flags[flag] = vars(args)[flag]
		self.commands[args.command].__call__(self, *args.arguments)


		# self.commands[command.__name__] = command
	# def cli_flag(self, flag, default_value = False):
	# 	def _cli_flag()

	# def registerFlag(self,flag, default_value=False):
	# 	self.flags[flag] = default_value

