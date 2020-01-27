'''
	Cinnamon Fresh
	Tic-Tac-Tournament
	main.py
	-----------------------------------------------------------------------
	The main backend function in python to handle the game logic and
	maintaining client information.
	-----------------------------------------------------------------------
	Sources:
		1. 	https://github.com/samhita-alla/flask-chat-app-article
		2. 	https://stackoverflow.com/questions/3056048/filename-and-line-number-of-python-script
		3. 	https://stackoverflow.com/questions/492387/indentationerror-unindent-does-not-match-any-outer-indentation-level
		4. 	https://stackoverflow.com/questions/37977250/node-js-socket-io-only-accessible-through-localhost
		5. 	https://stackoverflow.com/questions/45880348/how-to-remove-the-cause-of-an-unexpected-indentation-warning-when-generating-cod
		6. 	https://www.w3schools.com/js/js_loop_for.asp
		7. 	https://stackoverflow.com/questions/20261276/flask-creating-a-unique-profile-page-for-each-user
		8. 	https://stackoverflow.com/questions/39912455/passing-random-numbers-into-template-from-flask-python
		9. 	https://flask.palletsprojects.com/en/1.1.x/api/#flask.url_for
		10.	https://teamtreehouse.com/community/why-do-we-need-redirect-in-flask
		11.	https://www.freecodecamp.org/forum/t/setting-up-a-whitelist-in-mongo-db-atlas/236842
		12.	https://stackoverflow.com/questions/1186789/what-is-the-best-way-to-call-a-script-from-another-script
		13.	https://docs.mongodb.com/manual/reference/method/db.collection.find/
		14.	https://stackoverflow.com/questions/28981718/collection-object-is-not-callable-error-with-pymongo
		15.	https://docs.python-guide.org/scenarios/serialization/
		16.	https://stackoverflow.com/questions/46406225/pymongo-error-filter-must-be-an-instance-of-dict-bson-son-son-or-other-type-t
		17.	https://api.mongodb.com/python/current/tutorial.html
		18.	https://docs.mongodb.com/manual/reference/method/db.collection.findOne/
		19.	https://stackoverflow.com/questions/17256602/assertionerror-view-function-mapping-is-overwriting-an-existing-endpoint-functi
		20.	https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/
		21.	https://stackoverflow.com/questions/44060207/builderror-could-not-build-url-for-endpoint-user-with-values-nickname-di
		22.	https://pythonise.com/series/learning-flask/generating-dynamic-urls-with-flask
		23.	https://www.reddit.com/r/flask/comments/6dz044/ask_flask_how_to_use_redirecturl_for_when_my/
		24.	https://stackoverflow.com/questions/38926335/flask-redirecturl-for-returning-html-but-not-loading-page
		25.	https://medium.com/techkylabs/getting-started-with-python-flask-framework-part-1-a4931ce0ea13
		26.	https://junxiandoc.readthedocs.io/en/latest/docs/flask/flask_routing.html
		27.	https://pythonise.com/series/learning-flask/generating-dynamic-urls-with-flask
		28.	https://overiq.com/flask-101/creating-urls-in-flask/
		29.	https://www.javatpoint.com/flask-templates
		30.	https://stackoverflow.com/questions/15473626/make-a-post-request-while-redirecting-in-flask
		31.	https://www.programcreek.com/python/example/51520/flask.redirect
		32.	https://stackoverflow.com/questions/46123448/how-do-decorated-functions-work-in-flask-python-app-route
		33.	https://stackoverflow.com/questions/37524203/flask-redirect-does-not-render-template-when-redirecting-from-a-post
		34.	https://stackoverflow.com/questions/34245814/flask-redirect-with-authentication
		35.	https://socket.io/docs/rooms-and-namespaces/
		36.	https://socket.io/get-started/chat
		37.	https://stackoverflow.com/questions/53807546/concise-example-of-how-to-join-and-leave-rooms-using-flask-and-socket-io
		38.	https://api.mongodb.com/python/current/api/pymongo/collection.html#pymongo.collection.Collection.find_one_and_replace
		39.	https://www.dotnetperls.com/find-one-mongodb
		40.	https://kb.objectrocket.com/mongo-db/how-to-find-and-replace-or-change-mongodb-documents-in-python-366
		41.	https://docs.mongodb.com/manual/reference/method/db.collection.replaceOne/
		42.	https://stackoverflow.com/questions/43290202/python-typeerror-unhashable-type-slice-for-encoding-categorical-data/43291257
		43.	https://api.mongodb.com/python/current/api/pymongo/collection.html
		44.	https://stackoverflow.com/questions/13794849/mongodb-how-to-search-based-on-two-parameters-in-mongo
		45.	https://railsless.blogspot.com/2013/04/pymongo-typeerror-index-password-cannot.html
		46.	https://stackoverflow.com/questions/35848688/whats-the-difference-between-replaceone-and-updateone-in-mongodb
		47.	https://kite.com/python/docs/pymongo.collection.Collection.update_one
		48.	https://stackoverflow.com/questions/55596266/invalid-syntax-issue-with-mongodb-update-query
		49.	https://api.mongodb.com/python/current/tutorial.html
		50.	https://docs.mongodb.com/manual/tutorial/update-documents/
		51.	https://note.nkmk.me/en/python-list-clear-pop-remove-del/
		52.	https://github.com/miguelgrinberg/Flask-SocketIO/issues/1017
		53. https://github.com/miguelgrinberg/flask-socketio/issues/40
		54.	https://www.journaldev.com/23232/python-add-to-dictionary
'''

