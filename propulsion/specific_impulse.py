# -*- coding: utf-8 -*-
"""
  specific_impulse.py generated by WhatsOpt 1.10.1
"""
import numpy as np
from propulsion.specific_impulse_base import SpecificImpulseBase

class SpecificImpulse(SpecificImpulseBase):
    """ An OpenMDAO component to encapsulate SpecificImpulse discipline """
		
    def compute(self, inputs, outputs):
        """ SpecificImpulse computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            g0 = inputs['g0']
            Ve = inputs['Ve']

            Isp = Ve / g0

            outputs['Isp'] = Isp  
        return outputs  

# Reminder: inputs of compute()
#   
#       inputs['g0'] -> shape: (1,), type: Float    
#       inputs['Ve'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(SpecificImpulse, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for SpecificImpulse """
#   
#       	partials['Isp', 'g0'] = np.zeros((1, 1))
#       	partials['Isp', 'Ve'] = np.zeros((1, 1))        
