# -*- coding: utf-8 -*-
"""
  solid_rocket_length_base.py generated by WhatsOpt 1.9.3
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

class SolidRocketLengthBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate SolidRocketLength discipline """

    def __init__(self, **kwargs):
        super(SolidRocketLengthBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("solid_rocket_length")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('Lcase', val=np.ones((1,)), desc='')
        self.add_input('Lconv', val=np.ones((1,)), desc='Convergent nozzle section length')
        self.add_input('Ldiv', val=np.ones((1,)), desc='Divergent nozzle section length')

        self.add_output('L_SRM', val=1.0, desc='')



        