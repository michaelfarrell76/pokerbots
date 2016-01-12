import argparse
import socket
import sys

#Dictionary to split up parsing different packages
options = {
            "NEWGAME"           :   newGame,
            "KEYVALUE"          :   keyValue,
            "REQUESTKEYVALUES"  :   requestKeyValues,
            "NEWHAND"           :   newHand,
            "GETACTION"         :   getAction,
            "HANDOVER"          :   handOver
}

"""
Simple example pokerbot, written in python.

This is an example of a bare bones pokerbot. It only sets up the socket
necessary to connect with the engine and then always returns the same action.
It is meant as an example of how a pokerbot should communicate with the engine.
"""
class Player:
    def __init__(self):
        print "init"

    def run(self, input_socket):
        
        # Get a file-object for reading packets from the socket.
        # Using this ensures that you get exactly one packet per read.
        f_in = input_socket.makefile()
        
        while True:
            # Block until the engine sends us a packet.
            data = f_in.readline().strip()
            
            # If data is None, connection has closed.
            if not data:
                print "Gameover, engine disconnected."
                break

            #Determine packet type
            word = data.split()[0]

            options[word](data)

        # Clean up the socket.
        s.close()
        
    def newGame(self, data):
    def keyValue(self, data):
    def requestKeyValues(self, data):
        # At the end, the engine will allow your bot save key/value pairs.
        # Send FINISH to indicate you're done.
        s.send("FINISH\n")
    def newHand(self, data):
    def getAction(self, data):
        # Currently CHECK on every move. You'll want to change this.
        s.send("CHECK\n")
    def handOver(self, data):

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A Pokerbot.', add_help=False, prog='pokerbot')
    parser.add_argument('-h', dest='host', type=str, default='localhost', help='Host to connect to, defaults to localhost')
    parser.add_argument('port', metavar='PORT', type=int, help='Port on host to connect to')
    args = parser.parse_args()

    # Create a socket connection to the engine.
    print 'Connecting to %s:%d' % (args.host, args.port)
    try:
        s = socket.create_connection((args.host, args.port))
    except socket.error as e:
        print 'Error connecting! Aborting'
        exit()

    bot = Player()
    bot.run(s)
