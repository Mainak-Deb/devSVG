from basicSVG import basicSVG

if __name__== "__main__":
    a=basicSVG("fo",400,400)
    a.setBackground((0,255,255))

    a.setStrokeWidth(5)
    a.setShapeOpacity(0.5)

    a.rect(0,0,100,100,(255,0,0),60)

    a.setStrokeColor((255,0,0))
    a.setStrokeOpacity(0.8)

    a.rect(10,10,50,50,(255,255,0),10)


    a.create()
    
