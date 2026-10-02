Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #Assignment operators
>>> 
>>> TotalMatches = 10
>>> print(TotalMatches)
10
>>> Matcheswon = 4
>>> Matcheswon += 1
>>> print(Matcheswon)
5
>>> 
>>> Playedmatches = 7
>>> Matchesleft = TotalMatches
>>> Matchesleft -= Playedmatches
>>> print(Matchesleft)
3
>>> 
>>> TotalMatchPoint = 20
>>> KeyboardInterrupt
>>> Pergamepoint = 2
>>> Pointsearned = Matcheswon
>>> Pointsearned *= Pergamepoint
>>> print(Pointsearned)
10
>>> Pointslost = Matcheslost
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    Pointslost = Matcheslost
NameError: name 'Matcheslost' is not defined. Did you mean: 'Matchesleft'?
