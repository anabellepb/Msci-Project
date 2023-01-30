import numpy as np


def acoustic_phonon(k, u):
    """

    :param k: position in Brillouin zone
    :type k: float
    :param u: velocity (?)
    :type u: float
    :return: Energy of an acoustic phonon
    :rtype: float
    """

    energy = float(2 * np.hbar * k * u)
    return energy


def optical_phonon():
    """

    :return: Energy of an optical phonon
    :rtype: int
    """

    return np.random.randint(0, 5)


def polar_optical_phonon():
    """

    :return: Energy of polar-optical phonon
    :rtype: int
    """
    return np.random.randint(0, 8)


class PhononEnergy:
    """
    Energy near the k=0 point of the brillouin zone for a phonon
    from: https://en.wikipedia.org/wiki/Density_of_states
    """

    def __init__(self, k, u):
        self.k = k
        self.u = u
