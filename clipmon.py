#!/usr/bin/python
import time, sys, os, subprocess, re, traceback
from datetime import datetime

import pyperclip

import conf


def clip_str_to_path_line(clip_str, path_exists=os.path.exists):
  if clip_str.count('\n') > 1:
    return

  for f in test_replacements, test_partial_path:
    result_line = f(clip_str, path_exists)
    if result_line:
      return result_line

def test_replacements(clip_str, path_exists):
  replaced_str = clip_str
  for find_regex, replace_str in conf.find_replace_map:
    replaced_str = re.sub(find_regex, replace_str, replaced_str)

  match = re.search(
    #                 file extension
    #    path               |
    #     |                 |
    r'((?:~|/)[^@^:^\\^\(]+\.[a-z]{2,3}).*(?:line.*?|\()([0-9]+)', replaced_str)
  if match and path_exists(os.path.expanduser(match.group(1))):
    return ':'.join([match.group(1), match.group(2)])

  match = re.search(
    #                file extension
    #   path              |
    #    |                |
    r'((?:~|/)[^@^:^\\^\(]+\.[a-z]{2,3}):([0-9]+)', replaced_str)
  if match and path_exists(os.path.expanduser(match.group(1))):
    return ':'.join([match.group(1), match.group(2)])

def test_partial_path(clip_str, path_exists):
  match = re.search(
    r'([a-zA-Z_/\-\.0-9]+/[a-zA-Z_0-9\-]+\.[a-z]{2,3}).*?(line.*?|:)([0-9]+)', clip_str)
  if match:
    partial_path = match.group(1)
    if partial_path.startswith('./'):
      partial_path = partial_path.replace('./', '')
    for proj_dir in conf.curr_proj_dirs:
      full_path = os.path.join(proj_dir, partial_path)
      if path_exists(os.path.expanduser(full_path)):
        return ':'.join([full_path, match.group(3)])


if __name__ == '__main__':
  try:
    clip_str = None
    is_first_run = True
    while True:
      prev_value = clip_str
      try:
        if not is_first_run:
          time.sleep(1)
        is_first_run = False
        clip_str = pyperclip.paste()
        # (the value that was initially on clipboard before running script)
        if prev_value is None:
          prev_value = clip_str
      except UnicodeDecodeError:
        pass
      else:
        if clip_str == prev_value:
          continue
        print 'new value:', clip_str
        path_line = clip_str_to_path_line(clip_str)
        if path_line:
          subprocess.Popen([conf.editor_cmd, path_line])
  except Exception as e:
    import Tkinter
    import tkMessageBox

    window = Tkinter.Tk()
    window.wm_withdraw()
    exception_str = traceback.format_exc()
    print 'exception_str:', exception_str
    tkMessageBox.showinfo(title="Error", message="{}\n{}".format(
      str(e), exception_str))

    sys.stderr.write(str(datetime.now()) + '\n')

    raise
