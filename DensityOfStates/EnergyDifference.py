import numpy as np

from DensityOfStates.PhononEnergy import PhononEnergy, acoustic_phonon, optical_phonon, polar_optical_phonon


class EnergyDifference:

    def __init__(self):
        self.u = 0.4
        self.k = 9.0
        self.dt = 3.0

    def initial_energy(self):
        """

        :return: Initial energy at a site for a specified phonon type
        :rtype: float
        """
        if type == 'acoustic':
            return acoustic_phonon(self.k, self.u)
        elif type == 'optical':
            return optical_phonon()
        else:
            return polar_optical_phonon()

    def final_energy(self):
        """

        :return: Final energy at a site for a specified phonon type
        :rtype: float
        """
        return (self.u * self.k) * self.dt

    def delta_energy(self, phonon_type):
        """

        :return: Difference in energy at sites for a specified phonon type
        :rtype: float
        """
        return self.final_energy(phonon_type) - self.initial_energy(phonon_type)
