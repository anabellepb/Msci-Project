import numpy

from DensityOfStates.EnergyDifference import EnergyDifference


def des_solution():
    """

    :return: the energy difference between two sites
    :rtype: float
    """

    phonon_type = 'acoustic'
    instance = EnergyDifference(phonon_type)
    energy_difference = instance.delta_energy()

    return energy_difference * numpy.pi
