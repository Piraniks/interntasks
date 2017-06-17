#!/usr/bin/env python3

from collections import defaultdict


def group_by(stream, field, success=None):

    answer = defaultdict(lambda: 0)
    last = None

    if success is not None:
        success = 'S' if success else 'F'

    for line in stream:
        if line.startswith('#'):  # ignore comments
            pass
        elif line.startswith(' '):  # last line is continued
            if last is not None:
                answer[last] += 1
        else:
            line_data = {
                'year': line[13:17],
                'month': line[18:21],
                'success': line[193],
                }

            if success is None or success == line_data['success']:
                last = line_data[field]  # last one was ok, so add again
                answer[last] += 1
            else:
                last = None  # last one was wrong, so ignore continuations

    return dict(answer)
