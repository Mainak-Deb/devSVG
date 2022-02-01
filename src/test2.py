from deSVG import deSVG

s=deSVG("subhro",400,400)


s.rect(110,60,100,100,(0,255,255))

s.setShapeOpacity(0.8)
s.setStrokeWidth(5)

s.setStrokeOpacity(0.5)
s.rect(40,40,100,100,(0,0,255))

s.create()