# Package imports
from flask import Flask, render_template, redirect, url_for, request
import flask
from flask_socketio import SocketIO, emit, join_room, leave_room
import json
import logging
import inspect
import sys
import config
import pickle
from random import seed
from random import randint
from pymongo import MongoClient

# File imports
import FullBoard

# Get the config file
CONFIG = config.configuration()

# Set up the initial flask app
app = Flask(__name__, static_folder="../static", template_folder="../templates")
app.secret_key = CONFIG.SECRET_KEY

# Initialize socketio server
socketio = SocketIO(app, async_mode='threading')

# Set the mongodb URL
MONGO_CLIENT_URL = "mongodb://CFresh:{}@tic-tac-tournament-shard-00-00-bz500.mongodb.net:27017,tic-tac-tournament-shard-00-01-bz500.mongodb.net:27017,tic-tac-tournament-shard-00-02-bz500.mongodb.net:27017/test?ssl=true&replicaSet=Tic-Tac-Tournament-shard-0&authSource=admin&retryWrites=true&w=majority".format(CONFIG.DB_USER_PW)

# Try to access the database and collection that we need.
try: 
    dbclient = MongoClient(MONGO_CLIENT_URL)
    db = dbclient.TTT
    collection = db.lobbies

# If we can't access the database, close the program.
except:
    print("Failure opening database. Is Mongo running? Correct password?")
    sys.exit(1)

# Global variables
CLIENTS = []
LOBBIES = []
USERNAMES = {}
GAME_USERNAMES = {}

# The first page that loads when a user connects
@app.route('/', methods=['GET', 'POST'])
def sessions():
	'''
	Loads the initial lobby.html page.

	Arguments: 	None

	Returns: 	template renderer for the lobby.html page
	'''
	return render_template('lobby.html')

def getLineInfo():
	'''
	Helper function that prints out the file path, the line, and the function where it is called.
	Useful for generating error messages and debugging.

	Arguments: 	None

	Returns: 	None
	'''
	print("*** File: " + inspect.stack()[1][1],"; Line: ",inspect.stack()[1][2],"; Function: ",
		inspect.stack()[1][3])

