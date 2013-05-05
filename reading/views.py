from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
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
    num = page.page_number
    try:
        prev_page = Page.objects.get(book=book, page_number=num-1)
        context['prev_page'] = prev_page.page_number
    except Page.DoesNotExist:
        pass
    try:
        next_page = Page.objects.get(book=book, page_number=num+1)
        context['next_page'] = next_page.page_number
    except Page.DoesNotExist:
        pass
    context['page'] = page
    return render_to_response('reading/page.html', context)


@login_required
def edit_page_chapter(request, book_id, page_num):
    book = get_object_or_404(BookTranslation, pk=book_id)
    page = get_object_or_404(Page, page_number=page_num, book=book)
    chapter = request.POST['value']
    page.chapter = chapter
    page.save()
    return HttpResponse(chapter)


@login_required
def edit_page_text(request, book_id, page_num):
    book = get_object_or_404(BookTranslation, pk=book_id)
    page = get_object_or_404(Page, page_number=page_num, book=book)
    text = request.GET['text']
    page.text = text
    page.save()
    return HttpResponse(text)
