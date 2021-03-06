"""Correct for the center of mass of the satellite

Description:
------------

asdf

"""
# Midgard imports
from midgard.dev import plugins

# Where imports
from where import apriori


@plugins.register
def center_of_mass(dset):
    """Calculate center of mass corrections

    Args:
        dset (Dataset):  Model data.

    Returns:
        Numpy array:     Corrections in meters for each observation.
    """
    com = apriori.get("slr_center_of_mass", sat_name=dset.vars["sat_name"])
    return -com.get(dset.station, dset.time)
