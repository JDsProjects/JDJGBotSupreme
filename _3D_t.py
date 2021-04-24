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
        x = self.x
        y = self.y
        z = self.z
        y1 = (y*math.cos(ang))-(z*math.sin(ang))
        z1 = (y*math.sin(ang))+(z*math.cos(ang))
        ret = Vec3((x, y1,z1))
        return ret

    def ry(self,ang):
        x = float(self.x) * 1
        y = self.y
        z = float(self.z) * 1
        x1 = (x*math.cos(ang))-(z*math.sin(ang))
        z1 = (x*math.sin(ang))+(z*math.cos(ang))
        ret = Vec3((x1,y,z1))
        return ret
    def rz(self,ang):
        x = self.x
        y = self.y
        z = self.z
        x1 = (x*math.cos(ang))-(y*math.sin(ang))
        y1 = (x*math.sin(ang))+(y*math.cos(ang))
        ret = Vec3((x1,y1,z))
        return ret
    def to_3D(self,w):
        self.x = self.x / w
        self.y = self.y / w
        self.z = self.z / w
    def to_2D(self,_type=0):
        #print("~~~~~~~~~~")
        ##print(str(self.x)+" : "+str(self.y)+" : "+str(self.z))
        self.x = self.x/self.z
        self.y = self.y/self.z
        #print(str(self.x)+" : "+str(self.y))
        #os.system("pause")
        if(_type):
            return self
        else:
            return Vec2(self.x,self.y)
    
    def cross(self,line):
      b= line
      a = self
      ret = Vec3((0,0,0))
      ret.x = (a.y * b.z) - (a.z * b.y)
      ret.y = (a.z * b.x) - (a.x * b.z)
      ret.z = (a.x * b.y) - (a.y * b.x)
      return ret
    def len(self):
      return math.sqrt((self.x*self.x)+(self.y*self.y)+(self.z*self.z))
    def dot(self,line):
      a = self
      b = line
      return (a.x * b.x) + (a.y * b.y) + (a.z * b.z)
    def sub(self, point):
      ret = Vec3((0,0,0))
      ret.x = self.x - point.x
      ret.y = self.y - point.y
      ret.z = self.z - point.z
      return ret
    def add(self, point):
      ret = Vec3((0,0,0))
      ret.x = self.x + point.x
      ret.y = self.y + point.y
      ret.z = self.z + point.z
      return ret
    def mul(self, vector):
      ret = Vec3((0,0,0))
      ret.x = self.x*vector.x
      ret.y = self.y*vector.y
      ret.z = self.z*vector.z
      return ret
    def div_f(self, num):
      ret = Vec3((0,0,0))
      ret.x = self.x/num
      ret.y = self.y/num
      ret.z = self.z/num
      return ret
    def reverse(self):
        return Vec3((self.z,self.y,self.x))
    def rayCast(self,line):
      ret = Vec3((0,0,0))
      _len = self.len()
      ret.x = self.x/_len
      ret.y = self.y/_len
      ret.z = self.z/_len
      ret = ret.dot(line)
      return ret
    def mix(self, color1,rat=0.5):
        c1= self.scale(1-rat)
        c2= color1.scale(rat)
        return c1.add(c2)
        
            

