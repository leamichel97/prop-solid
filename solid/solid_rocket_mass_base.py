# -*- coding: utf-8 -*-
"""
  solid_rocket_mass_base.py generated by WhatsOpt 1.9.4
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

class SolidRocketMassBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate SolidRocketMass discipline """

    def __init__(self, **kwargs):
        super(SolidRocketMassBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("solid_rocket_mass")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('Mcase', val=1.0, desc='')
        self.add_input('Migniter', val=1.0, desc='')
        self.add_input('Mnozzle', val=1.0, desc='')
        self.add_input('Mp', val=np.ones((1,)), desc='')

        self.add_output('M_SRM', val=1.0, desc='')



        