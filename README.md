# mazer
I is  a solution to mazer puzle based on Joseph Kern's one:
https://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image/13174351#13174351

A program needs to be invoked with the parameter giving a path to the source image.
For example:
python-mazer.py maze_04.png

The solution will be included in the file "result.png" placed in the folder of the program.
It will be created if not existing. And it will be overwritten it exists.

My only input here is:
- queue instead of Queue
- value tuple items number
- limits to x and y
- start/end points
- output file creation.
