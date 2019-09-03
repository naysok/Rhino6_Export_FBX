import rhinoscriptsyntax as rs
import Rhino
import Rhino.Geometry as rg
import ghpythonlib.components as ghpc
import scriptcontext as sc


def boxes(count):
    tmp_box = []
    for i in xrange(count):
        tmp_box.append(ghpc.Box2Pt(
            rg.Point3d(i,i,i),
            rg.Point3d(i+1,i+1,i+1),
            rs.WorldXYPlane()))
    return tmp_box

def mesh_spheres(count):
    tmp_sp = []
    for i in xrange(count):
        tmp_sp.append(ghpc.MeshSphere(
            rs.MovePlane(rs.WorldXYPlane(), (i,i,0)), 0.5, 8, 8))
    return tmp_sp


#box_ = boxes(10)
#print(box_)
#DEBUG = box_

sphere_ = mesh_spheres(10)
# print(sphere_)
DEBUG = sphere_





sc.doc = Rhino.RhinoDoc.ActiveDoc


if BOOL:
    
    for i in xrange(len(DEBUG)):
        
        selMesh = DEBUG[i]
        
        sc.doc.Objects.AddMesh(selMesh)
        
        
        name = "C:\Users\yoshioca\Documents\Rhino6_Export_FBX\Models\\" \
            + str(i) + ".fbx"
            
        query = ' _SelAll ' \
            +' _-Export g  ' \
            + name + ' _Enter _Enter _SelAll _Delete'
        
        print(query)
        rs.Command(query)


sc.doc = Rhino.RhinoDoc.ActiveDoc