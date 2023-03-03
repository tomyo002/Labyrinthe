from Maze import Maze

laby = Maze(4, 4, empty=True)
#print(laby)

#laby.add_wall((0,0),(0,1))
#laby.add_wall((0,1),(1,1))
#print(laby)

#laby.remove_wall((0,0),(0,1))
#print(laby)

#print(laby.get_walls())

#laby.fill()
#print(laby)
#laby.empty()
#print(laby)

#print(laby.get_contiguous_cells((1,1)))
#print(laby.get_contiguous_cells((3,3)))


print(laby.get_reachable_cells((0,1)))

