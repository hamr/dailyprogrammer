#!/usr/bin/env python

# http://www.reddit.com/r/dailyprogrammer/comments/pjsdx/difficult_challenge_2/

# Your mission is to create a stopwatch program.

# This program should have start, stop, and lap options,
# and it should write out to a file to be viewed later.

import time
import signal
import select
import tty
import termios
import time
import sys

from curses import ascii

def main():

    def isData():
        return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

    old_settings = termios.tcgetattr(sys.stdin)
    try:
        tty.setcbreak(sys.stdin.fileno())

        i = 1
        while 1:
            time.sleep(1.0)
            print i
            i += 1

            if isData():
                c = sys.stdin.read(1)
                if c == 'l':
                  print 'lap'
                  i = 1
                if c == chr(ascii.ESC):
                    break

    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

if __name__ == '__main__':
    main()
