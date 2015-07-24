from hpp.corbaserver.rbprm.rbprmbuilder import Builder
from hpp.corbaserver.rbprm.rbprmfullbody import FullBody
from hpp.gepetto import Viewer


packageName = "hrp2_14_description"
meshPackageName = "hrp2_14_description"
rootJointType = "freeflyer"
##
#  Information to retrieve urdf and srdf files.
urdfName = "hrp2_14"
urdfSuffix = "_reduced"
srdfSuffix = ""

fullBody = FullBody ()

fullBody.loadFullBodyModel(urdfName, rootJointType, meshPackageName, packageName, urdfSuffix, srdfSuffix)
fullBody.setJointBounds ("base_joint_xyz", [-5, 5, -5, 5, -5, 5])

from hpp.corbaserver.rbprm.problem_solver import ProblemSolver

ps = ProblemSolver( fullBody )
r = Viewer (ps)
r.loadObstacleModel ('hpp-rbprm-corba', "scene", "car")

#~ AFTER loading obstacles
rLeg = 'RLEG_JOINT0'
rKnee = 'RLEG_JOINT3'
rLegOffset = [0.055,0.105,0.017]
rLegNormal = [0,-1,0]
rLegx = 0.05; rLegy = 0.05
fullBody.addLimb(rLeg,rKnee,rLegOffset,rLegNormal, rLegx, rLegy, 5000, 0.01)

lLeg = 'LLEG_JOINT0'
lKnee = 'LLEG_JOINT3'
lLegOffset = [0.105,0.055,-0.017]
lLegNormal = [0,-1,0]
lLegx = 0.05; lLegy = 0.05
fullBody.addLimb(lLeg,lKnee,lLegOffset,rLegNormal, lLegx, lLegy, 5000, 0.01)
#~  	

#~ AFTER loading obstacles
rarm = 'RARM_JOINT0'
rHand = 'RARM_JOINT5'
rArmOffset = [0.03,-0.050,-0.050]
rArmNormal = [0,1,0]
rArmx = 0.024; rArmy = 0.024
fullBody.addLimb(rarm,rHand,rArmOffset,rArmNormal, rArmx, rArmy, 5000, 0.01)


#~ AFTER loading obstacles
larm = 'LARM_JOINT0'
lHand = 'LARM_JOINT5'
lArmOffset = [0.03,-0.050,-0.050]
lArmNormal = [0,1,0]
lArmx = 0.024; lArmy = 0.024
fullBody.addLimb(larm,lHand,lArmOffset,lArmNormal, lArmx, lArmy, 5000, 0.01)


q_0 = fullBody.getCurrentConfig (); r (q_0)

fullBody.client.basic.robot.setJointConfig('LARM_JOINT0',[1])
fullBody.client.basic.robot.setJointConfig('RARM_JOINT0',[1])
fullBody.client.basic.robot.setJointConfig('LLEG_JOINT3',[1.5])
fullBody.client.basic.robot.setJointConfig('RLEG_JOINT3',[1.5])
#~ 
fullBody.client.basic.robot.setJointConfig('base_joint_SO3',[0.7316888688738209, 0, 0.6816387600233341, 0]); q_init = fullBody.getCurrentConfig (); r (q_init)

q_init = fullBody.getCurrentConfig (); r (q_init)
q_init [0:3] = [0, -0.5, 0.2]; fullBody.setCurrentConfig (q_init); r (q_init)
#~ configs = fullBody.getContactSamplesIds(rLeg, q_init, [0,1,0])
#~ i = 0
#~ q_init = fullBody.getSample(rLeg, int(configs[i])); i = i+1;r(q_init)
#~ 
#~ fullBody.setCurrentConfig (q_init)
q_init = fullBody.generateContacts(q_init, [-0.1,0,1]) ; r(q_init)
#~ r (q_init)

q_goal = q_init [::]
q_goal [0:3] = [1, -0.5, 0.6]

#~ r (q_0)
#~ fullBody.setCurrentConfig (q_0)
#~ fullBody.client.basic.robot.setJointConfig('LARM_JOINT0',[1])
#~ fullBody.client.basic.robot.setJointConfig('RARM_JOINT0',[1])
#~ fullBody.client.basic.robot.setJointConfig('LLEG_JOINT3',[1.5])
#~ fullBody.client.basic.robot.setJointConfig('RLEG_JOINT3',[1.5])

#~ fullBody.client.basic.robot.setJointConfig('base_joint_SO3',[0.7316888688738209, 0, 0.6816387600233341, 0]); q_init = fullBody.getCurrentConfig (); r (q_init)
#~ q_init = fullBody.getCurrentConfig (); r (q_init)
#~ q_init [0:3] = [0, -0.5, 0.2]; fullBody.setCurrentConfig (q_init); r (q_init)
#~ q_init = fullBody.generateContacts(q_init, [-0.1,0,1]) ; r(q_init)
