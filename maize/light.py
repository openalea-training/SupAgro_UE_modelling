import pandas
from openalea.lpy import Lsystem
from alinea.caribu.CaribuScene import CaribuScene
from alinea.astk.sun_and_sky import sun_sky_sources, sky_sources as _sky_sources
from alinea.caribu.light import light_sources


def canopy_pattern(density=10, inter_row=80):
    inter_plant = 1. / density / (inter_row / 100.) * 100
    return (-0.5 * inter_row, -0.5 * inter_plant,
               0.5 * inter_row, 0.5 * inter_plant)

def sky_sources(clear_sky=False, daydate='2000-06-21', longitude=3.52, latitude=43.56, altitude=56,
                                   timezone='Europe/Paris'):
    if not clear_sky:
        light = light_sources(*_sky_sources())
    else:
        sun, sky = sun_sky_sources(daydate=daydate, longitude=longitude, latitude=latitude, altitude=altitude,
                                   timezone=timezone, normalisation=1)
        light = light_sources(*sun) + light_sources(*sky)
    return light


def illuminate(lstring, lscene, light=None, pattern=None):
  cs = CaribuScene(lscene, light=light)
  raw, agg = cs.run(simplify=True)
  agg['name'] = {vid:lstring[vid].name for vid in agg['area']}
  return pandas.DataFrame(agg)

  
def show_illumination(lstring, lscene, light=None, pattern=None):
  cs = CaribuScene(lscene, light=light)
  raw, agg = cs.run(simplify=True)
  cs.plot(raw['Ei'], minval=0, maxval=1)
  
  
def generate_plant(lsystem='simple_maize_nolight.lpy', parameters=None):
    """ Run a lpy model from python with parameters 
    
    parameters : a {'parameter_name': value, ...} dict with parameters
    Note: 
    the following lines should be included in lpy file, after the definition of the model parameters

    try:
      parameters = parameters
    except NameError:
      parameters = {}
    for p_name in parameters:
      globals()[p_name] = parameters[p_name]
    """
    if parameters:
        lsys = Lsystem(lsystem, {'parameters':parameters})
    else:
        lsys = Lsystem(lsystem)
    lstring = lsys.iterate()
    lscene = lsys.sceneInterpretation(lstring)
    return lstring, lscene
    