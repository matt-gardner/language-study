#!/usr/bin/env python
# -*- encoding: utf-8 -*-

verbs = dict()
verbs['aggello'] = u'ἀγγέλλω, ἀγγελῶ, ἤγγειλα, ἤγγελκα, ἤγγελμαι, ἠγγέλθην'
verbs['aischunomai'] = u'αἰσχύνομαι, αἰσχυνοῦμαι, _, _, ᾔσχυμμαι, ᾐσχύνθην'
verbs['dhloo'] = u'δηλόω, δηλώσω, ἐδήλωσα, δεδήλωκα, δεδήλωμαι, ἐδηλώθην'
verbs['elauno'] = u'ἐλαύνω, ἐλάω, ἤλασα, ἐλήλακα, ἐλήλαμαι, ἠλάθην'
verbs['elegxo'] = u'ἐλέγχω, ἐλέγξω, ἤλεγξα, _, ἐλήλεγμαι, ἠλέγχθην'
verbs['ethelo'] = u'ἐθέλω, ἐθελήσω, ἠθέλησα, ἠθέληκα, _, _'
verbs['faino'] = u'φαίνω, φανῶ, ἔφηνα, πέφηνα, πέφασμαι, ἐφάνην'
verbs['fobeomai'] = u'φοβέομαι, φοβήσομαι, _, _, πεφόβημαι, ἐφοβήθην'
verbs['grafo'] = u'γράφω, γράψω, ἔγραψα, γέγραφα, γέγραμμαι, ἐγράφην'
verbs['keleuo'] = u'κελεύω, κελεύσω, ἐκέλευσα, κεκέλευκα, κεκέλευσμαι, '
verbs['keleuo'] += u'ἐκελεύσθην'
verbs['maxomai'] = u'μάχομαι, μαχοῦμαι, ἐμαχεσάμην, _, μεμάχημαι, _'
verbs['nikao'] = u'νικάω, νικήσω, ἐνίκησα, νενίκηκα, νενίκημαι, ἐνικήθην'
verbs['paideuo'] = u'παιδεύω, παιδεύσω, ἐπαίδευσα, πεπαίδευκα, πεπαίδευμαι,'
verbs['paideuo'] += u' ἐπαιδεύθην'
verbs['pempo'] = u'πέμπω, πέμψω, ἔπεμψα, πέπομφα, πέπεμμαι, ἐπέμφθην'
verbs['poieo'] = u'ποιέω, ποιήσω, ἐποίησα, πεποίηκα, πεποίημαι, ἐποιήθην'
verbs['tatto'] = u'τάττω, τάξω, ἔταξα, τέταχα, τέταγμαι, ἐτάχθην'

cases = [{'person': 'First Person', 'number': 'Singular'}]
cases.append({'person': 'Second Person', 'number': 'Singular'})
cases.append({'person': 'Third Person', 'number': 'Singular'})
cases.append({'person': 'First Person', 'number': 'Plural'})
cases.append({'person': 'Second Person', 'number': 'Plural'})
cases.append({'person': 'Third Person', 'number': 'Plural'})

from attic_greek.test_modules import consonant_stems
from attic_greek.test_modules import contracted
from attic_greek.test_modules import contracted_future
from attic_greek.test_modules import regular
from attic_greek.test_modules import vowel_augment

all_tests = []
all_tests.extend(consonant_stems.all_tests)
all_tests.extend(contracted.all_tests)
all_tests.extend(contracted_future.all_tests)
all_tests.extend(regular.all_tests)
all_tests.extend(vowel_augment.all_tests)

# vim: et sw=4 sts=4
