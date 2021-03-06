# -*- coding: utf-8 -*-
"""
  propellants_mass.py generated by WhatsOpt 1.10.1
"""
import numpy as np
from solid.propellants_mass_base import PropellantsMassBase

class PropellantsMass(PropellantsMassBase):
    """ An OpenMDAO component to encapsulate PropellantsMass discipline """
		
    def compute(self, inputs, outputs):
        """ PropellantsMass computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            prop_m = inputs['prop_m']
            SF = inputs['SF']
            tb = inputs['tb']
        
            Mp = (prop_m * tb) * (1 + SF)
  
            outputs['Mp'] = Mp
        return outputs 

# Reminder: inputs of compute()
#   
#       inputs['prop_m'] -> shape: (1,), type: Float    
#       inputs['SF'] -> shape: (1,), type: Float    
#       inputs['tb'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(PropellantsMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for PropellantsMass """
#   
#       	partials['Mp', 'prop_m'] = np.zeros((1, 1))
#       	partials['Mp', 'SF'] = np.zeros((1, 1))
#       	partials['Mp', 'tb'] = np.zeros((1, 1))        
