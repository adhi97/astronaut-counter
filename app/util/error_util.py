import traceback

from flask import jsonify

class ErrorUtil:
	@staticmethod
	def __handle_traceback__():
		if traceback.format_exc().strip() != 'NoneType: None':
            traceback.print_exc()
            return True
		return False

	@classmethod
	def builder(cls):
		return ErrorUtilBuilder()

class ErrorUtilBuilder:
	def __init__(self):
		self.errors = []