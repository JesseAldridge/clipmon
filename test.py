import clipmon

with open('test_cases.txt') as f:
  lines = f.read().splitlines()

for i in range(0, len(lines), 3):
  test_line, expected = lines[i:i+2]
  if expected == 'None':
    expected = None
  actual = clipmon.clip_str_to_path_line(test_line)
  print 'line:    ', test_line
  print 'expected:', expected
  print 'actual:  ', actual
  print
  assert actual == expected

print 'ohhh yeahhh'
