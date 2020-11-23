Clock.bpm=120
Scale.default.set(Scale.minor)
Root.default.set("F#")

Clock.every(4, lambda: toca())

compas = 0

mel = [0,-3,0,0,1,2,2,0,0,0,0,2,1,-1,-1,1,2,0,0,0,-3,0,0,1,2,0,0,0,0,2,4,4,4,3,2,2,1,1,2,0,0,0,2,4,4,3,2,1,-1,-1,-1,-1,1,3,3,3,3,2,2,1,1,2,0,0]
mel2 = map(lambda x: x+7, mel)
mel3 = map(lambda x: x+2, mel)
dura = [1/4]+[1/2]*2+[3/4]+[1/4]*5+[1/2]+[1/4]*2+[1/2]*7+[1/4]*2+[1/2]+[1/2]+[3/4]+[1/4]+[1/2]+[1/4]+[1/2]+[1/4]*11+[1/2]*3+[1/4]*2+[1/2]*5+[1/4]+[1/2]+[1/4]*11+[1/2]+[1/4]+[5/4]


def toca():
    global compas
    if(compas == 0):
        hh >> play("--------")
        p1 >> pads([(0,2,4)], dur=1, delay=[1/2], amplify=1/2)
        p2 >> sawbass([7,2,7,2,6],dur=[1]*3 + [1/2]*2, amplify=2)
    print(compas)
    if(compas == 3):
        p1 >> pads([(0,2,4)], dur=[1,1/2,2], delay=1/2, amplify=3/5)
        p2 >> sawbass([7,2,7], dur=[1]*2 + [2])
        bd >> play("/", amplify=3)
        me >> pluck(mel, dur=dura, amplify=2, delay=3.75)
        mi >> star(list(mel2), dur=dura, amplify=2, delay=3.75)
    if(compas == 4):
        p1 >> pads([[(0,2,4)]*4, [(-1,1,4)]*2, [(0,2,4)]*6], dur=[1], delay=1/2, amplify=1/2)
        p2 >> sawbass([7,2,6,7,2,6,2,6,2], dur=[1] + [1/2]*2, amplify=1)
        bd >> play("x-x-x-x-")
    if(compas == 10):
        qw >> play("H  H  H ", amplify=1/3)
        we >> play("A  A  A ", amplify=1/3)
        er >> play("C  C  C ", amplify=1/3)
        rt >> play("K  K  K ", amplify=1/3)
        ty >> play("E  E  E ", amplify=1/3)
        yu >> play("P  P  P ", amplify=1/3)
        ui >> play("S  S  S ", amplify=1/3)
    if(compas == 12):
        db >> donk([(0,2)], dur=[1/4])
        p1.stop()
        mi.stop()
        hh.stop()
    if(compas == 15):
        p1 >> pluck([(0,2,4)], dur=[1,1/2,2], delay=1/2, amplify=3/5)
        p2 >> bass([7,2,7], dur=[1]*2 + [2])
        p2 >> sawbass([7,2,7], dur=[1]*2 + [2])
        bd >> play("xxxxxxx", amplify=2)
        mt >> marimba(mel, dur=dura, amplify=2, delay=3.75)
        my >> lazer(list(mel2), dur=dura, amplify=2, delay=3.75)
    if(compas == 16):
        bd >> play("[xx]", amplify=3)
        qw >> play(" 2020   ", amplify=1/10)
        we.stop()
        er.stop()
        rt.stop()
        ty.stop()
        yu.stop()
        ui.stop()
    if(compas == 17):
        bd >> play("[xxxxx]", amplify=2)
        mt >> marimba(mel, dur=dura, amplify=2, delay=3.75)
        me >> pluck(mel, dur=dura, amplify=2, delay=3.75)
    if(compas == 18):
        db >> donk([(0,2)], dur=[1/4])
        p1 >> pluck([(0,2,4)], dur=[1,1/2,2], delay=1/2, amplify=2/5)
        p2 >> bass([7,2,7], dur=[1]*2 + [2], amplify=2/5)
        p3 >> sawbass([7,2,7], dur=[1]*2 + [2], amplify=2/5)
        p4 >> jbass([7,2,7], dur=[1]*2 + [2], amplify=2/5)
        hh >> play("--------")
        bd >> play("x x x x ", amplify=1)
        qw >> play("H  H  H ", amplify=2)
    if(compas == 32):
        qw.stop()
        p1.stop()
        p2.stop()
        p3.stop()
        p4.stop()
        my.stop()
        me.stop()
        mi.stop()
        bd.stop()
        hh.stop()
        db.stop()
    if(compas == 34):
        Clock.clear()
    compas += 1
