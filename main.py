from display import *
from draw import *
from parser import *
from matrix import *
import math

screen = new_screen()
zbuffer = new_zbuffer()
color = [ 0, 255, 0 ]
edges = []
polygons = []
t = new_matrix()
ident(t)
csystems = [ t ]
parse_file( 'script.txt', edges, polygons, csystems, screen, zbuffer, color )
parse_file( 'drawing.txt', edges, polygons, csystems, screen, zbuffer, color )
