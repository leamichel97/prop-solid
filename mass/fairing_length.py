# -*- coding: utf-8 -*-
"""
  fairing_length.py generated by WhatsOpt 1.10.1
"""
import numpy as np
from mass.fairing_length_base import FairingLengthBase

class FairingLength(FairingLengthBase):
    """ An OpenMDAO component to encapsulate FairingLength discipline """
		
    def compute(self, inputs, outputs):
        """ FairingLength computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Ds = inputs['Ds']

            Lfairing = 1.1035 * (Ds **1.6385) + 2.3707

            outputs['Lfairing'] = Lfairing
        
        return outputs  

# Reminder: inputs of compute()
#   
#       inputs['Ds'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(FairingLength, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for FairingLength """
#   
#       	partials['Lfairing', 'Ds'] = np.zeros((1, 1))        
