from DensityOfStates.PhononEnergy import acoustic_phonon, optical_phonon, polar_optical_phonon


class EnergyDifference:

    def __init__(self, phonon_type):
        self.phonon_type = phonon_type
        self.u = 0.4
        self.k = 9.0
        self.dt = 3.0

    def energy_calculation(self, k, u):
        """

        :param k: position in Brillouin zone
        :type k: float
        :param u: velocity (?)
        :type u: float
        :return: Energy of an acoustic phonon
        :rtype: float
        """

        if self.phonon_type == 'acoustic':
            return acoustic_phonon(k, u)
        elif self.phonon_type == 'optical':
            return optical_phonon()
        else:
            return polar_optical_phonon()

    def initial_energy(self):
        """

        :return: Initial energy at a site for a specified phonon type
        :rtype: float
        """
        return self.energy_calculation(self.k, self.u)

    def final_energy(self):
        """

        :return: Final energy at a site for a specified phonon type
        :rtype: float
        """
        return self.energy_calculation(self.k * self.dt, self.u * self.dt)

    def delta_energy(self):
        """

        :return: Difference in energy at sites for a specified phonon type
        :rtype: float
        """
        return self.final_energy() - self.initial_energy()
