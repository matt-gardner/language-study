#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from scrape import urlopen_with_chrome
from BeautifulSoup import BeautifulSoup

def get_definition_from_pons(word):
    url = 'http://en.pons.eu/dict/search/results/?q=%s&l=ensl&in=&lf=en' % (
            word)
    html = urlopen_with_chrome(url.encode('utf-8'))
    soup = BeautifulSoup(html)
    senses = []
    for sense in soup.findAll('span', attrs={'class':'sense'}):
        if sense.parent.name == 'th':
            table = sense.parent.parent.parent.parent
        else:
            table = sense.parent.parent.parent
        senses.append((sense, table))
    for sense, table in senses:
        print ''.join(sense.parent.findAll(text=True)).strip()
        for target in table.findAll('td', attrs={'class':'target'}):
            source = target.findPreviousSibling('td', attrs={'class': 'source'})
            print ''.join(source.findAll(text=True)).strip(), ':',
            print ''.join(target.findAll(text=True)).strip()
        print
    if not senses:
        for target in soup.findAll('td', attrs={'class':'target'}):
            source = target.findPreviousSibling('td', attrs={'class': 'source'})
            print ''.join(source.findAll(text=True)).strip(), ':',
            print ''.join(target.findAll(text=True)).strip()


if __name__ == '__main__':
    get_definition_from_pons(u'davčen')
    print '\n'
    get_definition_from_pons('porabiti')
    print '\n'
    get_definition_from_pons('paziti')

# vim: et sw=4 sts=4
