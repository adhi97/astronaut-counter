from voluptuous import Schema, Optional, Required, Length, All


class Validator:
	 astroSchema = Schema({
    	Required('id'): All(str, Length(min=24, max=24))
    })

	@classmethod
	def validateGet(cls, data):
		return cls.astroSchema(data)