from Maze import Maze

#laby = Maze(4, 4, empty=True)
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


#print(laby.get_reachable_cells((0,1)))

#laby = Maze.gen_btree(4,4)
#print(laby)

#laby = Maze.gen_sidewinder(10, 10)
#print(laby)

#laby = Maze.gen_fusion(15,15)
#print(laby)

#laby = Maze.gen_exploration(15,15)
#print(laby)


#laby = Maze.gen_wilson(10,10)
#print(laby)

"""laby = Maze.gen_fusion(15, 15)
solution = laby.solve_dfs((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))"""
laby = Maze.gen_exploration(15, 15)
solution = laby.solve_rhr((0, 0), (14, 14))
str_solution = {c:'*' for c in solution}
str_solution[( 0,  0)] = 'D'
str_solution[(14, 14)] = 'A'
print(laby.overlay(str_solution))