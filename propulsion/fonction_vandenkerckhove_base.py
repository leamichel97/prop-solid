# -*- coding: utf-8 -*-
"""
  fonction_vandenkerckhove_base.py generated by WhatsOpt 1.9.4
"""
# DO NOT EDIT unless you know what you are doing
# whatsopt_url: 
# analysis_id: 776


import numpy as np
from numpy import nan
from os import path
from importlib import import_module
from yaml import load, FullLoader
from openmdao.api import ExplicitComponent

class FonctionVandenkerckhoveBase(ExplicitComponent):
    """ An OpenMDAO base component to encapsulate FonctionVandenkerckhove discipline """

    def __init__(self, **kwargs):
        super(FonctionVandenkerckhoveBase, self).__init__(**kwargs)
        self._impl = None
        dockconf = path.join(path.dirname(__file__), ".whatsopt_dock.yml")
        if path.exists(dockconf):
            with open(dockconf) as dockfile:
                dock = load(dockfile, Loader=FullLoader)
                impl = dock.get("fonction_vandenkerckhove")
                if impl:
                    module = import_module(impl['module'])
                    self._impl = getattr(module, impl['class'])()

    def setup(self):
        self.add_input('gamma', val=1.22, desc='Flight path angle')

        self.add_output('gamma_maj', val=np.ones((1,)), desc='Vandenkerckhove function')



        