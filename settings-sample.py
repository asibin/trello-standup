# Get one on https://trello.com/app-key
API_KEY = 'aaaaaaaaaaaaaaaaaaaaaaaa'

# Generate user token
# run >> python token.py to get url where you can generate your token
TOKEN = 'bbbbbbbbbbbbbbbbbbbbbbb'

# Board ID - currently manual, will automate getting it from name
# Get board id at https://developers.trello.com/sandbox, sign in with your api key, click authenticate, click execute
# on Get Boards method and get id for your board (there could be a better way :D)
BOARD_ID = 'cccccccccccccccccccccccc'

# Your username as in list name for example "Weekly Updates Sibin Arsenijevic"
USER = "Sibin Arsenijevic"

# Absolute path to your projects folder, i.e. where all your tracked projects are stored
WORKDIR = "/Users/sibin/workspace"

# Number of days git standup should show
NR_LAST_DAYS = 5

# Path to git standup
GIT_STANDUP_PATH = '/usr/local/bin/git-standup'

# List of repos to exclude from reporting
BLACKLIST = ['dotfiles']
