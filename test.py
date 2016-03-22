import os

import clipmon
import conf

with open('test_whitelist.txt') as f:
    conf.test_whitelist = set(f.read().splitlines())

with open('test_cases.txt') as f:
    lines = f.read().splitlines()

for i in range(0, len(lines), 3):
    test_line, expected = lines[i:i+2]
    if expected == 'None':
        expected = None
    actual = clipmon.clip_str_to_path_line(test_line)
    # expected, actual = [
    #     os.path.expanduser(s.replace('<proj_dir>', proj_dir))
    #     if s else None for s in (expected, actual)]
    print 'line:    ', test_line
    print 'expected:', expected
    print 'actual:  ', actual
    print
    assert actual == expected

print 'ohhh yeahhh'
