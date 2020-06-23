# -*- coding: utf-8 -*-
"""
  interstage_mass.py generated by WhatsOpt 1.9.3
"""
import numpy as np
from mass.interstage_mass_base import InterstageMassBase

class InterstageMass(InterstageMassBase):
    """ An OpenMDAO component to encapsulate InterstageMass discipline """
		
    def compute(self, inputs, outputs):
        """ InterstageMass computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Ds = inputs['Ds']
            k_sm = inputs['k_sm']
            Sint = inputs['Sint']

            Minterstage = k_sm * 7.7165 * Sint * (3.3208 * Ds)**0.4856

            outputs['Minterstage'] = Minterstage
        return outputs 

# Reminder: inputs of compute()
#   
#       inputs['Ds'] -> shape: (1,), type: Float    
#       inputs['k_sm'] -> shape: (1,), type: Float    
#       inputs['Sint'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(InterstageMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for InterstageMass """
#   
#       	partials['Minterstage', 'Ds'] = np.zeros((1, 1))
#       	partials['Minterstage', 'k_sm'] = np.zeros((1, 1))
#       	partials['Minterstage', 'Sint'] = np.zeros((1, 1))        
