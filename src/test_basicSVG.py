from deSVG import deSVG

if __name__== "__main__":
    a=deSVG("folds",400,400)
    a.setBackground((0,255,255))

    a.setStrokeWidth(5)
    a.setShapeOpacity(0.5)

    a.rect(0,0,100,200,(255,0,0),0)

    a.setStrokeColor((255,0,0))
    a.setStrokeOpacity(0.8)

    a.rect(10,10,50,50,(255,255,0),10)

    a.setStrokeColor((255,244,0))
    a.setStrokeOpacity(0.8)
    
    a.circle(200,200,100,(24,123,43))
    a.circle(200,300,100,(24,123,43))

    a.line((0,0),(100,100))
    a.line((0,0),(200,100))
    a.line((0,0),(200,300))

    a.create()
    
