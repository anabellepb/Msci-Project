import numpy

from DensityOfStates.EnergyDifference import EnergyDifference


def des_solution():
    """

    :return: the energy difference between two sites
    :rtype: float
    """

    phonon_type = 'acoustic'
    energy_difference = EnergyDifference.delta_energy(phonon_type)

    return energy_difference * numpy.pi

