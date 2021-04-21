'''
Trello @ Canonical.

Usage:
  trello_cli board show <key> <token>
  trello_cli column show <board_id> <key> <token>
  trello_cli label show <board_id> <key> <token>
  trello_cli card new <column_id> <key> <token>  [--comment_text=<ct>] [--label_id=<li>] [--title=<t>]
  trello_cli -h | --help

Options:
  -h --help     Show this screen.

'''

from docopt import docopt
import requests

URL = "https://api.trello.com/1"

class Trello:
    def __init__(self, key, token):
        self.key = key
        self.token = token
    
    def list_boards_id(self):
        r = requests.get(f"{URL}/members/me/boards?key={self.key}&token={self.token}")   
        if r.status_code == 200:
            boards = r.json()
            return [{"id": board["id"], "name": board["name"]} for board in boards]    
        
        print("Unable to list boards")
        return None
    
    def list_column_ids(self, board_id):
        r = requests.get(f"{URL}/boards/{board_id}/lists?key={self.key}&token={self.token}")   
        if r.status_code == 200:
            columns = r.json()
            return [{"id": column["id"], "name": column["name"]} for column in columns]  

        print("Unable to list columns")            
        return None

    def list_label_ids(self, board_id):
        r = requests.get(f"{URL}/boards/{board_id}/labels?key={self.key}&token={self.token}")   
        if r.status_code == 200:
            labels = r.json()
            return [{"id": label["id"], "color": label["color"]} for label in labels] 
          
        print("Unable to list labels")            
        return None

    def create_card(self, column, title, comment, label):
        r = requests.post(f"{URL}/cards", data={"key": self.key, "token": self.token, "name": title, "idList": column})
        if r.status_code == 200:
            card_id = r.json()["id"]

            # add label to the card
            if label:
                rl = requests.post(f"{URL}/cards/{card_id}/idLabels",  data={"key": self.key, "token": self.token, "value": label})
                if rl.status_code != 200:
                    print("Unable to add label to card")

            # add comments to the card
            if comment:
                rc = requests.post(f"{URL}/cards/{card_id}/actions/comments",  data={"key": self.key, "token": self.token, "text": comment})
                if rc.status_code != 200:
                    print("Unable to add comments tot the card")

            return card_id

        print("Unable to create card")
        return None

def printing_loop(obj_array):
    print("Please select the desired ID:\n")
    for objname in obj_array:
        for k, v in objname.items():
            print('{}: {}'.format(k, v))
        print("\n")

def cli():
    args = docopt(__doc__)

    # authentication information
    key = args["<key>"]
    token = args["<token>"]

    # initialize Trello
    trello = Trello(key, token)
    
    # get board information before adding the card into the board
    if args['board'] and args['show']:
        # show user the board info
        boards = trello.list_boards_id()
        #print(boards) 
        printing_loop(boards)

    # get column information before adding the card into the board
    if args['column'] and args['show']:
        # show users the list info
        board = args["<board_id>"]
        columns = trello.list_column_ids(board)
        printing_loop(columns)

    # get label information before adding the card into the board
    if args['label'] and args['show']:
        # show users the boards info
        board = args["<board_id>"]
        labels = trello.list_label_ids(board)
        printing_loop(labels)
      
              
    if args['card']:
        column = args["<column_id>"]
        title = args["--title"]
        label = args["--label_id"]
        comment = args["--comment_text"]
        card = trello.create_card(column, title, comment, label)
        print(card)


if __name__ == "__main__":
    cli()