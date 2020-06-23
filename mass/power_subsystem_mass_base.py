# -*- coding: utf-8 -*-
"""
  power_subsystem_mass_base.py generated by WhatsOpt 1.9.3
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 778


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class PowerSubsystemMassBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate PowerSubsystemMass discipline """

    def __init__(self, **kwargs):
        super(PowerSubsystemMassBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("power_subsystem_mass")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('Mavionics', val=np.ones((1,)), desc='')

        self.add_output('M_EPS', val=np.ones((1,)), desc='Power subsystemmass')



        