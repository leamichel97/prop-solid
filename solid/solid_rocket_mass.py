# -*- coding: utf-8 -*-
"""
  solid_rocket_mass.py generated by WhatsOpt 1.9.3
"""
import numpy as np
from solid.solid_rocket_mass_base import SolidRocketMassBase

class SolidRocketMass(SolidRocketMassBase):
    """ An OpenMDAO component to encapsulate SolidRocketMass discipline """
		
    def compute(self, inputs, outputs):
        """ SolidRocketMass computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
                    
            outputs['M_SRM'] = 1.0   

# Reminder: inputs of compute()
#   
#       inputs['Mcase'] -> shape: 1, type: Float    
#       inputs['Migniter'] -> shape: 1, type: Float    
#       inputs['Mnozzle'] -> shape: 1, type: Float    
#       inputs['Mp'] -> shape: (1,), type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(SolidRocketMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for SolidRocketMass """
#   
#       	partials['M_SRM', 'Mcase'] = np.zeros((1, 1))
#       	partials['M_SRM', 'Migniter'] = np.zeros((1, 1))
#       	partials['M_SRM', 'Mnozzle'] = np.zeros((1, 1))
#       	partials['M_SRM', 'Mp'] = np.zeros((1, 1))        
