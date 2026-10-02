Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing
#sequencing

name='nived'
#n i v e d
#0 1 2 3 4

#n i v e d
#-5 -4 -3 -2 -1

Name[5]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    Name[5]
NameError: name 'Name' is not defined. Did you mean: 'name'?
#Indexing
#sequencing

name='nived'
#n i v e d
#0 1 2 3 4

# n i v e d
#-5-4-3-2-1

name[2]
'v'
name[-5]
'n'
name[-1]
'd'
name[4]
'd'

mark=['26','36','46','96','106']
mark[3]
'96'
mark[4]
'106'
mark[-4]
'36'
mark[1]
'36'


Name[0:4]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    Name[0:4]
NameError: name 'Name' is not defined. Did you mean: 'name'?
name[0:4]
'nive'
name[0:5]
'nived'
name[:5]
'nived'
name[:3]
'niv'
name[::-1]
'devin'

mark[0:4:1]
['26', '36', '46', '96']
mark[0:4:2]
['26', '46']
mark[0:5:2]
['26', '46', '106']
mark[::1]
['26', '36', '46', '96', '106']

#Ranging
#range(stop)
#range(start : stop)
#range(start : stop :step)

for i in range(0,12):
    print()

    












#Ranging
#range(stop)
#range(start : stop)
#range(start : stop :step)

for i in range(13):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12

for i in range(0,13):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
10
11
12
>>> 
>>> for i in range(1,13,1):
...     print(i)
... 
...     
1
2
3
4
5
6
7
8
9
10
11
12
>>> 
>>> for i in range (1,13,2):
...     print(i)
... 
...     
1
3
5
7
9
11

