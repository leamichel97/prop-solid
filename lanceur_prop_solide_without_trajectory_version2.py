# -*- coding: utf-8 -*-
"""
  lanceur_prop_solide_without_trajectory_version2.py generated by WhatsOpt 1.9.4
"""
from optparse import OptionParser
from openmdao.api import Problem
from openmdao.api import NonlinearBlockGS, ScipyKrylov
# from openmdao_extensions.reckless_nonlinear_block_gs import RecklessNonlinearBlockGS
from lanceur_prop_solide_without_trajectory_version2_base import LanceurPropSolideWithoutTrajectoryVersion2Base, LanceurPropSolideWithoutTrajectoryVersion2FactoryBase

class LanceurPropSolideWithoutTrajectoryVersion2(LanceurPropSolideWithoutTrajectoryVersion2Base):
    """ An OpenMDAO component to encapsulate LanceurPropSolideWithoutTrajectoryVersion2 analysis """
    def __init__(self, **kwargs):
        super(LanceurPropSolideWithoutTrajectoryVersion2, self).__init__(**kwargs)

        # Example of manual solver adjusments (imports should be adjusted accordingly)
        # self.nonlinear_solver = NewtonSolver() 
        # self.nonlinear_solver.options['maxiter'] = 20
        # self.linear_solver = DirectSolver()

    def setup(self):
        super(LanceurPropSolideWithoutTrajectoryVersion2, self).setup()


class LanceurPropSolideWithoutTrajectoryVersion2Factory(LanceurPropSolideWithoutTrajectoryVersion2FactoryBase):
    """ A factory to create disciplines of LanceurPropSolideWithoutTrajectoryVersion2 analysis """
    pass

if __name__ == "__main__":
    parser = OptionParser()
    parser.add_option("-n", "--no-n2", action="store_false", dest='n2_view', default=True, 
                      help="display N2 openmdao viewer")
    (options, args) = parser.parse_args()

    problem = Problem()
    problem.model = LanceurPropSolideWithoutTrajectoryVersion2()

    problem.setup()
    problem.final_setup()
    
    if options.n2_view:
        from openmdao.visualization.n2_viewer.n2_viewer import n2
        n2(problem)
