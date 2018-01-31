
def createSphere(name,r,size=0.01,color=[0,0,0,1]):
  r.client.gui.addSphere(name,size,color)
  r.client.gui.addToGroup(name,r.sceneName)
  r.client.gui.refresh()

def moveSphere(name,r,pos):
  q=pos+[1,0,0,0]
  r.client.gui.applyConfiguration(name,q)
  r.client.gui.refresh()

