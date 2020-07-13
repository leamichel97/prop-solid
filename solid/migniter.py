# -*- coding: utf-8 -*-
"""
  migniter.py generated by WhatsOpt 1.9.4
"""
import numpy as np
from solid.migniter_base import MigniterBase

class Migniter(MigniterBase):
    """ An OpenMDAO component to encapsulate Migniter discipline """
		
    def compute(self, inputs, outputs):
        """ Migniter computation """
        if self._impl:
            # Docking mechanism: use implementation if referenced in .whatsopt_dock.yml file
            self._impl.compute(inputs, outputs)
        else:
            Ds = inputs['Ds']
            Lcase = inputs['Lcase']
            Mp = inputs['Mp']
            rho_p = inputs['rho_p']

            Vcavity = Lcase * np.pi * ((0.99*Ds)/2)**2 - (Mp/rho_p)

            Migniter = (20.62 * Vcavity) ** 0.7368
        
            outputs['Migniter'] = Migniter
        return outputs

# Reminder: inputs of compute()
#   
#       inputs['Ds'] -> shape: 1, type: Float    
#       inputs['Lcase'] -> shape: 1, type: Float    
#       inputs['Mp'] -> shape: 1, type: Float    
#       inputs['rho_p'] -> shape: 1, type: Float      
	
# To declare partial derivatives computation ...
# 
#    def setup(self):
#        super(Migniter, self).setup()
#        self.declare_partials('*', '*')  
#			
#    def compute_partials(self, inputs, partials):
#        """ Jacobian for Migniter """
#   
#       	partials['Migniter', 'Ds'] = np.zeros((1, 1))
#       	partials['Migniter', 'Lcase'] = np.zeros((1, 1))
#       	partials['Migniter', 'Mp'] = np.zeros((1, 1))
#       	partials['Migniter', 'rho_p'] = np.zeros((1, 1))        
