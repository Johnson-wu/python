import socket
import sys

HOST, PORT = "localhost", 8888
# data = " ".join(sys.argv[1:])

# Create a socket (SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	sock.connect((HOST, PORT))
	while True:
		# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# sock.connect((HOST, PORT))
		# Connect to server and send data
		
		want = raw_input('>>>')
		if len(want) == 0: continue
		if want == 'q': 
			break
		else:
			sock.sendall(want + "\n")

			# Receive data from the server and shut down
			received = sock.recv(1024)
			print "Sent:     {}".format(want)
			print "Received: {}".format(received)
finally:
    sock.close()


