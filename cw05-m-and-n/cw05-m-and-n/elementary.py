import scipy as sp
class Particle(object):
    """ class """

    mass = 0.00
    position = (0.0, 0.0, 0.0)
    momentum = (0.0,0.0,0.0)
    

    def __init__(self, x, y, z):
        self.momentum = (0.0,0.0,0.0)
        self.mass = 1.0
        self.position = (x,y,z)
        
    def impulse(self,px,py,pz):
        self.momentum = (self.momentum[0]+px,self.momentum[1]+py,self.momentum[2]+pz)

    def move(self, dt):
        #p = mv
        #v = d/t
        #p = (d/t)*m
        #p = (d*m)/t
        #p*t = d*m
        #(p*t)/m = d
        self.position = ((self.position[0] + (self.momentum[0]*dt)/self.mass),(self.position[1] + (self.momentum[1]*dt)/self.mass),(self.position[2] + (self.momentum[2]*dt)/self.mass))

class ChargedParticle(Particle):
    
    charge = 0
        
class Electron(ChargedParticle):
    
    def __init__(self, x,y,z):
        super(Electron,self).__init__(x,y,z)
        self.charge = sp.constants.e*(-1)
        self.mass = sp.constants.electron_mass
        
class Proton(ChargedParticle):
    
    def __init__(self, x,y,z):
        super(Proton,self).__init__(x,y,z)
        self.charge = sp.constants.e
        self.mass = sp.constants.proton_mass
        
        
        