import math
class Vec2:
  def __init__(self,_x,_y):
    self.x = _x
    self.y = _y
class tri2d:
  def __init__(self, _p1,_p2,_p3):
    self.p1 = _p1
    self.p2 = _p2
    self.p3 = _p3
  def p_init(self,p):
    self.p1 = p[0]
    self.p2 = p[1]
    self.p3 = p[2]
  def area(self):
    a= self.p1
    b = self.p2
    c = self.p3
    return abs(((a.x*(b.y-c.x))+(b.x*(c.x-a.x))+(c.x*(a.x-b.x))/2))
class transFace:
  def __init__(self, vertex, normals):
    self.v = vertex
    self.n = normals
  def smoothShade(self,point,lighting,color="NULL"):
    a = self.v.area()
    a1 = tri2d(self.v.p1,self.v.p2,point)
    a2 = tri2d(self.v.p1,self.v.p3,point)
    a3 = tri2d(self.v.p3,self.v.p2,point)
    mixer= [a1/a,a2/a,a3/a]
    normal_lighting = [lighting.rayCast(self.n.p1),lighting.rayCast(self.n.p2),lighting.rayCast(self.n.p3)]
    avg = (mixer[0]*normal_lighting[0])+(mixer[1]*normal_lighting[1])+(normal_lighting[2]*mixer[2])
    if(color!="NULL"):
      return ((color[0]+avg)/2,(color[1]+avg)/2,(color[2]+avg)/2)
    else:
      return avg
  def Fill(self, color):
    x1 = self.v.p1.x
    y1 = self.v.p1.y
    x2 = self.v.p2.x
    y2 = self.v.p2.y
    x3 = self.v.p3.x
    y3 = self.v.p3.y
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
      i=y1
      for i in range(y1,y2):
        ax = x1 + (i - y1) * dax_step
        bx = x1 + (i - y1) * dbx_step
        if (ax > bx):
          tmp = ax
          ax = bx
          bx = tmp

        #for j in range(ax,bx):
					#Draw(j, i)

		#dy1 = y3 - y2;
		#dx1 = x3 - x2;

		#if (dy1) dax_step = dx1 / (float)abs(dy1);
		#if (dy2) dbx_step = dx2 / (float)abs(dy2);
		#if (dy1)
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



