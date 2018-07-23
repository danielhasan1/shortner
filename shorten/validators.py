from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validator_url(value):
	url_validator = URLValidator()
	value1=False
	value2=False
	try:
		url_validator(value)
	except:
		value1=True
	value2url="http://"+value
	try:
		url_validator(value2url)
		#value=value2url
	except:
		value2 = True
		print("here",value2url)
	if value1==False and value2==False:
		raise ValidationError("Invalid URL for this Field")
	print("final",value)
	return value


def validate_dot_com(value):
	if not ".com" in value:
		if not ".co" in value:
			if not ".in" in value:
				if not ".org" in value:
					if not "youtu.be" in value:
						raise ValidationError("May be its missing something!")
		#raise ValidationError("This is not a valid url")

	return value


def validaotr_http(value):
	if not "http://" in value:
		if not "https://" in value:
			raise ValidationError("please type a valid url or its missing (http://) protocol")
	return value