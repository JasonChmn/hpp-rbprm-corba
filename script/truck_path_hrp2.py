from hpp.corbaserver.rbprm.rbprmbuilder import Builder
from hpp.gepetto import Viewer

rootJointType = 'freeflyer'
packageName = 'hpp-rbprm-corba'
meshPackageName = 'hpp-rbprm-corba'
urdfName = 'hrp2_trunk08'
urdfNameRom = 'hrp2_rom'
urdfSuffix = ""
srdfSuffix = ""

rbprmBuilder = Builder ()

rbprmBuilder.loadModel(urdfName, urdfNameRom, rootJointType, meshPackageName, packageName, urdfSuffix, srdfSuffix)
rbprmBuilder.setJointBounds ("base_joint_xyz", [-1, 1, -4, 0, 1, 2.5])

#~ from hpp.corbaserver.rbprm. import ProblemSolver
from hpp.corbaserver.rbprm.problem_solver import ProblemSolver

ps = ProblemSolver( rbprmBuilder )

r = Viewer (ps)

q_init = rbprmBuilder.getCurrentConfig (); r (q_init)

#~ rbprmBuilder.client.basic.robot.setJointConfig('base_joint_SO3',[0.7316888688738209, 0, -0.6816387600233341, 0]); q_init = rbprmBuilder.getCurrentConfig (); r (q_init)

q_init = rbprmBuilder.getCurrentConfig (); r (q_init)
q_init  = [0.0, -2.2, 2.0, 0.53536860083385163, -0.46463139916614854, 0.49874749330202722, 0.49874749330202722];
q_init  = [-0.1, -2.65, 2.1, 0.53536860083385163, 0.46463139916614854, 0.49874749330202722, -0.49874749330202722];r(q_init)
q_init  = [-0.1, -2.4, 1.9, 0.53536860083385163, 0.46463139916614854, 0.49874749330202722, -0.49874749330202722];r(q_init)

#~ q_init = [2.5, -0.1, 1.55, 1.0, 0.0, 0.0, 0.0]; r (q_init)  # 1 scale
#~ q_init [0:3] = [2.2, 0, 2]; r (q_init)
#~ q_init [0:3] = [2., -0.1, 1.8]; r (q_init) # 0.9 scale
#~ q_init [0:3] = [2., -0.1, 1.6]; r (q_init) # 0.8 scale

rbprmBuilder.setCurrentConfig (q_init); r (q_init)

q_goal = [0, -4.0, 1.8, 0.7316888688738209, 0.0, 0.0, -0.68163876002333412]
#~ q_goal [0:3] = [4.0, 0, 2.0]; r (q_goal)  # 1 scale
#~ q_goal [0:3] = [3., -0.1, 1.9]; r (q_goal)  # 0.9 scale
#~ q_goal [0:3] = [3., -0.1, 1.5]; r (q_goal)  # 0.8 scale


ps.addPathOptimizer("RandomShortcut")
#~ ps.addPathOptimizer("GradientBased")
ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)

#~ ps.client.problem.selectConFigurationShooter("RbprmShooter")
#~ ps.client.problem.selectPathValidation("RbprmPathValidation",0.05)
r.loadObstacleModel (packageName, "truck", "planning")
ps.solve ()


from hpp.gepetto import PathPlayer
pp = PathPlayer (rbprmBuilder.client.basic, r)

#~ pp (0)
pp (1)
#~ pp.fromFile("/home/stonneau/dev/hpp/src/hpp-rbprm-corba/script/paths/truck.path")
#~ pp (1)
#~ pp.toFile(1, "/home/stonneau/dev/hpp/src/hpp-rbprm-corba/script/paths/truck.path")

