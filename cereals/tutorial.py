# ipython --gui=qt
from cereals import build_shoot, parametric_leaf, leaf_azimuth
from display import display_mtg


stem_radius=0.5
insertion_heights=(10,20)
leaf_lengths=(10,10)
leaf_areas=(10,10)
a_leaf = parametric_leaf(nb_segment=10, insertion_angle=50, scurv=0.5,curvature=50, alpha=-2.3)
leaf_shapes = [a_leaf for l in leaf_lengths]
leaf_azimuths = leaf_azimuth(size=len(leaf_lengths), phyllotactic_angle=180, phyllotactic_deviation=15, plant_orientation=0, spiral=False)
g = build_shoot(stem_radius=stem_radius, insertion_heights=insertion_heights, leaf_lengths=leaf_lengths, leaf_areas=leaf_areas, 
                leaf_shapes=leaf_shapes, leaf_azimuths=leaf_azimuths)
display_mtg(g)