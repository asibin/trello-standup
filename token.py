import trello

from settings import API_KEY

trello = trello.TrelloApi(API_KEY)
print "To get your token go here: " + trello.get_token_url('Trello-standup')

