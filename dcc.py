import socket
import time

# a=socket.create_connection(('holmes.freenode.net', 6667))
# a=socket.create_connection(('irc.irchighway.net', 6667))
a=socket.create_connection(('chat.freenode.net', 6667))
a.send(b'PASS pwd\r\n')
a.send(b"USER ashboy ashboy ashboy :ashboy \r\n")
# a.send(b'NICK ashboy:\r\n')
a.send(b'NICK ashboy\r\n')
# a.send(b'JOIN #ebooks\r\n');
a.send(b'JOIN #archlinux\r\n');
a.send(b'PRIVMSG Guest66:heyo\r\n');
while True:
    print(a.recv(1000))
    time.sleep(.4)