# socketio connector for the clientConnectMsg event
@socketio.on('clientConnectMsg')
def sendClientConnect(id, methods=['GET', 'POST']):
	'''
	Handles when a client connects to the server. Creates a message for the
	server to say in chat. Adds a new player to the board that is this new
	client if the game isn't full.

	Arguments: 	id = the new client's id number
				methods = Get and post methods

	Returns: 	None
	'''
	global CLIENTS, LOBBIES, USERNAMES
	print("Client " + str(id) + " connected!")
	# Add the new client to the global clients list
	CLIENTS.append(str(id))
	# Has this socket join the main lobby's room.
	join_room(1)
	# Create a dictionary for the server message.
	msg = {
		"user_name" : "Server",
		"message" : USERNAMES[str(id)]["username"] + " connected!"
	}
	# Save the list of old lobbies for later reference.
	old_lobbies = LOBBIES
	# Wipe the global lobbies list
	LOBBIES = []
	# Loop through the database collection.
	for game in collection.find():
		# If the game isn't full...
		if (game["full"] == False):
			# Loop through the old list of lobbies
			for lob in old_lobbies:
				# If the current game id is the same as an old lobby's game id...
				if (str(game["game_id"]) == str(lob["game_id"])):
					# Append that lobby to the new global lobbies list.
					# We do all this so that we retain the old creators and update the lobbies list frequently
					LOBBIES.append({
						"game_id" : str(game["game_id"]),
						"creator" : lob["creator"]
					})
				else:
					continue

	# Emit to lobby.html that we want to print out the list of lobbies.
	socketio.emit('print lobby', {
		"lobbies" : LOBBIES, 
		"username" : USERNAMES[str(request.sid)]["username"]
	}, room=1)
	# Emit the server message dictionary to the server response event in
	# the html/javascript 
	socketio.emit('game server response', msg, room=1)

# socketio connector for the serverMsg event
@socketio.on('serverMsg')
def sendServerMsg(msg, game_id=1, methods=['GET', 'POST']):
	'''
	Handles when the server wants to send a message to the chat so that
	the clients can all see it, such as when a player wins.

	Arguments: 	msg = the message the server wants to send
				game_id = the game id where the message will be sent (defaults to the main lobby)
				methods = Get and post methods

	Returns: 	None
	'''
	# Dictionary that holds the information to write the message to the client.
	msg_dict = {
		"user_name" : "Server",
		"message" : msg
	}
	# Emit the message dictionary to the server response event.
	socketio.emit('server response', msg_dict, room=game_id)

# socketio connector for the send global message event
@socketio.on('send global message')
def handle_my_custom_event(json, game_id=1, methods=['GET', 'POST']):
	'''
	Handles when a client wants to send a message to the main lobby chat.

	Arguments: 	json = the message dict the client wants to send
				game_id = the game id where the message will be sent (defaults to the main lobby)
				methods = Get and post methods

	Returns: 	None
	'''
	print('received send message: ' + str(json))
	# Emit the message to lobby.html
	socketio.emit('my global response', json, room=game_id)

# socketio connector for the new lobby event
@socketio.on('new lobby')
def make_lobby(game_id=1, methods=['GET', 'POST']):
	'''
	Handles when a client clicks on the new lobby button. It creates the lobby and then redirects
	whoever made it into that lobby.

	Arguments: 	game_id = the game id where the message will be sent (defaults to the main lobby)
				methods = Get and post methods

	Returns: 	None
	'''
	global LOBBIES, USERNAMES
	# Create a new board
	tempBoard = FullBoard.FullBoard()
	# Generate a game_id which will also be the end of the url for the lobby.
	game_id = randint(100000, 999999)
	# Insert a new entry in the database that has a serialized board, the game_id, if it's full or not, and its users.
	collection.insert({"Board" : pickle.dumps(tempBoard), "game_id" : game_id, "full" : False, "users" : [USERNAMES[str(request.sid)]["username"]]})
	# Append to the lobbies list the game_id and the creator
	LOBBIES.append({
				"game_id" : str(game_id),
				"creator" : USERNAMES[str(request.sid)]["username"]
			})
	# Emit the print lobby event so that we refresh the lobbies with the new one included.
	socketio.emit('print lobby', {
		"lobbies" : LOBBIES, 
		"username" : USERNAMES[str(request.sid)]["username"]
	}, room=1)
	# Emit the auto join event so that the person who made the lobby joins it instantly. Send
	# it to just that client by giving its socket id as the room.
	socketio.emit('auto join', {
		"game_id" : str(game_id)
	}, room=request.sid)

