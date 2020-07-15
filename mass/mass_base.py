# -*- coding: utf-8 -*-
"""
  mass_base.py generated by WhatsOpt 1.10.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 778


import numpy as np
from numpy import nan

from openmdao.api import Problem, Group, ParallelGroup, IndepVarComp
from openmdao.api import NonlinearBlockGS
from openmdao.api import ScipyKrylov
from openmdao import __version__ as OPENMDAO_VERSION

from mass.interstage_length import InterstageLength
from mass.fairing_length import FairingLength
from mass.fairing_mass import FairingMass
from mass.interstage_mass import InterstageMass
from mass.pad_interface_mass import PadInterfaceMass
from mass.avionics_mass import AvionicsMass
from mass.power_subsystem_mass import PowerSubsystemMass
from mass.payload_adapter_mass import PayloadAdapterMass










class MassBase(Group):
    """ An OpenMDAO base component to encapsulate Mass MDA """
    def __init__(self, thrift_client=None, **kwargs):
        super(MassBase, self). __init__(**kwargs)

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

        self.add_subsystem('InterstageLength', self.create_interstage_length(), promotes=['Lconv', 'Ldiv', 'Linterstage'])
        self.add_subsystem('FairingLength', self.create_fairing_length(), promotes=['Ds', 'Lfairing'])
        self.add_subsystem('FairingMass', self.create_fairing_mass(), promotes=['Ds', 'Lfairing', 'Mfairing'])
        self.add_subsystem('InterstageMass', self.create_interstage_mass(), promotes=['Ds', 'k_sm', 'Linterstage', 'Minterstage', 'Sint'])
        self.add_subsystem('PadInterfaceMass', self.create_pad_interface_mass(), promotes=['Ds', 'Mpad'])
        self.add_subsystem('AvionicsMass', self.create_avionics_mass(), promotes=['Ds', 'Lfairing', 'Linterstage', 'Lvehicle', 'L_SRM', 'Mavionics'])
        self.add_subsystem('PowerSubsystemMass', self.create_power_subsystem_mass(), promotes=['Mavionics', 'M_EPS'])
        self.add_subsystem('PayloadAdapterMass', self.create_payload_adapter_mass(), promotes=['M_PL', 'M_PLA'])

    def create_interstage_length(self):
    	return InterstageLength()
    def create_fairing_length(self):
    	return FairingLength()
    def create_fairing_mass(self):
    	return FairingMass()
    def create_interstage_mass(self):
    	return InterstageMass()
    def create_pad_interface_mass(self):
    	return PadInterfaceMass()
    def create_avionics_mass(self):
    	return AvionicsMass()
    def create_power_subsystem_mass(self):
    	return PowerSubsystemMass()
    def create_payload_adapter_mass(self):
    	return PayloadAdapterMass()


# Used by Thrift server to serve disciplines
class MassFactoryBase(object):
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
