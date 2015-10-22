#!/usr/bin/python
import time, sys, os, subprocess, re

import clipboard

def clip_str_to_path_line(clip_str):
  if clip_str.count('\n') > 1:
    return
                          # file extension
                    # a path |
  match = re.search('(/[^@]+\.[a-z]{2,3})[^:]*(line.*?|:)([0-9]+)', clip_str)
  if match:
    return ':'.join([match.group(1), match.group(3)])

if __name__ == '__main__':
  clip_str = None
  while True:
    prev_value = clip_str
    clip_str = clipboard.paste()
    if prev_value is not None and clip_str != prev_value:
      print 'new value:', clip_str
      path_line = clip_str_to_path_line(clip_str)
      if path_line:
        print 'got path_line:', path_line
        subprocess.Popen(['/usr/local/bin/atom', path_line])
    time.sleep(0.5)
