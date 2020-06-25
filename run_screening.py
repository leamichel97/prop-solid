# -*- coding: utf-8 -*-
"""
  run_screening.py generated by WhatsOpt 1.9.3
"""
# DO NOT EDIT unless you know what you are doing
# analysis_id: 775

import sys
import numpy as np
import matplotlib.pyplot as plt
from packaging import version

from openmdao import __version__ as OPENMDAO_VERSION
from openmdao.api import Problem, SqliteRecorder, CaseReader
from openmdao_extensions.salib_doe_driver import SalibDOEDriver

from SALib.analyze import morris
from SALib.analyze import sobol
from SALib.plotting import morris as mp
from SALib.plotting.bar import plot as barplot
from lanceur_prop_solide_without_trajectory_version2 import LanceurPropSolideWithoutTrajectoryVersion2 


from optparse import OptionParser
parser = OptionParser()
parser.add_option("-b", "--batch",
                  action="store_true", dest="batch", default=False,
                  help="do not plot anything")
parser.add_option("-s", "--sobol",
                  action="store_true", dest="sobol", default=False,
                  help="do not plot anything")
parser.add_option("-p", "--parallel", 
                  action="store_true", default=False,
                  help="run doe in parallel")
(options, args) = parser.parse_args()

pb = Problem(LanceurPropSolideWithoutTrajectoryVersion2())
sa_method_name='Morris'
sa_doe_options={'n_trajs': 10, 'n_levels': 4}
if options.sobol:
    sa_method_name='Sobol'
    sa_doe_options={'n_samples': 500, 'calc_second_order': False}

pb.driver = SalibDOEDriver(sa_method_name=sa_method_name, sa_doe_options=sa_doe_options)
pb.driver.options['run_parallel'] = options.parallel

case_recorder_filename = 'lanceur_prop_solide_without_trajectory_version2_screening.sqlite'        
recorder = SqliteRecorder(case_recorder_filename)
pb.driver.add_recorder(recorder)

if version.parse(OPENMDAO_VERSION) > version.parse("2.8.0"):
    pb.model.nonlinear_solver.options['err_on_non_converge'] = True
else:
    pb.model.nonlinear_solver.options['err_on_maxiter'] = True


pb.model.add_design_var('Mnozzle', lower=-sys.float_info.max, upper=sys.float_info.max)
pb.model.add_design_var('M_CaseFrust', lower=-sys.float_info.max, upper=sys.float_info.max)


pb.model.add_objective('F_T')
pb.model.add_objective('Isp')
pb.model.add_objective('Lconv')
pb.model.add_objective('Ldiv')
pb.model.add_objective('Lfairing')
pb.model.add_objective('Linterstage')
pb.model.add_objective('L_SRM')
pb.model.add_objective('Mavionics')
pb.model.add_objective('Mfairing')
pb.model.add_objective('Minterstage')
pb.model.add_objective('Mpad')
pb.model.add_objective('M_EPS')
pb.model.add_objective('M_PLA')
pb.model.add_objective('M_SRM')
pb.model.add_objective('prop_m')

pb.setup()  
pb.run_driver()        