# socketio connector for the join lobby event
@socketio.on('join lobby')
def join_lobby(game_id, methods=['GET', 'POST']):
	'''
	Handles when a client clicks on the join lobby button. It redirects the player to the lobby does
	some database saving to retain its username.

	Arguments: 	game_id = the game id where the message will be sent
				methods = Get and post methods

	Returns: 	None
	'''
	# Make an empty object to hold the database document
	documentHolder = None
	# Loop through the database...
	for i in collection.find():
		# If the game id matches...
		if i["game_id"] == game_id:
			# Copy the matching document into the empty object we made earlier
			documentHolder = i
			# Delete the document from the database so we can overwrite it.
			collection.delete_one(i)
			break
	# Add the username to the document.
	documentHolder["users"].append(USERNAMES[str(request.sid)]["username"])
	# Put it back into the database.
	collection.insert(documentHolder)

# socketio connector for the set name event
@socketio.on('set name')
def set_name(socket_id, name, methods=['GET', 'POST']):
	'''
	Gets the entered username and adds it to the global list of usernames, attached to its socket id

	Arguments: 	socket_id = The socket_id of the username we just got
				name = A string of the name we got for the user
				methods = Get and post methods

	Returns: 	None
	'''
	global USERNAMES
	# Check if the socket already has a username in the global list
	if socket_id in USERNAMES:
		# If it does already exist, change its old username to the new one.
		USERNAMES[str(socket_id)]["username"] = name
	else:
		# Otherwise, create a new entry that holds its username and sets it to being in the lobby.
		USERNAMES[str(socket_id)] = {"username" : name, "inLobby" : True}

# default socketio connector that is called when a socket disconnects
@socketio.on('disconnect')
def test_disconnect():
	'''
	Called when a user disconnects, sends a message if they're in a game, otherwise just print a message
	to the server so we don't spam the chat.

	Arguments: 	None

	Returns: 	None
	'''
	# If the socket is tied to a game username, then it's in a game and we can send a message to that game
	# saying they disconnected.
	if str(request.sid) in GAME_USERNAMES:
		# Print a message to the console and then send a message through the server to the chat saying they
		# disconnected.
		print("******* CLIENT " + GAME_USERNAMES[str(request.sid)]["username"] + " DISCONNECTED *********")
		g_sendServerMsg(str(GAME_USERNAMES[str(request.sid)]["username"] + " disconnected."), GAME_USERNAMES[str(request.sid)]["game_id"])
	else:
		print("******* CLIENT NOT IN LOBBY DISCONNECTED *********")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# The route for the game page which takes an int that is a game_id
@app.route('/index3/<int:game_id>', methods=['GET', 'POST'])
def index3(game_id):
	'''
	Loads the initial index3.html page.

	Arguments: 	None

	Returns: 	template renderer for the index3.html page
	'''
	return render_template("index3.html", game_id=game_id)

# socketio connector for the get username event
@socketio.on('get username')
def getUsername(game_id, _id, methods=['GET', 'POST']):
	'''
	Gets the username from the database after a client has moved into a game lobby.

	Arguments: 	game_id = The game id of the lobby the client just joined
				_id = The new socket id of the client
				methods = get and post methods

	Returns: 	None
	'''
	username = ""
	# Find the document in the collection that corresponds to the game
	documentHolder = collection.find_one({"game_id" : int(game_id)})
	dH2 = None
	# Have the socket join this game's room
	join_room(game_id)
	# If there is one player in the game...
	if (len(documentHolder["users"]) == 1):
		# Set the username as the first user in the users list
		username = documentHolder["users"][0]
	# If there are two players in the game...
	elif (len(documentHolder["users"]) == 2):
		# Set the username as the second user in the users list
		username = documentHolder["users"][1]
		# Delete the document from the database so we can update it.
		collection.delete_one(documentHolder)
		# Add a specatator user so we can assign all future people who join the lobby the role of spectator.
		documentHolder["users"].append("Spectator")
		# Put the document back into the database.
		collection.insert(documentHolder)
	# Otherwise a spectator joined...
	else:
		# Set the username as Spectator 'x' where x is the assigned number of the spectator, starting at 1.
		username = "Spectator " + str(len(documentHolder["users"]) - 2)
		# Refresh the document in the database and add another user so the right number of spectators appear.
		collection.delete_one(documentHolder)
		documentHolder["users"].append("Spectator")
		collection.insert(documentHolder)
	# Create a dictionary for the username and its new id
	json = {
		"user_name" : username,
		"_id" : _id
	}
	# Emit that dict to the change name event.
	socketio.emit('change name', json, room=game_id)

