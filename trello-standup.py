import trello
import os
import subprocess
import logging
import sys

from settings import API_KEY, BOARD_ID, TOKEN, USER, WORKDIR, NR_LAST_DAYS, GIT_STANDUP_PATH, BLACKLIST
from datetime import date

trello_api = trello.TrelloApi(API_KEY, token=TOKEN)
logging.basicConfig()
logger = logging.getLogger(__name__)


def get_user_list():
    trello_lists = trello_api.boards.get_list(BOARD_ID)
    logger.debug("Searching for user: " + USER)
    for trello_list in trello_lists:
        if USER in trello_list['name']:
            logger.debug("This is your list ID: " + trello_list['id'])
            return trello_list['id']


def git_standup():
    os.chdir(WORKDIR)
    p = subprocess.Popen([GIT_STANDUP_PATH, '-d', str(NR_LAST_DAYS), '-D', 'short', '-a', USER],
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    com = p.communicate()
    if com[1] == '':
        return com[0]
    else:
        logging.info('Getting git log from git standup failed with error: %s', str(com[1]))
        sys.exit(1)


def write_card_comment(git_log_data, card_id):
    comment_text = []
    project_name = ''
    for line in git_log_data.split('\n'):
        if line.startswith(WORKDIR):
            if len(comment_text) > 0 and project_name not in BLACKLIST:
                trello_api.cards.new_action_comment(card_id, "\n".join(comment_text))
            project_name = line.split('/')[-1]
            comment_text = []
            if project_name in BLACKLIST:
                continue
            comment_text.append(project_name)
        else:
            comment_text.append(line.replace('<{}>'.format(USER), '' ))


def get_week_number():
    today_date = date.today()
    return date.isocalendar(today_date)[1]


def create_master_card():
    list_id = get_user_list()
    week_number = str(get_week_number())
    week_name = "Week {}".format(week_number)
    board_list = trello_api.lists.get_card(list_id=list_id)

    if any(week_name in card['name'] for card in board_list):
        logger.debug("Need to create comment on existing card")
        for card in board_list:
            if card['name'] == week_name:
                write_card_comment(git_standup(), card['id'])
                logger.debug("Comment created!")
    else:
        logger.debug("Create new card")
        new_card = trello_api.lists.new_card(list_id=list_id, name=week_name)
        text = "TEST"
        write_card_comment(git_standup(), new_card['id'])
        logger.debug("Created new card: {} and added comment\n{}".format(new_card['id'], text))

if __name__ == '__main__':
    create_master_card()
