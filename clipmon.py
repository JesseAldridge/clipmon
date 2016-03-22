#!/usr/bin/python
import time, sys, os, subprocess, re, traceback
from datetime import datetime

import pyperclip

import conf


def clip_str_to_path_line(clip_str):
    if clip_str.count('\n') > 1:
        return
    # test full path
    result_line = test_full_match(clip_str)
    if result_line:
        return result_line
    else:
        for proj_dir in conf.curr_proj_dirs:
            replaced_str = clip_str.replace('http://localhost:5000/', proj_dir)
            result_line = test_full_match(replaced_str)
            if result_line:
                return result_line

    # test partial path
    match = re.search(
        r'([a-zA-Z_/\-\.0-9]+/[a-zA-Z_0-9\-]+\.[a-z]{2,3})[^:]{0,9}(line.*?|:)([0-9]+)', clip_str)
    if match:
        partial_path = match.group(1)
        if partial_path.startswith('./'):
            partial_path = partial_path.replace('./', '')
        for proj_dir in conf.curr_proj_dirs:
            full_path = os.path.join(proj_dir, partial_path)
            if path_exists(full_path):
                return ':'.join([full_path, match.group(3)])

def test_full_match(clip_str):
    match = re.search(
        #             file extension
        # path            |
        #  |              |
        r'(/[^@^:^\\^\(]+\.[a-z]{2,3})[^:]{0,9}(line.*?|:|\()([0-9]+)', clip_str)
    if match and path_exists(match.group(1)):
        return ':'.join([match.group(1), match.group(3)])

def path_exists(path):
    return path in conf.test_whitelist if conf.test_whitelist else os.path.exists(path)


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
                if clip_str == prev_value:
                    continue
                print 'new value:', clip_str
                path_line = clip_str_to_path_line(clip_str)
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
            str(e), exception_str))

        sys.stderr.write(str(datetime.now()) + '\n')

        raise