# socketio connector for the g_clientConnectMessage event ("g_" = game)
@socketio.on('g_clientConnectMsg')
def g_sendClientConnect(game_id, id, methods=['GET', 'POST']):
	'''
	Handles when a client connects to the server. Creates a message for the
	server to say in chat. Adds a new player to the board that is this new
	client if the game isn't full.

	Arguments: 	game_id = The game id of the lobby
				id = The new client's id number
				methods = Get and post methods

	Returns: 	None
	'''
	print("Client " + str(id) + " connected!")
	# Set a variable to the unserialized board in the database that corresponds to this game
	BOARD = pickle.loads(collection.find_one({"game_id" : int(game_id)})["Board"])
	# Create a dictionary for the server message.
	msg = {
		"user_name" : "Server",
		"message" : GAME_USERNAMES[str(id)]["username"] + " connected!"
	}
	# Emit the server message dictionary to the server response event in
	# index3.html
	socketio.emit('game server response', msg, room=game_id)

# socketio connector for the set game name event
@socketio.on('set game name')
def set_name(socket_id, name, game_id, methods=['GET', 'POST']):
	'''
	Adds the username and game_id into the game_usernames global list.

	Arguments: 	socket_id = the socket id of the user
				name = the user's name	
				game_id = The game id of the lobby
				methods = Get and post methods

	Returns: 	None
	'''
	global GAME_USERNAMES
	# Check if the user's socket_id is already in the game_usernames list.
	if socket_id in GAME_USERNAMES:
		# If it is, update that entry with the new name
		GAME_USERNAMES[str(socket_id)]["username"] = name
	else:
		# If it isn't, create a new entry for the new user
		GAME_USERNAMES[str(socket_id)] = {"username" : name, "inLobby" : True, "game_id" : game_id}

# socketio connector for the g_clientConnectStart event ("g_" = game)
@socketio.on('g_clientConnectStart')
def g_sendClientStart(game_id, id, methods=['GET', 'POST']):
	'''
	Handles when a client connects to the server. After it has connected and sent the message,
	add that player to the game.

	Arguments: 	game_id = The game id of the lobby
				id = The new client's id number
				methods = Get and post methods

	Returns: 	None
	'''
	global CLIENTS, LOBBIES, GAME_USERNAMES
	# Load and unserialize the board from the database
	BOARD = pickle.loads(collection.find_one({"game_id" : int(game_id)})["Board"])
	# If the board isn't running...
	if(not BOARD.running):
		# Add the player to the board
		BOARD.addplayer(str(id))
	# If it is running...
	if(BOARD.running):
		# Update the database entry so that it says the game is full.
		collection.update_one({"game_id" : int(game_id)}, {"$set": {"full" : True}})
		# Loop through the list of lobbies.
		for i in range(len(LOBBIES)):
			# If the game_id matches, delete it from the list so that it doesn't show up for
			# other users still on the main lobby screen.
			if LOBBIES[i]['game_id'] == game_id:
				LOBBIES.remove(LOBBIES[i])
		# Emit the print lobby event so that it refreshes the list of lobbies for the people in the main lobby.
		socketio.emit('print lobby', {
			"lobbies" : LOBBIES, 
			"username" : GAME_USERNAMES[str(request.sid)]["username"]
		}, room=1)
	# Create a server message json object that holds all the values the
	# javascript needs to show initial board info like turns
	try:
		json = {
			"space": None, 
			"player": BOARD.turn,
			"moves": list(BOARD.moves),
			"player_ID" : BOARD.turn_ID,
			"other_player_ID" : BOARD.other_ID,
			"username" : str(GAME_USERNAMES[str(BOARD.turn_ID)]["username"]),
			"other_username" : str(GAME_USERNAMES[str(BOARD.other_ID)]["username"])
		}
	# If no other_username is found, set it to none. This occurs when only one player has joined.
	except:
		json = {
			"space": None, 
			"player": BOARD.turn,
			"moves": list(BOARD.moves),
			"player_ID" : BOARD.turn_ID,
			"other_player_ID" : BOARD.other_ID,
			"username" : GAME_USERNAMES[str(request.sid)]["username"],
			"other_username" : "None"
		}
	# Update the board in the database.
	collection.update_one({"game_id" : int(game_id)}, {"$set": {"Board" : pickle.dumps(BOARD)}})
	# Emit the json object to the valid move event in index3.html
	socketio.emit('valid move', json, room=game_id)

