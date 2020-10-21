from PIL import Image, ImageDraw
import math
class Vec2:
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
    def to_tu(self):
        return (self.x,self.y)
    x=0
    y=0
class Vec3:
    x=0
    y=0
    z=0
    def construct(self,inlst):
        ret = Vec3(inlst)
        return ret
    def __init__(self,inlst):
        self.x = inlst[0]
        self.y = inlst[1]
        self.z = inlst[2]
    def to_string(self):
        return str(self.x)+" "+str(self.y)+" "+str(self.z)
    def scale(self,scale):
        a = self.x * scale
        b = self.y * scale
        c = self.z * scale
        ret = Vec3((a,b,c))
        return ret
    def rx(self,ang):
        x = self.y
        y = self.z
        self.y = (x*math.cos(ang))-(y*math.sin(ang))
        self.z = (x*math.sin(ang))+(y*math.sin(ang))
    def ry(self,ang):
        x = float(self.x) * 1
        y = float(self.z) * 1
        self.x = (x*math.cos(ang))-(y*math.sin(ang))
        self.z = (x*math.sin(ang))+(y*math.sin(ang))
    def rz(self,ang):
        x = self.x
        y = self.y
        self.x = (x*math.cos(ang))-(y*math.sin(ang))
        self.y = (x*math.sin(ang))+(y*math.sin(ang))
    def to_3D(self,w):
        self.x = self.x / w
        self.y = self.y / w
        self.z = self.z / w
    def to_2D(self):
        #print("~~~~~~~~~~")
        ##print(str(self.x)+" : "+str(self.y)+" : "+str(self.z))
        self.x = self.x/self.z
        self.y = self.y/self.z
        #print(str(self.x)+" : "+str(self.y))
        #os.system("pause")
        return Vec2(self.x,self.y)
class tri:
    def __init__(self,points):
        #print(points[0])
        self.p1 = points[0]
        self.p2 = points[1]
        self.p3 = points[2]
    p1 = "NULL"
    p2 = "NULL"
    p3 = "NULL"
class Render3D:
    pos = (-2,-94,-105)
    rot = (0,0,0)
    zf = 0.0001
    zn = 0.1
    objs = []
    image = "NULL"
    drawer = "NULL"
    f = "NULL"
    q =  "NULL" 
    def __init__(self):
        self.image =  Image.new("RGBA", (500, 500), (0,0,0,0))
        self.drawer = ImageDraw.Draw(self.image)
        self.q = self.zf / (self.zf - self.zn)
        self.f = float(1/math.tan(90/2))
    def load(self,file_path,color):
        f = open(file_path, "r")
        lines = f.read().split('\n')
        vertex = []
        mesh = []
        #print(lines)
        for line in lines:
         #   print(line)
            if len(line) > 1:
                if line[0]=='v' and line[1]==' ':
                    line = line.replace("v ","")
                    line = line.split(" ")
                    vertex.append(Vec3((float(line[0]),float(line[1]),float(line[2]))))
                else:
                    if line.startswith("f "):
                        line = line.replace("f ","")
                        line = line.split(" ")
                        points = []
                        points.append(vertex[int(line[0].split("/")[0])-1])
                        points.append(vertex[int(line[1].split("/")[0])-1])
                        points.append(vertex[int(line[2].split("/")[0])-1])
                        mesh.append(tri((points)))
        self.objs.append({"name":file_path.replace("./out/","").replace(".obj",""),"obj":mesh,"color":color})        
    def project(self,wire):
        for obj in self.objs:
          if(obj["name"]=="Face"):
            drawer = ImageDraw.Draw(self.image)
            img = Image.open("./out/m.png").convert("RGBA")
            x,y = img.size
            for _x in range(x):
              for _y in range(y):
                color = img.getpixel((_x,_y))
                if(color[3]==255):
                  drawer.point((_x+270,_y+245),fill=color)
                  drawer.point(((x-_x)+205,_y+245),fill=color)          
          for _tri in obj["obj"]:
              points = [_tri.p1,_tri.p2,_tri.p3]
              _points=[]
              for _p in points:
                p = Vec3((_p.x,_p.y,_p.z))
                p=p.scale(1)
                p.ry(self.rot[1])
                p.x=p.x+self.pos[0]
                p.y+=self.pos[1]
                p.z+=self.pos[2]
                z =  p.z
                newp = Vec3((p.x*self.f,p.y*self.f,((z*self.q)-(self.zn*self.q))))
                newp.to_3D(z)
                newp = newp.to_2D()
                newp.x = newp.x + 250
                newp.y = newp.y + 250
                _points.append(newp.to_tu())
              self.drawer.polygon(_points, fill = obj["color"])
              if(wire):
                self.drawer.polygon(_points, outline=(255,255,255,10))
