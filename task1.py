#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

from collections import defaultdict


def group_by(stream, field, success=None):

	answer = defaultdict(lambda :0)
	old = None

	if success is not None:
		success = 'S' if success else 'F'

	for line in stream:
		if line.startswith('#'): # ignore comments
			pass
		elif line.startswith(' '): # last line is continued
			if old is not None:
				answer[old]+=1
		else:
			line_yms = {
			'year': line[13:17], 
			'month': line[18:21],
			'success': line[193],
			}

			if (success is None) or (success == line_yms['success']):
				answer[line_yms[field]] += 1
				old = line_yms[field] # last one was ok, so add again
			else:
				old = None # last one was wrong, so ignore continuation

	return dict(answer)
