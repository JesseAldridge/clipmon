import os

# ----- Specify your configuration here. -----

find_replace_map = (
  ('/Users/[a-zA-Z]+/', '~/'),
  ('/mnt/airlab/repos', '~/airlab/repos'),
  ('http://localhost:5000/', '~/Dropbox/CardBrew/')
)

curr_proj_dirs = [
  '~/airlab/repos/airbnb',
  '~/airlab/repos/rookery',
  '~/gigwalk/apps/gigwalk_apps_platform_api/',
  '~/Dropbox/CardBrew/'
]

# editor_cmd = '/usr/local/bin/atom'
editor_cmd = os.path.expanduser('~/Dropbox/bin/subl')

# ----- End of your configuration. ------

curr_proj_dirs = [s + '/' if not s.endswith('/') else s for s in curr_proj_dirs]
