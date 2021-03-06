# -*- coding: utf-8 -*-
"""
  lanceur_prop_solide_without_trajectory_version2_base.py generated by WhatsOpt 1.10.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: https://ether.onera.fr/whatsopt
# analysis_id: 775


import numpy as np
from numpy import nan

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from propulsion.propulsion import Propulsion
from solid.solid import Solid
from mass.mass import Mass
from propulsion.fonction_vandenkerckhove import FonctionVandenkerckhove
from propulsion.expansion_ratio import ExpansionRatio
from propulsion.throat_area import ThroatArea
from propulsion.prop_mass_flow_rate import PropMassFlowRate
from propulsion.characteristic_velocity import CharacteristicVelocity
from propulsion.thrust_coefficient import ThrustCoefficient
from propulsion.exhaust_velocity import ExhaustVelocity
from propulsion.thrust_force import ThrustForce
from propulsion.specific_impulse import SpecificImpulse
from solid.propellants_mass import PropellantsMass
from solid.solid_motor_length import SolidMotorLength
from solid.migniter import Migniter
from solid.mcase import Mcase
from solid.solid_rocket_mass import SolidRocketMass
from solid.length_convergent_section import LengthConvergentSection
from solid.length_divergent_section import LengthDivergentSection
from solid.solid_rocket_length import SolidRocketLength
from mass.interstage_length import InterstageLength
from mass.fairing_length import FairingLength
from mass.fairing_mass import FairingMass
from mass.interstage_mass import InterstageMass
from mass.pad_interface_mass import PadInterfaceMass
from mass.avionics_mass import AvionicsMass
from mass.power_subsystem_mass import PowerSubsystemMass
from mass.payload_adapter_mass import PayloadAdapterMass
from mass.total_mass import TotalMass


class LanceurPropSolideWithoutTrajectoryVersion2Base(Group):
    """ An OpenMDAO base component to encapsulate LanceurPropSolideWithoutTrajectoryVersion2 MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(LanceurPropSolideWithoutTrajectoryVersion2Base, self). __init__(**kwargs)

        self.nonlinear_solver = NonlinearBlockGS() 
        self.nonlinear_solver.options['atol'] = 1.0e-10
        self.nonlinear_solver.options['rtol'] = 1.0e-10
        self.nonlinear_solver.options['err_on_non_converge'] = True
        self.nonlinear_solver.options['reraise_child_analysiserror'] = False

        self.linear_solver = ScipyKrylov()       
        self.linear_solver.options['atol'] = 1.0e-10
        self.linear_solver.options['rtol'] = 1.0e-10
        self.linear_solver.options['err_on_non_converge'] = True
        self.linear_solver.options['iprint'] = 1

    def setup(self): 
        indeps = self.add_subsystem('indeps', IndepVarComp(), promotes=['*'])

        indeps.add_output('Ae', np.ones((1,)))
        indeps.add_output('beta', np.ones((1,)))
        indeps.add_output('De', np.ones((1,)))
        indeps.add_output('Ds', np.ones((1,)))
        indeps.add_output('Dt', np.ones((1,)))
        indeps.add_output('FF', 1.0)
        indeps.add_output('f_safety', 1.0)
        indeps.add_output('g0', np.ones((1,)))
        indeps.add_output('gamma', np.ones((1,)))
        indeps.add_output('k_sm', np.ones((1,)))
        indeps.add_output('Lvehicle', np.ones((1,)))
        indeps.add_output('Mcarter', 1.0)
        indeps.add_output('Minsulation', 1.0)
        indeps.add_output('Mnozzle', 1.0)
        indeps.add_output('M_CaseBody', 1.0)
        indeps.add_output('M_CaseTop', 1.0)
        indeps.add_output('M_InsulationBody', 1.0)
        indeps.add_output('M_InsulationTop', 1.0)
        indeps.add_output('M_PL', np.ones((1,)))
        indeps.add_output('Pa', np.ones((1,)))
        indeps.add_output('Pc', np.ones((1,)))
        indeps.add_output('Pe', np.ones((1,)))
        indeps.add_output('R', np.ones((1,)))
        indeps.add_output('rho', 1.0)
        indeps.add_output('rho_in', 1.0)
        indeps.add_output('rho_p', 1.0)
        indeps.add_output('Ru', np.ones((1,)))
        indeps.add_output('SF', np.ones((1,)))
        indeps.add_output('sigma', 1.0)
        indeps.add_output('Sint', np.ones((1,)))
        indeps.add_output('t', 1.0)
        indeps.add_output('tb', np.ones((1,)))
        indeps.add_output('Tc', np.ones((1,)))
        indeps.add_output('theta_n', np.ones((1,)))
        indeps.add_output('zeta', np.ones((1,)))
        self.add_subsystem('Propulsion', self.create_propulsion(), promotes=['Ae', 'F_T', 'g0', 'gamma', 'Isp', 'Pa', 'Pc', 'Pe', 'prop_m', 'R', 'Tc', 'zeta'])
        self.add_subsystem('Solid', self.create_solid(), promotes=['beta', 'De', 'Ds', 'Dt', 'FF', 'f_safety', 'Lconv', 'Ldiv', 'L_SRM', 'Mcarter', 'Mcase', 'Migniter', 'Minsulation', 'Mnozzle', 'Mp', 'M_CaseBody', 'M_CaseTop', 'M_InsulationBody', 'M_InsulationTop', 'M_SRM', 'Pc', 'prop_m', 'rho', 'rho_in', 'rho_p', 'Ru', 'SF', 'sigma', 't', 'tb', 'theta_n'])
        self.add_subsystem('Mass', self.create_mass(), promotes=['Ds', 'k_sm', 'Lconv', 'Ldiv', 'Lfairing', 'Linterstage', 'Lvehicle', 'L_SRM', 'Mavionics', 'Mcase', 'Mf', 'Mfairing', 'Mi', 'Migniter', 'Minterstage', 'Mp', 'Mpad', 'M_EPS', 'M_PL', 'M_PLA', 'M_SRM', 'Sint'])

    def create_propulsion(self):
    	return Propulsion()


    def create_solid(self):
    	return Solid()


    def create_mass(self):
    	return Mass()




