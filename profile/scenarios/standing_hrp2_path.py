from hpp.corbaserver.rbprm.rbprmbuilder import Builder
from hpp.gepetto import Viewer

rootJointType = 'freeflyer'
packageName = 'hpp-rbprm-corba'
meshPackageName = 'hpp-rbprm-corba'
urdfName = 'hrp2_trunk_flexible'
urdfNameRoms =  ['hrp2_larm_rom','hrp2_rarm_rom','hrp2_lleg_rom','hrp2_rleg_rom']
urdfSuffix = ""
srdfSuffix = ""

rbprmBuilder = Builder ()

rbprmBuilder.loadModel(urdfName, urdfNameRoms, rootJointType, meshPackageName, packageName, urdfSuffix, srdfSuffix)
rbprmBuilder.setJointBounds ("base_joint_xyz", [-1.3,1, -0.5, 0.5, 0, 0.9])
rbprmBuilder.setFilter(['hrp2_larm_rom','hrp2_lleg_rom','hrp2_rleg_rom'])
rbprmBuilder.setAffordanceFilter('hrp2_rarm_rom', ['Support','Lean'])
rbprmBuilder.setAffordanceFilter('hrp2_larm_rom', ['Support','Lean'])
rbprmBuilder.setAffordanceFilter('hrp2_rleg_rom', ['Support'])
rbprmBuilder.setAffordanceFilter('hrp2_lleg_rom', ['Support'])
rbprmBuilder.boundSO3([-0.4,0.4,-3,3,-3,3])

#~ from hpp.corbaserver.rbprm. import ProblemSolver
from hpp.corbaserver.rbprm.problem_solver import ProblemSolver

ps = ProblemSolver( rbprmBuilder )

r = Viewer (ps)

q0 = rbprmBuilder.getCurrentConfig ();
q_init = rbprmBuilder.getCurrentConfig (); r (q_init)
q_goal = q_init [::]
q_goal [0:3] = [0.19, 0.05, 0.9]; r (q_goal)

#~ fullBody.client.basic.robot.setJointConfig('base_joint_SO3',[0.7316888688738209, 0, -0.6816387600233341, 0]); q_init = rbprmBuilder.getCurrentConfig (); r (q_init)

rbprmBuilder.client.basic.robot.setJointConfig('base_joint_SO3',[0.7316888688738209, 0, 0.6816387600233341, 0]); q_init = rbprmBuilder.getCurrentConfig (); r (q_init)
q_init = rbprmBuilder.getCurrentConfig ();
q_init [0:3] = [-1, 0.05, 0.4]; rbprmBuilder.setCurrentConfig (q_init); r (q_init)
#~ q_0 [0:3] = [-0.2, 0, 0.3]; r (q_0)


q_goal [0:3] = [0.13, 0.05, 0.8]; r (q_goal)
#~ q_init [0:6] = [0.0, -2.2, 2.0, 0.7316888688738209, 0.0, 0.6816387600233341]; 
#~ rbprmBuilder.setCurrentConfig (q_init); r (q_init)


#~ ps.addPathOptimizer("GradientBased")
ps.addPathOptimizer("RandomShortcut")
ps.setInitialConfig (q_init)
ps.addGoalConfig (q_goal)

from hpp.corbaserver.affordance.affordance import AffordanceTool
afftool = AffordanceTool ()
#~ afftool.setAffordanceConfig('Support', [0.2, 0.03, 0.00005])
#~ afftool.setAffordanceConfig('Lean', [0.5, 0.05, 0.00005])
r.loadObstacleModel (packageName, "scene_wall", "planning")
afftool.analyseAll()
afftool.visualiseAffordances('Support', r, [0.25, 0.5, 0.5])
afftool.visualiseAffordances('Lean', r, [1, 0, 0])

ps.client.problem.selectConFigurationShooter("RbprmShooter")
ps.client.problem.selectPathValidation("RbprmPathValidation",0.01)
t = ps.solve ()
if isinstance(t, list):
	t = t[0]* 3600000 + t[1] * 60000 + t[2] * 1000 + t[3]
f = open('log.txt', 'a')
f.write("path computation " + str(t) + "\n")
f.close()


from hpp.gepetto import PathPlayer
pp = PathPlayer (rbprmBuilder.client.basic, r)
#~ pp.fromFile("/home/stonneau/dev/hpp/src/hpp-rbprm-corba/script/paths/stair.path")
#~ 
#~ pp (2)
#~ pp (0)

#~ pp (1)
#~ pp.toFile(1, "/home/stonneau/dev/hpp/src/hpp-rbprm-corba/script/paths/stair.path")
#~ r (q_init)

rob = rbprmBuilder.client.basic.robot
r(q_init)
#~ rbprmBuilder.exportPath (r, ps.client.problem, 1, 0.01, "standing_hrp2__path.txt")


#~ configs = []
#~ problem = ps.client.problem
#~ length = problem.pathLength (0)
#~ t = 0
#~ i = 0
#~ configs = []
#~ dt = 0.1 / length
#~ while t < length :
	#~ q = rbprmBuilder.getCurrentConfig()
	#~ q[0:9]= problem.configAtParam (0, t)[0:9]
	#~ configs.append(q)
	#~ t += dt
	#~ i = i+1
	#~ 
#~ i = 0;
#~ r(configs[i]); i = +1
