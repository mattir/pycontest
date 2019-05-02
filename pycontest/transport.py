import numpy as np

def transport(loc, vel, dt):
    """transport equations
    Args:
         loc: initial location (can be int/float or array)
         vel: velocity (can be int/float or array)
         dt: time step

    Returns:
        location after one time step
     """

    # if loc, vel are simple numbers
    if isinstance(loc, (int, float)) and isinstance(vel, (int, float)):
        loc = loc + vel * dt
    # if loc or vel is a list, we want to convert to numpy arrays
    if isinstance(loc, list) and isinstance(vel, list):
        loc = np.array(loc)
        vel = np.array(vel)
    # if loc or vel are numpy arrays
    if isinstance(loc, np.ndarray) and isinstance(vel, np.ndarray):
        # ensure the type is always a float for both loc and vel
        loc = loc.astype(np.float32, copy=False)
        vel = vel.astype(np.float32, copy=False)
        loc[:] = loc[:] + vel[:] *dt
    return loc
