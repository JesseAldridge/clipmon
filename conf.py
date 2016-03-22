import os

# ----- Specify your configuration here. -----

curr_proj_dirs = [
  '/Users/jessealdridge/Dropbox/gigwalk/apps/gigwalk_apps_platform_api',
  '/Users/Jesse/Dropbox/CardBrew'
]

# editor_cmd = '/usr/local/bin/atom'
editor_cmd = os.path.expanduser('~/Dropbox/bin/subl')

# ----- End of your configuration. ------

test_whitelist = set()
curr_proj_dirs = [s + '/' if not s.endswith('/') else s for s in curr_proj_dirs]
