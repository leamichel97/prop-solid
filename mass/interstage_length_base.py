# -*- coding: utf-8 -*-
"""
  interstage_length_base.py generated by WhatsOpt 1.9.3
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

class InterstageLengthBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate InterstageLength discipline """

    def __init__(self, **kwargs):
        super(InterstageLengthBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("interstage_length")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('Lconv', val=1.0, desc='Convergent nozzle section length')
        self.add_input('Ldiv', val=1.0, desc='Divergent nozzle section length')

        self.add_output('Linterstage', val=np.ones((1,)), desc='Interstage length')



        