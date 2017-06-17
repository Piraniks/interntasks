#!/usr/bin/env python3

from collections import OrderedDict


def damage(spell):

    start_index = spell.find('fe') + 2  # +2 to remove first 'fe' from spell
    end_index = spell.rfind('ai')

    # order of 'fe' 'ai' matters, both must be in a spell
    if start_index != -1 and end_index != -1 and end_index >= start_index: 
        valid_spell = spell[start_index:end_index]

        if 'fe' in valid_spell:
            return 0
        else:
            # order in the book matters for biggest "spellpower" possible
            word_book = OrderedDict([ 
                ('dai', 5),
                ('ne', 2),
                ('ain', 3),
                ('ai', 2),
                ('jee', 3),
                ('je', 2),
                ])
            dmg = 3

            # process the actual spell
            for word in word_book:
                dmg += valid_spell.count(word) * word_book[word]
                valid_spell = valid_spell.replace(word, ' ')

            valid_spell = valid_spell.replace(' ', '')
            dmg -= len(valid_spell)

            return max(dmg, 0)
    else:
        return 0
