from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import RequestContext

from language_study.reading.models import BookTranslation
from language_study.reading.models import Page

from collections import defaultdict

def book(request, book_id):
    context = RequestContext(request)
    book = get_object_or_404(BookTranslation, pk=book_id)
    context['pages'] = book.page_set.all()
    return render_to_response('reading/book.html', context)

def page(request, book_id, page_num):
    context = RequestContext(request)
    book = get_object_or_404(BookTranslation, pk=book_id)
    page = get_object_or_404(Page, page_number=page_num, book=book)
    context['page'] = page
    return render_to_response('reading/page.html', context)
