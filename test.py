import os, shutil

import clipmon
import conf

1/0
test_paths = {os.path.expanduser(path) for path in (
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
)}

def path_exists(path):
  return path in test_paths

with open('test_cases.txt') as f:
  lines = f.read().splitlines()

for i in range(0, len(lines), 3):
  test_line, expected = lines[i:i+2]
  if expected == 'None':
    expected = None
  actual = clipmon.clip_str_to_path_line(test_line, path_exists)
  print 'line:  ', test_line
  print 'expected:', expected
  print 'actual:  ', actual
  print
  assert actual == expected

print 'ohhh yeahhh'
