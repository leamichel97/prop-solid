# -*- coding: utf-8 -*-
"""
  power_subsystem_mass.py generated by WhatsOpt 1.9.3
"""
import numpy as np
from mass.power_subsystem_mass_base import PowerSubsystemMassBase

class PowerSubsystemMass(PowerSubsystemMassBase):
    """ An OpenMDAO component to encapsulate PowerSubsystemMass discipline """
		
    def compute(self, inputs, outputs):
        """ PowerSubsystemMass computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
                    
            outputs['M_EPS'] = np.ones((1,))   

# Reminder: inputs of compute()
#   
#       inputs['Mavionics'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(PowerSubsystemMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for PowerSubsystemMass """
#   
#       	partials['M_EPS', 'Mavionics'] = np.zeros((1, 1))        
