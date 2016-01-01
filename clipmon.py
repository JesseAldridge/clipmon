#!/usr/bin/python
import time, sys, os, subprocess, re, traceback
from datetime import datetime

import pyperclip

import conf

def clip_str_to_path_line(clip_str):
  clip_str = clip_str.replace('http://localhost:5000/', os.path.expanduser(conf.curr_proj_dir))
  if clip_str.count('\n') > 1:
    return

  # test full path
                    #               file extension
                    #      path            |
                    #       |              |
  match = re.search(r'[^\w](/[^@^:^\\^\(]+\.[a-z]{2,3})[^:]{0,9}(line.*?|:|\()([0-9]+)', clip_str)
  if match:
    return ':'.join([match.group(1), match.group(3)])

  # test partial path
  match = re.search(
    r'([a-zA-Z_/\-\.0-9]+/[a-zA-Z_0-9\-]+\.[a-z]{2,3})[^:]{0,9}(line.*?|:)([0-9]+)', clip_str)
  if match:
    return ':'.join([os.path.join(conf.curr_proj_dir, match.group(1)), match.group(3)])

if __name__ == '__main__':
  try:
    clip_str = None
    while True:
      prev_value = clip_str
      try:
        clip_str = pyperclip.paste()
        # (the value that was initially on clipboard before running script)
        if prev_value is None:
          prev_value = clip_str
      except UnicodeDecodeError:
        pass
      else:
        if clip_str != prev_value:
          print 'new value:', clip_str
          path_line = clip_str_to_path_line(clip_str)
          if path_line:
            subprocess.Popen([conf.editor_cmd, path_line])
      time.sleep(0.5)
  except Exception as e:
    import Tkinter
    import tkMessageBox

    window = Tkinter.Tk()
    window.wm_withdraw()
    exception_str = traceback.format_exc()
    print 'exception_str:', exception_str
    tkMessageBox.showinfo(title="Error", message="{}\n{}".format(
      e.strerror, exception_str))

    sys.stderr.write(str(datetime.now()) + '\n')
    raise

    raise
