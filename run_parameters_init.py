# -*- coding: utf-8 -*-
"""
  run_parameters_init.py generated by WhatsOpt 1.10.1
"""
import numpy as np
from numpy import nan

def initialize(mda):

    mda['Ae'] = 1.5926 # Nozzle exit area - m^2
    mda['beta'] = 60 # Nozzle convergent half angle  - °
    mda['De'] = 1.424 # Nozzle exit diameter - m 
    mda['Ds'] = 1.27 # Stage diameter - m
    mda['Dt'] = 0.2 # Nozzle throat diameter - m
    mda['FF'] = 0.95 # Fill factor - Without Unit
    mda['f_safety'] = 1.5 # Safety factor - Without Unit
    mda['g0'] = 9.80665 # Earth's gravitational acceleration at sea level - m.s^2
    mda['gamma'] = 1.22 # the ratio of specific heats - Without Unit
    mda['k_sm'] = 1 # Interstage material correction factor - Without Unit
    mda['Lvehicle'] = 1.0 # Vehicle Length - m
    mda['Mcarter'] = 1.0 # Mass of the motor case itself - kg
    mda['Minsulation'] = 1.0 # Mass of the insulation layer - kg
    mda['Mnozzle'] = 13 # Nozzle Mass - kg
    mda['M_CaseBody'] = 1.0 # Case body Mass - kg
    mda['M_CaseTop'] = 1.0 # Case Top Mass - kg
    mda['M_InsulationBody'] = 1.0 # Mass of the insulation body - kg
    mda['M_InsulationTop'] = 1.0 # Mass of the insulation top - kg
    mda['M_PL'] = 140 # Payload mass - kg
    mda['Pa'] = 26442 # Ambient pressure  - Pa
    mda['Pc'] = 5610000 # Combustion chamber pressure - Pa
    mda['Pe'] = 18327 # Nozzle exit pressure - Pa
    mda['R'] = 286.689655 # Specific gas constant - J.kg^-1K^-1
    mda['rho'] = 1600 # the density of the material - kg.m^-3
    mda['rho_in'] = 850 # the density of the Ethylene - Propylene - Diene Copolymer (EPDM) for isolation - kg.m^-3
    mda['rho_p'] = 1850 # Propellant density - kg.m^-3
    mda['Ru'] = 0.1 # Longitudinal radius of the throat - m 
    mda['SF'] = 0.03 # Sliver fraction - Without Unit
    mda['sigma'] = 800000000 # Allowable material design stress - Pa
    mda['Sint'] = 1 # Interstage surface area  - m^2
    mda['t'] = 1.0 # The thickness of the motor case  - m
    mda['tb'] = 75.3 # Burn time - s
    mda['Tc'] = 3440 # Combustion chamber temperature - K
    mda['theta_n'] = 15 # Nozzle divergent half angle - °
    mda['zeta'] = 0.93630 # Thrust correction factor - Without Unit



if __name__ == "__main__":
    from tabulate import tabulate

    mda = {}
    initialize(mda)
    headers = ["parameter", "value"]
    data = [[k, mda[k]] for k in mda]
    print(tabulate(data, headers))