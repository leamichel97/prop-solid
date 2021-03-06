# -*- coding: utf-8 -*-
"""
  run_doe.py generated by WhatsOpt 1.10.1
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 775

import sys
import numpy as np
import matplotlib.pyplot as plt

from openmdao.api import Problem, SqliteRecorder, CaseReader
from openmdao_extensions.smt_doe_driver import SmtDOEDriver
from lanceur_prop_solide_without_trajectory_version2 import LanceurPropSolideWithoutTrajectoryVersion2 

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-b", "--batch",
                  action="store_true", dest="batch", default=False,
                  help="do not plot anything")
parser.add_option("-n", "--ncases", type="int",
                  dest="n_cases", default=50,
                  help="number of samples")
parser.add_option("-p", "--parallel", 
                  action="store_true", default=False,
                  help="run doe in parallel")
(options, args) = parser.parse_args()

pb = Problem(LanceurPropSolideWithoutTrajectoryVersion2())
pb.driver = SmtDOEDriver(sampling_method_name='LHS', n_cases=options.n_cases, sampling_method_options={'criterion': 'ese'})
pb.driver.options['run_parallel'] = options.parallel

case_recorder_filename = 'lanceur_prop_solide_without_trajectory_version2_doe.sqlite'        
recorder = SqliteRecorder(case_recorder_filename)
pb.driver.add_recorder(recorder)
pb.model.nonlinear_solver.options['err_on_non_converge'] = True


pb.model.add_design_var('Mnozzle', lower=-sys.float_info.max, upper=sys.float_info.max)


pb.model.add_objective('F_T')
pb.model.add_objective('Isp')
pb.model.add_objective('Lconv')
pb.model.add_objective('Ldiv')
pb.model.add_objective('Lfairing')
pb.model.add_objective('Linterstage')
pb.model.add_objective('Mavionics')
pb.model.add_objective('Mf')
pb.model.add_objective('Mfairing')
pb.model.add_objective('Mi')
pb.model.add_objective('Minterstage')
pb.model.add_objective('Mpad')
pb.model.add_objective('M_EPS')
pb.model.add_objective('M_PLA')
pb.model.add_objective('prop_m')

pb.setup()  
pb.run_driver()        

