import sys
import os.path
from queue import Queue
from PIL import Image
from shutil import copyfile

base_img = Image.open(sys.argv[1])
width, height = base_img.size
print (width, height)
start = (6,1)
end = (width - 6, height - 1)

def iswhite(value):
    if value == (255,255,255,255):
        return True

def getadjacent(n):
    x,y = n
    x_limited = min((x + 1), width - 1)
    y_limited = min((y + 1), height - 1)
    return [(x-1,y),(x,y-1),(x_limited,y),(x,y_limited)]

def BFS(start, end, pixels):

    queue = Queue()
    queue.put([start]) # Wrapping the start tuple in a list

    while not queue.empty():

        path = queue.get() 
        pixel = path[-1]

        if pixel == end:
            return path

        for adjacent in getadjacent(pixel):
            x,y = adjacent
            if iswhite(pixels[x,y]):
                pixels[x,y] = (127,127,127)
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)

    print ("Queue has been exhausted. No answer was found.")


if __name__ == '__main__':

    base_pixels = base_img.load()

    path = BFS(start, end, base_pixels)

    result_img = Image.open(sys.argv[1]) 
    result_pixels = result_img.load()
    for position in path:
        x,y = position
        result_pixels[x,y] = (255,0,0) # red

    if not os.path.isfile("result.png"):
        creation = open("result.png", "x")      
    
    result_img.save("result.png")
   
