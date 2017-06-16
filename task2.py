#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

from collections import OrderedDict


def damage(spell):

	start_index = spell.find('fe') + 2 # without +2 it would contain the first 'fe'
	end_index = spell.rfind('ai')

	if start_index != -1 and end_index != -1 and end_index >= start_index: # order of 'fe' 'ai' matters, both must be in a spell
		valid_spell = spell[start_index:end_index]

		if 'fe' in valid_spell:
			return 0
		else:
			word_book = OrderedDict([ # order in the book matters for biggest "spellpower" possible for The One
			('dai', 5),
			('ne', 2),
			('ain', 3),
			('ai', 2),
			('jee', 3),
			('je', 2),
			])
			damage = 3

			# process the actual spell
			for word in word_book:
				damage += valid_spell.count(word) * word_book[word]
				valid_spell = valid_spell.replace(word, ' ')

			valid_spell = valid_spell.replace(' ', '')
			damage -= len(valid_spell)

			return max(damage, 0)
	else:
		return 0
