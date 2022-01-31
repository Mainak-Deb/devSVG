
class basicSVG:
    #basic properties
    name="newsvg"
    height=100;
    height=100;
    fill="white";
    style="background-color:rgb(255,255,255)"


    #strokeproperties
    __strokeWidth=0;
    __strokeColor="black";
    __strokeOpacity=1;

    #shapeOpacity
    __shapeOpacity=1;




    #this is the main content
    content=''''''

    #this is the svg file main template
    themain='''
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}"   style="{style}">
            {content}
        </svg> 
    '''

    #craete a svg creator
    def __init__(self,name="newSVG",height=100,width=100):
        self.name=name+".svg"
        self.height=height
        self.width=width
   

    #this creates a new file name and given width,height
    def create(self):
        self.themain=self.themain.format(
            width=self.width,
            height=self.height,
            content=self.content,
            style=self.style
        )
        self.themain=' '.join(self.themain.split())
        
        f = open(self.name, "w")
        f.write(self.themain)
        print(self.themain)
        f.close()








    # from here the all codes are for creating and managing shape 
    # here are some functions with inheritance which are  craeted to make shapes

    def setBackground(self,color):
        mainColour=" background-color:rgb({R},{G},{B});"
        mainColour=mainColour.format(
            R=color[0],
            G=color[1],
            B=color[2]
        )
        self.style=mainColour

    def setStrokeWidth(self,width):
        self.__strokeWidth=width;

    def setStrokeColor(self,color):
        mainColour="rgb({R},{G},{B});"
        mainColour=mainColour.format(
            R=color[0],
            G=color[1],
            B=color[2]
        )
        self.__strokeColor=mainColour;
    
    def setStrokeOpacity(self,opacity):
        self.__strokeOpacity=opacity;

    def setShapeOpacity(self,opacity):
        self.__shapeOpacity=opacity;


    def rect(self,x,y,height,width,color,corner=0):
        #this is the main string svg code of rectangle
        mainRect='''<rect 
                        x="{x}"
                        y="{y}" 
                        rx="{corner}" 
                        ry="{corner}" 
                        width="{width}" 
                        height="{height}"
                        style="fill:rgb({R},{G},{B});
                        stroke:{stroke};
                        stroke-width:{strokeWidth};
                        fill-opacity:{fillOpacity};
                        stroke-opacity:{strokeOpacity}" 
                    />'''
        R=color[0]
        G=color[1]
        B=color[2]
        mainRect=mainRect.format(
            x=x,
            y=y,
            corner=corner,
            width=width,
            height=height,
            R=R,
            G=G,
            B=B,
            stroke=self.__strokeColor,
            strokeWidth=self.__strokeWidth,
            fillOpacity=self.__shapeOpacity,
            strokeOpacity=self.__strokeOpacity
        )
        self.content+=mainRect


    def circle(self,x,y,radius,color):
        #this is the main string svg code of rectangle
        mainCircle='''<circle
                        x="{x}"
                        y="{y}" 
                        radius="{radius}"
                        style="fill:rgb({R},{G},{B});
                        stroke:{stroke};
                        stroke-width:{strokeWidth};
                        fill-opacity:{fillOpacity};
                        stroke-opacity:{strokeOpacity}" 
                    />'''
        R=color[0]
        G=color[1]
        B=color[2]
        mainCircle=mainCircle.format(
            x=x,
            y=y,
            radius=radius,
            R=R,
            G=G,
            B=B,
            stroke=self.__strokeColor,
            strokeWidth=self.__strokeWidth,
            fillOpacity=self.__shapeOpacity,
            strokeOpacity=self.__strokeOpacity
        )
        self.content+=mainCircle


    def line(self,pos1,pos2):
            #this is the main string svg code of rectangle
            mainLine='''<line 
                            x1="{x1}"
                            y1="{y1}" 
                            x2="{x2}"
                            y2="{y2}"
                            style="stroke:{stroke};
                            stroke-width:{strokeWidth};
                            fill-opacity:{fillOpacity};
                            stroke-opacity:{strokeOpacity}" 
                        />'''

            mainLine=mainLine.format(
                x1=pos1[0],
                y1=pos1[1],
                x2=pos2[0],
                y2=pos2[1],
                stroke=self.__strokeColor,
                strokeWidth=self.__strokeWidth,
                fillOpacity=self.__shapeOpacity,
                strokeOpacity=self.__strokeOpacity
            )
            
            self.content+=mainLine
            