# socketio connector for the serverMsg event ("g_" = game)
@socketio.on('serverMsg')
def g_sendServerMsg(msg, game_id, methods=['GET', 'POST']):
	'''
	Handles when the server wants to send a message to the chat so that
	the clients can all see it in the game, such as when a player wins.

	Arguments: 	msg = the message the server wants to send
				game_id = the id of the current game lobby
				methods = Get and post methods

	Returns: 	None
	'''
	# Dictionary that holds the information to write the message to the client.
	msg_dict = {
		"user_name" : "Server",
		"message" : msg
	}
	# Emit the message dictionary to the server response event.
	socketio.emit('game server response', msg_dict, room=game_id)

# socketio connector for the send game message event ("g_" = game)
@socketio.on('send game message')
def g_handle_my_custom_event(json, game_id, methods=['GET', 'POST']):
	'''
	Handles when a client in the game wants to send a message to the 
	rest of the lobby.

	Arguments: 	msg = the message the server wants to send
				game_id = the id of the current game lobby
				methods = Get and post methods

	Returns: 	None
	'''
	print('received game send message: ' + str(json))
	# Emit the my response event to index3.html
	socketio.emit('my response', json, room=game_id)

# socketio connector for the reset game event ("g_" = game)
@socketio.on('reset game')
def g_reset_game(game_id, methods=['GET', 'POST']):
	'''
	Handles when someone presses the reset game button in a game.

	Arguments: 	game_id = the id of the current game lobby
				methods = Get and post methods

	Returns: 	None
	'''
	# Load and unserialize the board into a new variable
	BOARD = pickle.loads(collection.find_one({"game_id" : int(game_id)})["Board"])
	# Set a variable to the players in the board
	tempPlayers = BOARD.players
	# Clear the board
	BOARD.clearState()
	# Add the players back in
	BOARD.addplayer(tempPlayers[0])
	BOARD.addplayer(tempPlayers[1])
	# Update the board in the database
	collection.update_one({"game_id" : int(game_id)}, {"$set": {"Board" : pickle.dumps(BOARD)}})
	# Emit the clear board event so that the board seen by the players matches the board in the dictionary
	socketio.emit('clear board', room=game_id)

