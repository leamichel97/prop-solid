# -*- coding: utf-8 -*-
"""
  propellants_mass_base.py generated by WhatsOpt 1.10.1
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 777


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class PropellantsMassBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate PropellantsMass discipline """

    def __init__(self, **kwargs):
        super(PropellantsMassBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("propellants_mass")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('prop_m', val=1.0, desc='Propellantmass flow rate')
        self.add_input('SF', val=0.03, desc='Sliver fraction')
        self.add_input('tb', val=1.0, desc='Burn time')

        self.add_output('Mp', val=np.ones((1,)), desc='')



        