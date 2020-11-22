Scale.default="minor"
Clock.bpm=120
Scale.default.set("major")
Scale.default.set(Scale.major)
Root.default.set("A")

hh >> play("- - - - ")
p1 >> lazer([(-2,0,2)], dur=1, delay=1/2)
p2 >> bass([5,2,5,2,4]*3,dur=[1]*3+[1/2]*2)

Clock.every(4, lambda: toca())

compas = 0
def toca():
    global compas
    compas += 1
    if(compas == 3):
        p1 >> lazer([(0,2)]*3, dur=[1,1/2,1/4+1+1/2,1/4], delay=1/2)
        p2 >> bass([5,2,5])
    if(compas == 4):
        p1.stop()
        p2 >> bass([5,2,4]*2+[2,4,2,5,2,4],dur=[1,1/2,1/2])



#p1 >> glass([2,1,2,2,1,1,0,1,1,0], dur=[[1,1,1/2,1/2,1]*2], vib=0) TWISTED NERVE
#pulse -> 8 bits 
#razz -> tompetes
#donk -> djenbe
