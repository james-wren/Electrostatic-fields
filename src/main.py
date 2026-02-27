from simulation import field_generator

charges = [
    (-1, (45, 162)), 
    (1, (12, 110)), 
    (1, (88, 145)), 
    (-1, (156, 24)), 
    (-1, (30, 195)), 
    (-1, (112, 7)), 
    (1, (175, 55)), 
    (-1, (10, 82)), 
    (-1, (198, 134)), 
    (1, (67, 41))
]


X, Y = field_generator.setup_graph(200, 200, 40, 40)
field_generator.create_quiver(X, Y, charges)