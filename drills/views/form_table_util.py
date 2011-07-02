#!/usr/bin/env python


def create_table(verb, person, number):
    language = verb.word.wordlist.language
    conj_cls = __import__(language.module_name).mapping[verb.conjugation.name]
    conj = conj_cls(verb.word.word, verb.id)
    args = {}

    moods = [m.name for m in language.mood_set.all()]
    voices = [v.name for v in language.voice_set.all()]
    tenses = [t.name for t in language.tense_set.all()]

    table = '<table>'
    table += '<thead>'
    table += '<tr><th></th>'
    for mood in moods:
        table += '<th>%s</th>' % mood
    table += '</tr>'
    table += '</thead>'


    for voice in voices:
        args['voice'] = voice
        table += '<tbody>'
        for tense in tenses:
            args['tense'] = tense
            table += '<tr>'
            table += '<th>%s %s</th>' % (tense, voice)
            for mood in moods:
                args['mood'] = mood
                if mood == 'Infinitive':
                    args['person'] = 'None'
                    args['number'] = 'None'
                else:
                    args['person'] = person
                    args['number'] = number
                try:
                    forms = conj.conjugate(**args)
                    form = forms[0]
                except ValueError as e:
                    form = '-'
                table += '<td>%s</td>' % form
            table += '</tr>'
        table += '</tbody>'

    table += '</table>'
    return table

# vim: et sw=4 sts=4
