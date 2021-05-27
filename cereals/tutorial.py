# ipython --gui=qt
from cereals import build_shoot
from display import display_mtg


stem_radius=0.5
insertion_heights=(10,20)
leaf_lengths=(10,10)
leaf_areas=(10,10)
g = build_shoot(stem_radius=stem_radius, insertion_heights=insertion_heights, leaf_lengths=leaf_lengths, leaf_areas=leaf_areas)
display_mtg(g)