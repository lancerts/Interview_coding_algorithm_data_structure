

import random
import sys
import getopt
import time
from PIL import Image, ImageDraw, ImageFont
from math import sqrt
import logging

def rand_seq(size):
    '''generates values in random order
    equivalent to using shuffle in random,
    without generating all values at once'''
    values=range(size)
    for i in xrange(size):
        # pick a random index into remaining values
        j=i+int(random.random()*(size-i))
        # swap the values
        values[j],values[i]=values[i],values[j]
        # return the swapped value
        yield values[i]

def all_pairs(size):
    '''generates all i,j pairs for i,j from 0-size'''
    for i in rand_seq(size):
        for j in rand_seq(size):
            yield (i,j)

def reversed_sections(tour):
    '''generator to return all possible variations where the section between two cities are swapped'''
    for i,j in all_pairs(len(tour)):
        if i != j:
            copy=tour[:]
            if i < j:
                copy[i:j+1]=reversed(tour[i:j+1])
            else:
                copy[i+1:]=reversed(tour[:j])
                copy[:j]=reversed(tour[i+1:])
            if copy != tour: # no point returning the same tour
                yield copy

def swapped_cities(tour):
    '''generator to create all possible variations where two cities have been swapped'''
    for i,j in all_pairs(len(tour)):
        if i < j:
            copy=tour[:]
            copy[i],copy[j]=tour[j],tour[i]
            yield copy

def cartesian_matrix(coords):
    '''create a distance matrix for the city coords that uses straight line distance'''
    matrix={}
    for i,(x1,y1) in enumerate(coords):
        for j,(x2,y2) in enumerate(coords):
            dx,dy=x1-x2,y1-y2
            dist=sqrt(dx*dx + dy*dy)
            matrix[i,j]=dist
    return matrix

def read_coords(coord_file):
    '''
    read the coordinates from file and return the distance matrix.
    coords should be stored as comma separated floats, one x,y pair per line.
    '''
    coords=[]
    for line in coord_file:
        x,y=line.strip().split(' ')
        coords.append((float(x),float(y)))
    return coords

def tour_length(matrix,tour):
    '''total up the total length of the tour based on the distance matrix'''
    total=0
    num_cities=len(tour)
    for i in range(num_cities):
        j=(i+1)%num_cities
        city_i=tour[i]
        city_j=tour[j]
        total+=matrix[city_i,city_j]
    return total

def write_tour_to_img(coords,tour,title,img_file):
    padding=100
    # shift all coords in a bit
    a=15
    coords=[(int(x)/a-1200,int(y)/a-600) for (x,y) in coords]
    maxx,maxy=0,0

    for x,y in coords:
        maxx=max(x,maxx)
        maxy=max(y,maxy)
    maxx=maxx+padding
    maxy+=padding
    img=Image.new("RGB",(int(maxx),int(maxy)),color=(255,255,255))

    font=ImageFont.load_default()
    d=ImageDraw.Draw(img);
    num_cities=len(tour)
    for i in range(num_cities):
        j=(i+1)%num_cities
        city_i=tour[i]
        city_j=tour[j]
        x1,y1=coords[city_i]
        x2,y2=coords[city_j]
        d.line((int(x1),int(y1),int(x2),int(y2)),fill=(255,0,0), width=1)
        d.text((int(x1)+7,int(y1)-5),str(i),font=font,fill=(32,32,32))


    for x,y in coords:
        x,y=int(x),int(y)
        d.ellipse((x-5,y-5,x+5,y+5),outline=(0,0,0),fill=(196,196,196))

    d.text((300,100),title,font=font,fill=(0,0,0))

    del d
    #img.save(img_file, "png")

    img.show()

def init_random_tour(tour_length):
   tour=range(tour_length)
   random.shuffle(tour)
   return tour

#def run_hillclimb(init_function,move_operator,objective_function,max_iterations):
#    from hillclimb import hillclimb_and_restart
#    iterations,score,best=hillclimb_and_restart(init_function,move_operator,objective_function,max_iterations)
#    return iterations,score,best

def run_anneal(init_function,move_operator,objective_function,max_iterations,start_temp,alpha):
    if start_temp is None or alpha is None:
        usage();
        print "missing --cooling start_temp:alpha for annealing"
        sys.exit(1)
    from sa import anneal
    iterations,score,best=anneal(init_function,move_operator,objective_function,max_iterations,start_temp,alpha)
    return iterations,score,best

def usage():
    print "usage: python %s [-o <output image file>] [-v] [-m reversed_sections|swapped_cities] -n <max iterations> [-a hillclimb|anneal] [--cooling start_temp:alpha] <city file>" % sys.argv[0]

def main():
    out_file_name="tsp.png"
    max_iterations=20000
    verbose=True
    move_operator=reversed_sections
    start_temp=800
    alpha=0.995


    city_file="tsp2.txt"
    # enable more verbose logging (if required) so we can see workings
    # of the algorithms

    format='%(asctime)s %(levelname)s %(message)s'
    if verbose:
        logging.basicConfig(level=logging.INFO,format=format)
    else:
        logging.basicConfig(format=format)

    # setup the things tsp specific parts hillclimb needs
    coords=read_coords(open(city_file,'r'))
    init_function=lambda: init_random_tour(len(coords))
    matrix=cartesian_matrix(coords)
    objective_function=lambda tour: -tour_length(matrix,tour)

    logging.info('using move_operator: %s'%move_operator)

    start = time.time()

    iterations,score,best=run_anneal(init_function,move_operator,objective_function,max_iterations,start_temp,alpha)
    # output results
    print iterations,score,best
    print time.time() - start


    write_tour_to_img(coords,best,'%s: %f'%(city_file,score),out_file_name)
    time.sleep(1)
if __name__ == "__main__":
    main()