from json.tool import main
from tkinter.ttk import Style
from turtle import shapesize


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
        print(color)
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

