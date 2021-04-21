# Trello CLI in Python

Trello CLI is a program that adds cards to the trello.com board. This program takes user input and adds a trello card with labels and comments to the specified column on the board.

## Download 

After downloading the fileuser will need to unzip the 

## Installation
Install Trello CLI by running in the root directory:

```shell script
pip install .
```

## Usage
Authentication credentials need to be gotten. users can get the key and token for authentication from your own account. Create a trello account if they do not have one and visit https://trello.com/app-key to generate your own key and token.

To add card to the board run Trello CLI using:

```shell script
trello_cli card new <column_id> <key> <token>  [--comment_text=<ct>] [--label_id=<li>] [--title=<t>]
```
To get the Column ID

```shell script
trello_cli column show <board_id> <key> <token>
```

To get the Board ID 

```shell script
trello_cli board show <key> <token>
```

To get the label ID

```shell script
trello_cli label show <board_id> <key> <token>
```
Title, Label ID and comments are set to optional and CLI will still run fine without specifying that. So you can add card to the program without specifying the label and comment.

## Next development Steps
For next development step, We could package and deploy to Python Package Index - PyPi.
It will have been nice to write a unit test for this code base but it is not important right now as the code is not large enough to allow mocking and isolating commands. 
