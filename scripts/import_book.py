#!/usr/bin/env python

import os, sys

sys.path.append(os.getcwd()+'/..')
os.environ['DJANGO_SETTINGS_MODULE'] = 'language_study.settings'

from django.db import transaction

from language_study.drills.models import Language
from language_study.reading.models import *

from optparse import OptionParser
from subprocess import Popen
import os

#@transaction.commit_manually
def main(base_dir, book_title, language_name, tesseract_language):
    language = Language.objects.get(name=language_name)
    try:
        book = Book.objects.get(title=book_title)
    except Book.DoesNotExist:
        book = Book(title=book_title)
        book.save()
    try:
        translation = book.booktranslation_set.get(language=language)
    except BookTranslation.DoesNotExist:
        translation = BookTranslation(book=book, language=language)
        translation.save()
    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            if filename.endswith('.jpg'):
                base = filename[:-4]
                # We assume that the file ends with '_[pagenum].jpg'
                pagenum = int(base.split('_')[-1])
                try:
                    # If the page is already in the database, skip it
                    page = translation.page_set.get(page_number=pagenum)
                    continue
                except Page.DoesNotExist:
                    pass
                print 'OCRing page', pagenum
                command = ['tesseract', filename, base, '-l',
                        tesseract_language]
                proc = Popen(command, cwd=root)
                proc.wait()
                text = open(root + base + '.txt').read()
                image_path = root + filename
                chapter = -1 # I don't think we can do any better for now
                print 'Saving page'
                p = Page(book=translation, chapter=chapter,
                        page_number=pagenum, image_path=image_path, text=text)
                p.save()



if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-d', '--base-dir',
            dest='base_dir',
            help='Path to base directory of image files',
            )
    parser.add_option('-t', '--book-title',
            dest='title',
            help='Title of the book'
            )
    parser.add_option('-l', '--language',
            dest='language',
            help="Language that the book is in"
            )
    options, args = parser.parse_args()
    if options.language == 'Slovene':
        tesseract_language = 'slv'
    main(options.base_dir, options.title, options.language, tesseract_language)

# vim: et sw=4 sts=4