# Used by Thrift server to serve disciplines
class LanceurPropSolideWithoutTrajectoryVersion2FactoryBase(object):
    @staticmethod
    def create_propulsion_fonction_vandenkerckhove():
    	return FonctionVandenkerckhove()
    @staticmethod
    def create_propulsion_expansion_ratio():
    	return ExpansionRatio()
    @staticmethod
    def create_propulsion_throat_area():
    	return ThroatArea()
    @staticmethod
    def create_propulsion_prop_mass_flow_rate():
    	return PropMassFlowRate()
    @staticmethod
    def create_propulsion_characteristic_velocity():
    	return CharacteristicVelocity()
    @staticmethod
    def create_propulsion_thrust_coefficient():
    	return ThrustCoefficient()
    @staticmethod
    def create_propulsion_exhaust_velocity():
    	return ExhaustVelocity()
    @staticmethod
    def create_propulsion_thrust_force():
    	return ThrustForce()
    @staticmethod
    def create_propulsion_specific_impulse():
    	return SpecificImpulse()
    @staticmethod
    def create_solid_propellants_mass():
    	return PropellantsMass()
    @staticmethod
    def create_solid_solid_motor_length():
    	return SolidMotorLength()
    @staticmethod
    def create_solid_migniter():
    	return Migniter()
    @staticmethod
    def create_solid_mcase():
    	return Mcase()
    @staticmethod
    def create_solid_solid_rocket_mass():
    	return SolidRocketMass()
    @staticmethod
    def create_solid_length_convergent_section():
    	return LengthConvergentSection()
    @staticmethod
    def create_solid_length_divergent_section():
    	return LengthDivergentSection()
    @staticmethod
    def create_solid_solid_rocket_length():
    	return SolidRocketLength()
    @staticmethod
    def create_mass_interstage_length():
    	return InterstageLength()
    @staticmethod
    def create_mass_fairing_length():
    	return FairingLength()
    @staticmethod
    def create_mass_fairing_mass():
    	return FairingMass()
    @staticmethod
    def create_mass_interstage_mass():
    	return InterstageMass()
    @staticmethod
    def create_mass_pad_interface_mass():
    	return PadInterfaceMass()
    @staticmethod
    def create_mass_avionics_mass():
    	return AvionicsMass()
    @staticmethod
    def create_mass_power_subsystem_mass():
    	return PowerSubsystemMass()
    @staticmethod
    def create_mass_payload_adapter_mass():
    	return PayloadAdapterMass()
    @staticmethod
    def create_mass_total_mass():
    	return TotalMass()