class mario:
    key = [{"name":"hat","adr":["38"]},{"name":"hair","adr":["98","9C","A0","A4"]},{"name":"head","adr":["80","84","88","8C"]},{"name":"arms_chest","adr":["3C","40","44"]},{"name":"overalls","adr":["20","24","28","2C"]},{"name":"gloves","adr":["50","54","58","5C"]},{"name":"shoes","adr":["68","6C","70","74"]}]
    engine = Render3D()
    def find_one(self,name,color):
        for obj in self.engine.objs:
            if(obj["name"].lower()==name):
                obj["color"]=color
                return
    def decode3D(self,name,color):
        if(name=="hat"):
            self.find_one("cappy",color)
            return
        if(name=="hair"):
            self.find_one("haircap",color)
            return
        if(name=="arms_chest"):
            self.find_one("rightupperarm",color)
            self.find_one("leftupperarm",color)
            self.find_one("rightlowerarm",color)
            self.find_one("leftlowerarm",color)
            self.find_one("shirt",color)
            return
        if(name=="head"):
            self.find_one("face",color)
            self.find_one("eyes",color)
            self.find_one("mstash",color)
            return
        if(name=="gloves"):
            self.find_one("righthand",color)
            self.find_one("lefthand",color)
            return
        if(name=="overalls"):
            self.find_one("overalls",color)
            self.find_one("but",color)
            self.find_one("rightupperleg",color)
            self.find_one("rightlowerleg",color)
            self.find_one("leftlowerleg",color)
            self.find_one("leftupperleg",color)
            return
        if(name=="shoes"):
            self.find_one("rightshoe",color)
            self.find_one("leftshoe",color)
            return
        print("\n\nERROR: "+name+" doesnt exist!")
            
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
                            self.decode3D(name,color)
    def render(self,cc,wire):
      decoder = ram()
      self.engine.objs =[]
      self.engine.load("./out/But.obj",(0,0,255,255))
      self.engine.load("./out/RightLowerArm.obj",(255,0,0,255))
      self.engine.load("./out/RightUpperArm.obj",(255,0,0,255))
      self.engine.load("./out/LeftUpperArm.obj",(255,0,0,255))
      self.engine.load("./out/LeftLowerArm.obj",(255,0,0,255))
      self.engine.load("./out/RightHand.obj",(128,128,128,255))
      self.engine.load("./out/LeftHand.obj",(128,128,128,255))
      self.engine.load("./out/RightUpperLeg.obj",(0,0,255,255))
      self.engine.load("./out/RightLowerLeg.obj",(0,0,255,255))
      self.engine.load("./out/LeftUpperLeg.obj",(0,0,255,255))
      self.engine.load("./out/LeftLowerLeg.obj",(0,0,255,255))
      self.engine.load("./out/RightShoe.obj",(128,0,0,255))
      self.engine.load("./out/LeftShoe.obj",(128,0,0,255))
      self.engine.load("./out/HairCap.obj",(128,0,0,255))
      self.engine.load("./out/cappy.obj",(255,0,0,255))
      self.engine.load("./out/shirt.obj",(255,0,0,255))
      self.engine.load("./out/Overalls.obj",(0,0,255,255))
      self.engine.load("./out/Buttons.obj",(255,255,0,255))
      self.engine.load("./out/mstash.obj",(254,193,121,255))
      self.engine.load("./out/Face.obj",(254,193,121,255))

      for mesh in self.engine.objs:
        if(mesh["name"].lower()=="face"):
          self.engine.load("./out/Eyes.obj",mesh["color"])
      #self.decode3D("hat",(255,255,0,255))
      self.decode(decoder.decode(cc))
      self.engine.pos = (-2,-168,400)
      self.engine.project(wire)
      card = self.engine.image.copy()
      img = Image.open("./out/eyes.png").convert("RGBA")
      drawer = ImageDraw.Draw(card)
      x,y = img.size
      for _x in range(x):
        for _y in range(y):
          #card.point(((x*self.pix_size)+_x,(y*self.pix_size)+_y),fill=color)
          color = img.getpixel((_x,_y))
          if(color[3]==255):
            drawer.point((_x+6,_y+14),fill=color)
      img = Image.open("./out/m.png").convert("RGBA")
      x,y = img.size
      for _x in range(x):
        for _y in range(y):
          #card.point(((x*self.pix_size)+_x,(y*self.pix_size)+_y),fill=color)
          color = img.getpixel((_x,_y))
          if(color[3]==255):
            #drawer.point((_x+265,_y+250),fill=color)
            color[3]
      #card.paste(img, (225, 190))
      #img.save("render.png", format="png")
      card.save("./render.png")


class ram:
    def decode(self,instructions):
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

        
