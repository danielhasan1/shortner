from django.conf import settings
from django.http import HttpResponseRedirect
DEFAULT_REDIRECT_URL = getattr(settings,"DEFAULT_REDIRECT_URL","http://www.kwarg.com")
def wildcard_redirect(reqquet,path=None):
	if path is not None:
		new_url = DEFAULT_REDIRECT_URL + "/" + path
		return HttpResponseRedirect(new_url)