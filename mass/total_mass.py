# -*- coding: utf-8 -*-
"""
  total_mass.py generated by WhatsOpt 1.10.1
"""
import numpy as np
from mass.total_mass_base import TotalMassBase

class TotalMass(TotalMassBase):
    """ An OpenMDAO component to encapsulate TotalMass discipline """
		
    def compute(self, inputs, outputs):
        """ TotalMass computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
                    
            outputs['Mf'] = 1.0 
            outputs['Mi'] = 1.0   

# Reminder: inputs of compute()
#   
#       inputs['Mavionics'] -> shape: 1, type: Float    
#       inputs['Mcase'] -> shape: 1, type: Float    
#       inputs['Mfairing'] -> shape: 1, type: Float    
#       inputs['Migniter'] -> shape: 1, type: Float    
#       inputs['Minterstage'] -> shape: 1, type: Float    
#       inputs['Mp'] -> shape: 1, type: Float    
#       inputs['Mpad'] -> shape: 1, type: Float    
#       inputs['M_EPS'] -> shape: 1, type: Float    
#       inputs['M_PLA'] -> shape: 1, type: Float    
#       inputs['M_SRM'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(TotalMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for TotalMass """
#   
#       	partials['Mf', 'Mavionics'] = np.zeros((1, 1))
#       	partials['Mf', 'Mcase'] = np.zeros((1, 1))
#       	partials['Mf', 'Mfairing'] = np.zeros((1, 1))
#       	partials['Mf', 'Migniter'] = np.zeros((1, 1))
#       	partials['Mf', 'Minterstage'] = np.zeros((1, 1))
#       	partials['Mf', 'Mp'] = np.zeros((1, 1))
#       	partials['Mf', 'Mpad'] = np.zeros((1, 1))
#       	partials['Mf', 'M_EPS'] = np.zeros((1, 1))
#       	partials['Mf', 'M_PLA'] = np.zeros((1, 1))
#       	partials['Mf', 'M_SRM'] = np.zeros((1, 1))
#       	partials['Mi', 'Mavionics'] = np.zeros((1, 1))
#       	partials['Mi', 'Mcase'] = np.zeros((1, 1))
#       	partials['Mi', 'Mfairing'] = np.zeros((1, 1))
#       	partials['Mi', 'Migniter'] = np.zeros((1, 1))
#       	partials['Mi', 'Minterstage'] = np.zeros((1, 1))
#       	partials['Mi', 'Mp'] = np.zeros((1, 1))
#       	partials['Mi', 'Mpad'] = np.zeros((1, 1))
#       	partials['Mi', 'M_EPS'] = np.zeros((1, 1))
#       	partials['Mi', 'M_PLA'] = np.zeros((1, 1))
#       	partials['Mi', 'M_SRM'] = np.zeros((1, 1))        
