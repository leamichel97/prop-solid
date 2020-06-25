# -*- coding: utf-8 -*-
"""
  fairing_mass.py generated by WhatsOpt 1.9.3
"""
import numpy as np
from mass.fairing_mass_base import FairingMassBase

class FairingMass(FairingMassBase):
    """ An OpenMDAO component to encapsulate FairingMass discipline """
		
    def compute(self, inputs, outputs):
        """ FairingMass computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Ds = inputs['Ds']
            Lfairing = inputs['Lfairing']

            Mfairing = 49.3218 * ((Lfairing * Ds)**0.9054)

            outputs['Mfairing'] = Mfairing
            
        return outputs   

# Reminder: inputs of compute()
#   
#       inputs['Ds'] -> shape: (1,), type: Float    
#       inputs['Lfairing'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(FairingMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for FairingMass """
#   
#       	partials['Mfairing', 'Ds'] = np.zeros((1, 1))
#       	partials['Mfairing', 'Lfairing'] = np.zeros((1, 1))        
