import httplib, sys

conn = httplib.HTTPConnection("127.0.0.1")
while 1:
    cmd = raw_input('Provide input (ex. GET hello.html): ')
    cmd = cmd.split()
	
    if cmd[0] == 'exit' or cmd[0] == 'bye':
        print 'exiting...'
        break
    else:
        conn.request(cmd[0], cmd[1])
        rsp = conn.getresponse()
        print(rsp.status, rsp.reason)
        print(rsp.read())
conn.close()