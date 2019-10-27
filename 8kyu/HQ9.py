# -*- coding: utf-8 -*-
# Source of katas: https://www.codewars.com/
# @Filename: HQ9.py

'''
You task is to implement an simple interpreter for the notorious esoteric language HQ9+ that will work for a single character input:

If the input is 'H', return 'Hello World!'
If the input is 'Q', return the input
If the input is '9', return the full lyrics of 99 Bottles of Beer(http://www.99-bottles-of-beer.net/lyrics.html). It should be formatted like this:
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
97 bottles of beer on the wall, 97 bottles of beer.
Take one down and pass it around, 96 bottles of beer on the wall.
...
...
...
2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.
For everything else, don't return anything (return null in C#, None in Rust).
(+ has no visible effects so we can safely ignore it.)
'''

# my solution
def HQ9(code):
    s = ''
    for i in range(99, 2, -1):
        onecircle = ("%s bottles of beer on the wall, %s bottles of beer."
        "\nTake one down and pass it around, %s bottles of beer on the wall.\n" % (i, i, i-1))
        s = s + onecircle

    endcircle = (
    "2 bottles of beer on the wall, 2 bottles of beer.\n"
    "Take one down and pass it around, 1 bottle of beer on the wall.\n"
    "1 bottle of beer on the wall, 1 bottle of beer.\n"
    "Take one down and pass it around, no more bottles of beer on the wall.\n"
    "No more bottles of beer on the wall, no more bottles of beer.\n"
    "Go to the store and buy some more, 99 bottles of beer on the wall.")

    s = s + endcircle

    return 'Hello World!' if code=='H' else 'Q' if code=='Q' else s if code=='9' else None

# best practice by Blind4Basics
LINES = "{0} of beer on the wall, {0} of beer.\nTake one down and pass it around, {1} of beer on the wall."
SONG = '\n'.join( LINES.format("{} bottles".format(n), "{} bottle".format(n-1)+"s"*(n!=2)) for n in range(99,1,-1) )
SONG += """
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""

def HQ9(code):
    return {'H': 'Hello World!', 'Q': 'Q', '9': SONG}.get(code, None)

#　best practice by hmikihth
# It is possible in one short line without hard coding! Have a nice day ;)
HQ9 = lambda c, b=(lambda x: "{} bottle{} of beer".format(x if x > 0 else "no more", "s" if x!=1 else "")): {'H':'Hello World!', 'Q':'Q', '9':"".join("{0}{2}, {1} on the wall.\n".format("{0} on the wall, {0}.\n".format(b(i)).capitalize(), b(i-1) if i else b(99), "Take one down and pass it around" if i else "Go to the store and buy some more") for i in range(99, -1, -1))[:-1]}.get(c, None)


# test cases 太长了，不贴了
