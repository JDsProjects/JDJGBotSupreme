from PIL import Image, ImageDraw
import math
import _3D_t
path = "./out/"
class Render3D:
    pos = (-2,-94,105)
    rot = (0,0,0)
    zf = 0.0001
    zn = 0.1
    objs = []
    image = "NULL"
    drawer = "NULL"
    f = "NULL"
    q =  "NULL" 
    shaders = 0.2
    gamma = 0
    #light = _3D_t.Vec3((1,1,-0.09))
    light = _3D_t.Vec3((-1,0.6,-0.09))
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
        normals=[]
        #print(lines)
        for line in lines:
         #   print(line)
            if len(line) > 1:
                if line[0]=='v' and line[1]==' ':
                    line = line.replace("v ","")
                    line = line.split(" ")
                    tmp = _3D_t.Vec3((float(line[0]),float(line[1]),float(line[2])))
                    for tmp1 in vertex:
                        if(tmp.x==tmp1.x and tmp.y==tmp1.y and tmp.z ==tmp1.z):
                            print(tmp.to_string()+" L: "+str(len(vertex)))
                    vertex.append(tmp)
                else:
                    if line.startswith("vn "):
                      line = line.replace("vn ","").split(" ")
                      normals.append(_3D_t.Vec3((float(line[0]),float(line[1]),float(line[2]))))
                    else:
                      if line.startswith("f "):
                          line = line.replace("f ","")
                          line = line.split(" ")
                          points = []
                          vni = []
                          points.append(vertex[int(line[0].split("/")[0])-1])
                          points.append(vertex[int(line[1].split("/")[0])-1])
                          points.append(vertex[int(line[2].split("/")[0])-1])
                          vni.append(normals[int(line[0].split("/")[2])-1])
                          vni.append(normals[int(line[1].split("/")[2])-1])
                          vni.append(normals[int(line[2].split("/")[2])-1])
                          mesh.append(_3D_t.tri(points,vni))
        
        self.objs.append({"name":file_path.replace(path+"","").replace(".obj",""),"obj":mesh,"color":color})
    def translate(self, _point):
        point = _point
        point=point.scale(1)
        point = point.ry(self.rot[1])
        point = point.rz(self.rot[2])
        point = point.rx(self.rot[0])
        point.x=point.x+self.pos[0]
        point.y+=self.pos[1]
        point.z+=self.pos[2]
        return point
    def shade_8bit(self, byte,shading):
      color_ratio = 1-self.shaders-self.gamma
      return (byte*color_ratio) + (shading*self.shaders) + (255*self.gamma)
      #byte /=255
      #return (byte * shading)*255
    def sproject(self,wire):
        for obj in self.objs:
          if(obj["name"]=="Eyes"):
            drawer = ImageDraw.Draw(self.image)
            img = Image.open(path+"m.png").convert("RGBA")
            x,y = img.size
            for _x in range(x):
              for _y in range(y):
                color = img.getpixel((_x,_y))
                if(color[3]==255):
                  drawer.point((_x+270,_y+245),fill=color)
                  drawer.point(((x-_x)+205,_y+245),fill=color)          
          for _tri in obj["obj"]:
              points = [self.translate(_tri.p1),self.translate(_tri.p2),self.translate(_tri.p3)]
              _points=[]
              line1 = points[1].sub(points[0])
              line2 = points[2].sub(points[0])
              normal = line1.cross(line2)
              _pos = _3D_t.Vec3(self.pos)
              trans_location = _pos.add(points[0])
              normal  = normal.div_f(normal.len())
              normal_dot =normal.dot(trans_location) #normal.rayCast(trans_location)
              if(normal_dot < 0):
                #shading = (self.light.rayCast(normal))*(255)
                #shading = self.light.div_f(self.light.len()).dot(normal)*255
                for _p in points:
                  p = _p
                  z =  p.z
                  newp = _3D_t.Vec3((p.x*self.f,p.y*self.f,((z*self.q)-(self.zn*self.q))))
                  newp.to_3D(z)
                  newp = newp.to_2D(1)
                  newp.x = newp.x + 250
                  newp.y = newp.y + 250
                  _points.append(newp)
                toBeRasturized = _3D_t.tri(_points,(_tri.n1,_tri.n2,_tri.n3))
                color = _3D_t.Vec3((obj["color"]))
                toBeRasturized.FillShadeTru(self.drawer,color,self.shaders)
                if(wire):
                    new_points = [(_points[0].x,_points[0].y),(_points[1].x,_points[1].y),(_points[2].x,_points[2].y)]
                    self.drawer.polygon(new_points, outline=(0,0,0,255))
                
    def project(self,wire):
        for obj in self.objs:
          if(obj["name"]=="Face"):
            drawer = ImageDraw.Draw(self.image)
            img = Image.open(path+"m.png").convert("RGBA")
            x,y = img.size
            for _x in range(x):
              for _y in range(y):
                color = img.getpixel((_x,_y))
                if(color[3]==255):
                  drawer.point((_x+270,_y+245),fill=color)
                  drawer.point(((x-_x)+205,_y+245),fill=color)          
          for _tri in obj["obj"]:
              points = [self.translate(_tri.p1),self.translate(_tri.p2),self.translate(_tri.p3)]
              _points=[]
              line1 = points[1].sub(points[0])
              line2 = points[2].sub(points[0])
              normal = line1.cross(line2)
              _pos = _3D_t.Vec3(self.pos)
              trans_location = _pos.add(points[0])
              normal  = normal.div_f(normal.len())
              normal_dot =normal.dot(trans_location) #normal.rayCast(trans_location)
              if(normal_dot < 0):
                #shading = (self.light.rayCast(normal))*(255)
                shading = self.light.div_f(self.light.len()).dot(normal)*255
                for _p in points:
                  p = _p
                  z =  p.z
                  newp = _3D_t.Vec3((p.x*self.f,p.y*self.f,((z*self.q)-(self.zn*self.q))))
                  newp.to_3D(z)
                  newp = newp.to_2D()
                  newp.x = newp.x + 250
                  newp.y = newp.y + 250
                  _points.append(newp.to_tu())
                color = _3D_t.Vec3((obj["color"]))
                color.x=self.shade_8bit(color.x, shading)
                color.y=self.shade_8bit(color.y, shading)
                color.z=self.shade_8bit(color.z, shading)
                color = (int(color.x), int(color.y), int(color.z))
                self.drawer.polygon(_points, fill = color)
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
            self.find_one("logo",color)
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
            self.find_one("hairpiece",color)
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
    def set_rot(self, x,y,z):
      x = x * (3.14/180)
      y = y * (3.14/180)
      z = z * (3.14/180)
      self.engine.rot = (x,y,z)
    def render(self,cc,wire,smooth=0,user="NULL"):
      decoder = ram()
      #path = "./obj1/"
      self.engine.objs =[]
      self.engine.load(path+"But.obj",(0,0,255,255))
      self.engine.load(path+"RightLowerArm.obj",(255,0,0,255))
      self.engine.load(path+"RightUpperArm.obj",(255,0,0,255))
      self.engine.load(path+"LeftLowerArm.obj",(255,0,0,255))
      self.engine.load(path+"LeftUpperArm.obj",(255,0,0,255))

      self.engine.load(path+"RightHand.obj",(255,255,255,255))
      self.engine.load(path+"LeftHand.obj",(255,255,255,255))
      #rightLeg
      self.engine.load(path+"RightShoe.obj",(128,0,0,255))
      self.engine.load(path+"RightLowerLeg.obj",(0,0,255,255))
      self.engine.load(path+"RightUpperLeg.obj",(0,0,255,255))
      #leftLeg
      self.engine.load(path+"LeftShoe.obj",(128,0,0,255))
      self.engine.load(path+"LeftLowerLeg.obj",(0,0,255,255))
      self.engine.load(path+"LeftUpperLeg.obj",(0,0,255,255))
      
      self.engine.load(path+"HairCap.obj",(128,0,0,255))
      self.engine.load(path+"hairPiece.obj",(254,193,121,255))
      self.engine.load(path+"cappy.obj",(255,0,0,255))
      self.engine.load(path+"Overalls.obj",(0,0,255,255))    
      self.engine.load(path+"shirt.obj",(255,0,0,255))
      self.engine.load(path+"logo.obj",(255,0,0,255))
      self.engine.load(path+"Buttons.obj",(255,255,0,255))
      self.engine.load(path+"mstash.obj",(254,193,121,255))
      self.engine.load(path+"Face.obj",(254,193,121,255))

      for mesh in self.engine.objs:
        if(mesh["name"].lower()=="face"):
          self.engine.load(path+"Eyes.obj",mesh["color"])
      #self.decode3D("hat",(255,255,0,255))
      self.decode(decoder.decode(cc))
      self.engine.pos = (-2,-168,400)
      self.set_rot(0,360/2,0)
      if smooth:
          self.engine.sproject(wire)
      else:
          self.engine.project(wire)
      card = self.engine.image.copy()
      img = Image.open(path+"eyes.png").convert("RGBA")
      drawer = ImageDraw.Draw(card)
      x,y = img.size
      for _x in range(x):
        for _y in range(y):
          #card.point(((x*self.pix_size)+_x,(y*self.pix_size)+_y),fill=color)
          color = img.getpixel((_x,_y))
          if(color[3]==255):
            drawer.point((_x+6,_y+14),fill=color)
      img = Image.open(path+"m.png").convert("RGBA")
      x,y = img.size
      for _x in range(x):
        for _y in range(y):
          #card.point(((x*self.pix_size)+_x,(y*self.pix_size)+_y),fill=color)
          color = img.getpixel((_x,_y))
          if(color[3]==255):
            #drawer.point((_x+265,_y+250),fill=color)
            color[3]
      if(user!=168422909482762240):
        logo = path+"Logo.png"
      else:
        logo = path+"jdjg.png"
      img = Image.open(logo).convert("RGBA")
      x,y = img.size
      for _x in range(x):
        for _y in range(y):
          #card.point(((x*self.pix_size)+_x,(y*self.pix_size)+_y),fill=color)
          color = img.getpixel((_x,_y))
          off = 120
          if(color[3]==255):
            drawer.point(((_x*2)+220,(_y*2)+off),fill=color)
            drawer.point(((_x*2)+220,(_y*2)+off+1),fill=color)
            drawer.point(((_x*2)+221,(_y*2)+off),fill=color)
            drawer.point(((_x*2)+221,(_y*2)+off+1),fill=color)
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

        
