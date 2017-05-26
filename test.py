import os, shutil

import clipmon
import conf


test_paths = [
  '~/Dropbox/CardBrew/03_move/tests/move_test.js',
  '~/Dropbox/CardBrew/01_chars/chars.js',
  '~/Dropbox/CardBrew/src/02_commands_server/command_listener.js',
  '~/Dropbox/CardBrew/src/01_server/tests/test_server.js',
  '~/Dropbox/CardBrew/src/00_game/00_game.js',
  '~/gigwalk/apps/gigwalk_apps_platform_api/tests/api_app/templates/test_controller.py',
  (
    '~/gigwalk/apps/gigwalk_apps_platform_api/gigwalk_api_app/organization_location_lists/'
    'resources.py'
  ),
  '~/gigwalk/apps/gigwalk_apps_platform_api/back/lib/python2.7/site-packages/_pytest/config.py',
  '~/gigwalk/apps/gigwalk_apps_platform_api/gigwalk_api_app/lib/gigwalk_api.py',
  '~/gigwalk/apps/gigwalk_apps_platform_api/back/lib/python2.7/site-packages/_pytest/core.py',
  '~/gigwalk/apps/api-tests/test/index.js',
  '~/airlab/repos/rookery/app/mailers/homes_collections_mailer.rb',
  '/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/subprocess.py',
]
paths_to_rm = []
for path in test_paths:
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        paths_to_rm.append(path)
        dir_path = os.path.dirname(path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with open(path, 'w') as f:
            f.write('')

try:

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
finally:
    for path in paths_to_rm:
        os.remove(path)
        for _ in range(100000):
            if not path:
                break
            path = os.path.dirname(path)
            if os.listdir(path):
                break
            os.rmdir(path)
