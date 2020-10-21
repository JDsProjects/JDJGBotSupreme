from PIL import Image, ImageDraw, ImageFont
class Pixman:
    image="NULL"
    drawer="NULL"
    pix_size=2
    w=2
    h=2
    reg = []
    def __init__(self, width, height, pixelsize):
        self.image = Image.new("RGBA", (width*pixelsize, height*pixelsize), (0,0,0,0))
        self.drawer = ImageDraw.Draw(self.image)
        self.w = width
        self.h = height
        self.pix_size = pixelsize
    def drawp(self,x,y,color):
        #self.drawer.rectangle((x,y,self.pix_size,self.pix_size),fill=color)
        for _x in range(self.pix_size):
            for _y in range(self.pix_size):
                
                self.drawer.point(((x*self.pix_size)+_x,(y*self.pix_size)+_y),fill=color)
    def rectangle(self, x,y,_w,_h,color):
        #self.draw.rectangle((x*self.pix_size,y*self.pix_size,(_w*1)*self.pix_size,(_h*1)*self.pix_size),fill=color
        for _x in range(_w):
            for _y in range(_h):
                self.drawp(x+_x,y+_y,color)
    def add_region(self, region_name,color, pix):
        self.reg.append({"name":region_name,"pix":pix,"color":color})
    def get_region(self, region_name):
        for obj in self.reg:
            if obj["name"] == region_name:
                return obj
    def set_region(self, region_name,color):
        i=-1
        for obj in self.reg:
            i = i + 1
            if obj["name"] == region_name:
                self.reg[i]["color"] = color
    def find_region(self,region_name):
        for obj in self.reg:
            if (obj["name"]==region_name):
                return 1
        return 0
    def render(self):
        for obj in self.reg:
            for pixel in obj["pix"]:
                self.drawp(pixel[0],pixel[1],obj["color"])
    def export(self, file_name):
        self.image.save(file_name)
    key = [{"name":"hat","adr":["38"]},{"name":"hair","adr":["98","9C","A0","A4"]},{"name":"head","adr":["80","84","88","8C"]},{"name":"arms_chest","adr":["3C","40","44"]},{"name":"overalls","adr":["20","24","28","2C"]},{"name":"gloves","adr":["50","54","58","5C"]},{"name":"shoes","adr":["68","6C","70","74"]}]
    def decode(self,cc):
       # print(cc)
        for cc_doc in cc:
            color = (cc_doc["rgb"]["r"],cc_doc["rgb"]["g"],cc_doc["rgb"]["b"],255)
            for key_doc in self.key:
                name = key_doc["name"]
                #print(name)
                for cc_adr in cc_doc["adr"]:
                    #print(obj1["name"])
                    #print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    for obj1 in key_doc["adr"]:
                        if(cc_adr== obj1):
                            #print(cc_adr +"   OBJ:  "+obj)
                            self.set_region(name,color)
def get():
  myImage=Pixman(12,16,18)
  myImage.add_region("hat",(255,0,0,255),[(3,0),(4,0),(5,0),(6,0),(7,0),(2,1),(3,1),(4,1),(5,1),(6,1),(7,1),(8,1),(9,1),(10,1)])
  myImage.add_region("hair",(115,6,0,255),[(2,2),(3,2),(4,2),(3,3),(3,4),(4,4),(2,5),(1,5),(1,4),(1,3)])
  myImage.add_region("head",(254,193,121,255),[(5,2),(6,2),(8,2),(2,3),(4,3),(5,3),(6,3),(8,3),(9,3),(10,3),(2,4),(5,4),(6,4),(7,4),(9,4),(10,4),(11,4),(3,5),(4,5),(5,5),(6,5),(3,6),(4,6),(5,6),(6,6),(7,6),(8,6),(9,6)])
  myImage.add_region("face",(0,0,0,255),[(7,2),(7,3),(8,4),(7,5),(8,5),(9,5),(10,5)])
  myImage.add_region("arms_chest",(255,0,0,255),[(2,7),(3,7),(5,7),(6,7),(7,7),(1,8),(2,8),(3,8),(5,8),(6,8),(8,8),(9,8),(10,8),(0,9),(1,9),(2,9),(3,9),(8,9),(9,9),(10,9),(11,9),(2,10),(9,10)])
  myImage.add_region("overalls",(0,0,255,255),[(4,7),(4,8),(7,8),(4,9),(5,9),(6,9),(7,9),(3,10),(5,10),(6,10),(8,10),(3,11),(4,11),(5,11),(6,11),(7,11),(8,11),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12),(9,12),(2,13),(3,13),(4,13),(7,13),(8,13),(9,13)])
  myImage.add_region("buttons",(255,255,0,255),[(4,10),(7,10)])
  myImage.add_region("gloves",(224,224,224,255),[(0,10),(1,10),(0,11),(1,11),(2,11),(0,12),(1,12),(10,10),(11,10),(10,11),(11,11),(9,11),(10,12),(11,12)])
  myImage.add_region("shoes",(128,0,0,255),[(1,14),(2,14),(3,14),(8,14),(9,14),(10,14),(1,15),(2,15),(3,15),(8,15),(9,15),(10,15),(0,15),(11,15)])
  return myImage
  
class ram:
    def b(self,instructions):
        lines=instructions.split("\n")
        color_code = []
        x=0
        while x+1 < len(lines):
            color_value = lines[x]
            color_value2 = lines[x+1]
            colored_bit=color_value.split(" ")
            colored_bit2 = color_value2.split(" ")
            color_code_front = colored_bit[0].replace("8107EC","")
            color_code_front2 = colored_bit2[0].replace("8107EC","")
            color_section = colored_bit[1]
            color_section2 = colored_bit2[1]
            r = int(color_section[0:2], 16)
            g = int(color_section[2:4], 16)
            b = int(color_section2[0:2], 16)
            color_code.append({"adr":[color_code_front,color_code_front2],"rgb":{"r":r,"g":g,"b":b}})
            x+=2
        return color_code
    def encode(color_code):
        ret = ""
        for obj in color_code:
            ret+=("\n81"+obj["adr"][0]+" "+str(obj["rgb"]["r"])+str(obj["rgb"]["g"])+"\n")
            ret+=("81"+obj["adr"][1]+" "+str(obj["rgb"]["b"])+"00\n")
        return ret
            
            
def convertTuple(tup):
    return str(tup[0])+", "+str(tup[1])+", "+str(tup[2])