class tri:
    def __init__(self,v,n,t="NULL"):
        #print(points[0])
        light = Vec3((-1,0.6,0.5))
        self.p1 = v[0]
        self.p2 = v[1]
        self.p3 = v[2]
        if(t=="NULL"):
            self.n1 = n[0]
            self.n2 = n[1]
            self.n3 = n[2]
            normalized_L = light.div_f(light.len())
            self.normal_lighting = Vec3((normalized_L.dot(self.n1)*255,normalized_L.dot(self.n2)*255,normalized_L.dot(self.n3)*255))
            #self.normal_lighting = [normalized_L.dot(self.n1),normalized_L.dot(self.n2),normalized_L.dot(self.n3)]
    def to_string(self):
        return self.p1.to_string()+" / "+self.p2.to_string()+" / "+self.p3.to_string()
    def area(self):
        a= self.p1
        b = self.p2
        c = self.p3
        a.x = int(a.x)
        a.y = int(a.y)
        b.x = int(b.x)
        b.y = int(b.y)
        c.x = int(c.x)
        c.y = int(c.y)
        a1 = a.x*(b.y-c.y)
        a2 = b.x*(c.y-a.y)
        a3 = c.x*(a.y-b.y)
        #print(" A1: "+str(a.x)+" A2: "+str((b.x))+" A3: "+str((c.x)))
        #print("A: "+a.to_string()+" B: "+b.to_string()+" C: "+c.to_string())
        #print(" A1: "+str(a1)+" A2: "+str(a2)+" A3: "+str(a3))

        #import os
        #os.system("pause")
        return abs((a1+a2+a3)/2)
    def Shade_p(self,point,shader,color="NULL",diffuse=Vec3((0,0,0))):
        diffuse = diffuse.scale(0.01) #intensity
        a = self.area()
        a1 = tri((self.p1,self.p2,point),0,0).area()
        a2 = tri((self.p1,self.p3,point),0,0).area()
        a3 = tri((self.p3,self.p2,point),0,0).area()
        #print("A: "+str(a)+" A1: "+str(a1)+" A2: "+str(a2)+" A3: "+str(a3))
        mixer= [a1/a,a2/a,a3/a]
        #print(shader)
        avg = ((mixer[0]*self.normal_lighting.z)+(mixer[1]*self.normal_lighting.y)+(self.normal_lighting.x*mixer[2]))
        color_r = 1-shader
        if(diffuse.x ==0 and diffuse.y==0 and diffuse.z==0):
            #print("BANANA")
            #color = color.scale(color_r)
            #color.add(Vec3((avg*shader,avg*shader,avg*shader)))
            r = (color.x*color_r) + (avg*shader)
            g = (color.y*color_r) + (avg*shader)
            b = (color.z*color_r) + (avg*shader)
        else:
            color = color.scale(color_r)
            color = color.mix(diffuse.scale(avg),shader)
            r = color.x
            g = color.y
            b = color.z
        #r = (color.x*color_r) + (avg*shader)
        #g = (color.y*color_r) + (avg*shader) 
        #b = (color.z*color_r) + (avg*shader)
        return (int(r),int(g),int(b),255)
    def FillShadeTru(self, drawer,color,shader):
        
        #print(self.to_string())
        x1 = int(self.p1.x)
        y1 = int(self.p1.y)
        x2 = int(self.p2.x)
        y2 = int(self.p2.y)
        x3 = int(self.p3.x)
        y3 = int(self.p3.y)
        if (y2 < y1):
          tmp = y1
          y1= y2
          y2 = tmp
          tmp = x1
          x1= x2
          x2 = tmp
        if (y3 < y1):
          tmp = y1
          y1= y3
          y3 = tmp
          tmp = x1
          x1= x3
          x3 = tmp
        if (y3 < y2):
            tmp = y2
            y2= y3
            y3 = tmp
            tmp = x2
            x2= x3
            x3 = tmp
      
        dy1 = y2 - y1
        dx1 = x2 - x1

        dy2 = y3 - y1
        dx2 = x3 - x1
        dax_step = 0
        dbx_step = 0
        if (dy1): 
          dax_step = dx1 / abs(dy1)
        if (dy2):
           dbx_step = dx2 / abs(dy2)
        if (dy1):
            for i in range(int(y1),int(y2+1)):
                ax = x1 + int(float(i - y1) * float(dax_step))
                bx = x1 + int(float(i - y1) * float(dbx_step))
                if (ax > bx):
                    tmp = ax
                    ax = bx
                    bx = tmp
                for j in range(int(ax),int(bx)):
                    color1 = self.Shade_p(Vec3((j,i,0)),shader,color)
                    drawer.point((j,i),fill=color1)
                    #print("X: "+str(j)+" Y: "+str(i))
        dy1 = y3 - y2;
        dx1 = x3 - x2;

        if (dy1):
            dax_step = dx1 / abs(dy1);
        if (dy2):
            dbx_step = dx2 / abs(dy2);
        if (dy1):
            for i in range(int(y2),int(y3+1)):
                ax = x2 + int(float(i - y2) * float(dax_step))
                bx = x1 + int(float(i - y1) * float(dbx_step))
                if (ax > bx):
                    tmp = ax
                    ax = bx
                    bx = tmp
                for j in range(int(ax),int(bx)):
                    color1 = self.Shade_p(Vec3((j,i,0)),shader,color)
                    drawer.point((j,i),fill=color1)
                    #print("X: "+str(j)+" Y: "+str(i))
		#{
	#		for (int i = y2; i <= y3; i++)
	#		{
	#			int ax = x2 + (float)(i - y2) * dax_step;
	#			int bx = x1 + (float)(i - y1) * dbx_step;
#
#				float tex_su = u2 + (float)(i - y2) * du1_step;
#				float tex_sv = v2 + (float)(i - y2) * dv1_step;
#				float tex_sw = w2 + (float)(i - y2) * dw1_step;
				#float tex_eu = u1 + (float)(i - y1) * #du2_step;
				#float tex_ev = v1 + (float)(i - y1) * dv2_step;
				#float tex_ew = w1 + (float)(i - y1) * dw2_step;

				#if (ax > bx)
				#{
				#	swap(ax, bx);
				#	swap(tex_su, tex_eu);
				#	swap(tex_sv, tex_ev);
				#	swap(tex_sw, tex_ew);
				#}

				#tex_u = tex_su;
				#tex_v = tex_sv;
				#tex_w = tex_sw;

				#float tstep = 1.0f / ((float)(bx - ax));
				#float t = 0.0f;

				#for (int j = ax; j < bx; j++)
				#{
				#	tex_u = (1.0f - t) * tex_su + t * tex_eu;
				#	tex_v = (1.0f - t) * tex_sv + t * tex_ev;
				#	tex_w = (1.0f - t) * tex_sw + t * tex_ew;

				#	if (tex_w > pDepthBuffer[i*ScreenWidth() + j])
				#	{
						#Draw(j, i, tex->SampleGlyph(tex_u / #tex_w, tex_v / tex_w), tex->SampleColour(tex_u / tex_w, tex_v / tex_w));
						#pDepthBuffer[i*ScreenWidth() + j] = tex_w;
					#}
					#t += tstep;
			#	}
			#}	
		#}		
	#}
    p1 = "NULL"
    p2 = "NULL"
    p3 = "NULL"
    n1 = "NULL"
    n2 = "NULL"
    n3 = "NULL"