# socketio connector for the value event ("g_" = game)
@socketio.on('value')
def g_handle_value(json, game_id, methods=['GET', 'POST']):
	'''
	Handles when someone presses a space on the board.

	Arguments: 	json = dictionary from index3.html which holds the button the user pressed
				game_id = the id of the current game lobby
				methods = Get and post methods

	Returns: 	None
	'''
	# Load and unserialize the board from the database
	BOARD = pickle.loads(collection.find_one({"game_id" : int(game_id)})["Board"])
	# Get the space the user clicked
	space = json['this_id']
	# If the game isn't running yet, print a message saying there needs to be more players
	if not BOARD.running:
		print("Game hasn't begun: Need more players")
		return None

 	# Split the given place number into an index and space to identify the board and location on that board respectively
 	# We have to do this because python turns numbers with preceding 0's into just the number and the first 9 spaces are
 	# referenced as 01, 02, 03, ...
	if space < 9:
		index = 0
	else:
		split = [int(i) for i in str(space)]
		index = split[0]
		space = split[1]

	# Check if it's a valid move
	myVar = BOARD.validmove(index, space, json['socket_id'])
	# Check if it returned a list (this will contain the error string)
	if type(myVar) is list:
		# If the length of the return from validmove is 3, then we must run the ID through the hash function to get the 
		# player's name
		if len(myVar) == 3:
			myVar[1] = "Not " + str(GAME_USERNAMES[myVar[1]]["username"]) + "'s turn"
		msg_dict = {
		"user_name" : "Server",
		"message" : myVar[1]
		}
		# Emit to the chat the error message
		socketio.emit('game server response', msg_dict, room=game_id)
		return None

	# Back up check
	elif not BOARD.validmove(index, space, json['socket_id']):
		print("Invalid move")
		return None

	# Make the move on the backend board which means it passed all of the validmove tests
	BOARD.makemove(index, space, json['socket_id'])
	
	# Check if the game has been won or if it is a cat's game and emit the message to the chat
	if BOARD.checkwin():
		sendServerMsg(str("Player " + str(BOARD.win) + " wins!"))
		print("Player " + str(BOARD.win) + " wins!")
		msg_dict = {
		"user_name" : "Server",
		"message" : "Player " + str(GAME_USERNAMES[str(BOARD.win)]["username"]) + " wins!"
		}
		socketio.emit('game server response', msg_dict, room=game_id)
		# Get the right player's username who won
		if BOARD.win == BOARD.turn_ID:
			other = BOARD.other_ID
		else:
			other = BOARD.turn_ID
		# Create a message for the main lobby
		msg_dict = {
			"user_name" : "Server",
			"message" : str(GAME_USERNAMES[str(BOARD.win)]["username"]) + " beat " + str(GAME_USERNAMES[str(other)]["username"]) + "!"
		}
		# Emit the message to the main lobby screen so people not in the game can see who won
		socketio.emit('game server response', msg_dict, room=1)

	# Otherwise, it's a cat's game
	elif ((BOARD.win == None) and (BOARD.checkfull())):
		sendServerMsg("Too bad! It's a cat's game...")
		msg_dict = {
			"user_name" : "Server",
			"message" : "It's a cats game!"
		}
		# Emit the message to the lobby
		socketio.emit('game server response', msg_dict, room=game_id)

	# Change the players turn
	BOARD.changeturn()

	# Emit the necessary information to the front end to update the board
	json = {
		"index": index,
		"space": space, 
		"moves": list(BOARD.moves),
		"player": BOARD.turn,
		"player_ID" : BOARD.turn_ID,
		"other_player_ID" : BOARD.other_ID,
		"username" : str(GAME_USERNAMES[str(BOARD.turn_ID)]["username"]),
		"other_username" : str(GAME_USERNAMES[str(BOARD.other_ID)]["username"])
	}
	# Update the board in the dictionary
	collection.update_one({"game_id" : int(game_id)}, {"$set": {"Board" : pickle.dumps(BOARD)}})
	# Emit the information to index3.html
	socketio.emit('valid move', json, room=game_id)

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

# Secret html page where someone can reset the database easily with the click of a button.
@app.route('/secret', methods=['GET', 'POST'])
def secret():
	'''
	Loads the initial secret.html page.

	Arguments: 	None

	Returns: 	template renderer for the secret.html page
	'''
	return render_template("secret.html")

# socketio connector for the reset database event in secret.html
@socketio.on('reset database')
def g_handle_value(methods=['GET', 'POST']):
	'''
	Resets the database.

	Arguments: 	None

	Returns: 	None
	'''
	# Loop through the entries in the database
	for entry in collection.find():
		# Delete them one-by-one
		collection.delete_one(entry)
	# Clear the global lobbies list
	LOBBIES = []
	# Refresh the list of lobbies people can see in the main lobby.
	socketio.emit('print lobby', {
		"lobbies" : LOBBIES
	})
	# Print a message to the console confirming that the database has been reset.
	print("Database Reset: All documents deleted")

# Initialize flask and socketio
if __name__ == '__main__':
	socketio.run(app, debug=CONFIG.DEBUG, port=CONFIG.PORT, host="127.0.0.1")