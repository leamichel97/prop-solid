# -*- coding: utf-8 -*-
"""
  avionics_mass.py generated by WhatsOpt 1.10.1
"""
import numpy as np
from mass.avionics_mass_base import AvionicsMassBase

class AvionicsMass(AvionicsMassBase):
    """ An OpenMDAO component to encapsulate AvionicsMass discipline """
		
    def compute(self, inputs, outputs):
        """ AvionicsMass computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Ds = inputs['Ds']
            Lfairing = inputs['Lfairing']
            Linterstage = inputs['Linterstage']
            Lvehicle = inputs['Lvehicle']
            L_SRM = inputs['L_SRM']
            
            Lvehicle = Lfairing + Linterstage + L_SRM
            Mavionics = 0.25 * (246.76+ 1.3183 * Ds * Lvehicle)

            outputs['Mavionics'] = Mavionics

        return outputs    

# Reminder: inputs of compute()
#   
#       inputs['Ds'] -> shape: (1,), type: Float    
#       inputs['Lfairing'] -> shape: 1, type: Float    
#       inputs['Linterstage'] -> shape: 1, type: Float    
#       inputs['Lvehicle'] -> shape: (1,), type: Float    
#       inputs['L_SRM'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(AvionicsMass, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for AvionicsMass """
#   
#       	partials['Mavionics', 'Ds'] = np.zeros((1, 1))
#       	partials['Mavionics', 'Lfairing'] = np.zeros((1, 1))
#       	partials['Mavionics', 'Linterstage'] = np.zeros((1, 1))
#       	partials['Mavionics', 'Lvehicle'] = np.zeros((1, 1))
#       	partials['Mavionics', 'L_SRM'] = np.zeros((1, 1))        
