
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def index(request):
    return HttpResponseRedirect('/all-words/')


# vim: et sw=4 sts=4
