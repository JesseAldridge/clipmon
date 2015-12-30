import os

# ----- Specify your configuration here. -----

curr_proj_dir = '/Users/jessealdridge/gigwalk/apps/gigwalk_apps_platform_api'

# editor_cmd = '/usr/local/bin/atom'
editor_cmd = os.path.expanduser('~/Dropbox/bin/subl')

# ----- End of your configuration. ------

if not curr_proj_dir.endswith('/'):
  curr_proj_dir += '/'
