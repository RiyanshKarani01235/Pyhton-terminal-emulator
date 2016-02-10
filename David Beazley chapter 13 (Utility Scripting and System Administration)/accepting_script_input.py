#!/usr/bin/env python3

'''
"#!" --> Shebeang --> when a script with a shebang is run as a program, 
the program loader parses the rest of the script's initial line as an 
interpreter directive; the specified interpreter program is run instead, 
passing to it as an argument the path that was initially used when 
attempting to run the script
'''

import fileinput

with fileinput.input() as f_input : 
	for line in f_input : 
		print(line,end='')