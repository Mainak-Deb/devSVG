from basicSVG import basicSVG


class devsvg:
    __mainsvg=""
    name="newsvg"
    height=100;
    height=100;

    #craete a svg creator
    def __init__(self,name="newsvg",width=100,height=100):
        self.name=name+".svg"
        self.height=height
        self.width=width
        self.__mainsvg=basicSVG(self.name,self.width,self.height);
    

    def publish(self):
        self.__mainsvg.create();
