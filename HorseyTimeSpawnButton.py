import bpy
import bmesh
from . HorseyTimExtraFunctions import ExtraFunc
class SpawnOperator(bpy.types.Operator):
    iiii = 0
    mesh_name_mapping = {}
    locations = []
    meshs = []
    bm = bmesh.new()
    ogBm = bmesh.new()
    totalvertNum = len(bm.verts)
    numModVerts = totalvertNum/3
    omeshTrail = object
    #ogmeshTrail= object
    bl_idname = "wm.spawn_op_hello_world"
    bl_label = "Minimal Operator"
    def getVertCoordinates():
        #bpy.ops.object.mode_set(mode='EDIT')
        meshLocs = bpy.context.scene.objects["MeshTrail"]
        
        print(meshLocs)
        wmtx = meshLocs.matrix_world
        vertList = [(wmtx @ vertex.co) for vertex in meshLocs.data.vertices if vertex.select]
        #bpy.ops.object.mode_set(mode='OBJECT')
        return vertList

    def SafeObjectDelete():
        objs = bpy.data.objects
        objs.remove(SpawnOperator.meshs[1], do_unlink=True)
        SpawnOperator.meshs.pop(1)
    
    def CopyAndConvert(Empty):
        ob = SpawnOperator.mesh_name_mapping[f"Empty{str(SpawnOperator.iiii)}"].copy()
        ob.data = Empty.data
        bpy.context.collection.objects.link(ob)
        #ob.data.convert(target='MESH')
        mesh = bpy.data.meshes.new_from_object(ob)
        new_obj = bpy.data.objects.new("MeshTrail", mesh)
        SpawnOperator.mesh_name_mapping[f"MeshTrail{str(SpawnOperator.iiii)}"] = new_obj
        from . HorseyTimeFrameChange import MeshTrailBmesh
        InstanceBmesh = MeshTrailBmesh(bmesh.new(),bmesh.new())
        SpawnOperator.mesh_name_mapping[f"Bmesh{str(SpawnOperator.iiii)}"] = InstanceBmesh
        #SpawnOperator.ogmeshTrail = new_obj
        new_obj.matrix_world = ob.matrix_world
        #new_obj = "CustomProp"
        
        ExtraFunc.SelectDelete(ob)
        
        SpawnOperator.mesh_name_mapping[f"Bmesh{str(SpawnOperator.iiii)}"].ogBm.from_mesh(new_obj.data)
        for vert in SpawnOperator.mesh_name_mapping[f"Bmesh{str(SpawnOperator.iiii)}"].ogBm.verts:
            #print("AAA")
            vert.co.x +=1
        SpawnOperator.mesh_name_mapping[f"Bmesh{str(SpawnOperator.iiii)}"].ogBm.to_mesh(new_obj.data)
        new_obj.data.update()
        bpy.context.collection.objects.link(new_obj)
        new_obj.parent = Empty
        #SpawnOperator.meshs.append(new_obj)
        #ob.location = SpawnOperator.locations[1]
        #ob.select_set(True)
        
    def EmptyInit(Empty):
        
        #bpy.ops.object.mode_set(mode='EDIT')
        #bpy.ops.curve.select_all(action='TOGGLE')
        #ob =SpawnOperator.CopyAndConvert(Empty)
        ExtraFunc.SpawnOnce(Empty)
        totalvertNum = len(SpawnOperator.bm.verts)
        numModVerts = totalvertNum/3
        SpawnOperator.totalvertNum = len(SpawnOperator.bm.verts)
        SpawnOperator.numModVerts = SpawnOperator.totalvertNum/3
        
        
    def my_handler(scene):
       
        #Empty = bpy.context.scene.objects["EmpyObj"]
        
        
        #numVerts = (SpawnOperator.totalvertNum)
        #print(f"numverts{numVerts}")
        #vertlist = SpawnOperator.getVertCoordinates()
        i = 0
        j = 0
        #print()
        while j < SpawnOperator.iiii:
            j+=1
            i=0
            SpawnOperator.numModVerts =  len(SpawnOperator.mesh_name_mapping[f"MeshTrail{str(j)}"].data.vertices)
            print(f"J:  {j} Which Mestrail")
            print(SpawnOperator.mesh_name_mapping[f"Bmesh{str(j)}"])
            print(SpawnOperator.numModVerts*2)
            #print(SpawnOperator.iiii)
            #SpawnOperator.numModVerts = SpawnOperator.numModVerts/3
            while i < SpawnOperator.numModVerts:
                #print(f"{i +(SpawnOperator.totalvertNum *2)}){SpawnOperator.bm.verts[int(i +(SpawnOperator.numModVerts *2))].co}  {int(i +SpawnOperator.totalvertNum)} {SpawnOperator.bm.verts[int(i +SpawnOperator.numModVerts ) ].co}  ")
                #print(f"{i} {SpawnOperator.bm.verts[int(i )].co}")
                SpawnOperator.mesh_name_mapping[f"Bmesh{str(j)}"].bm.verts[int(i +(SpawnOperator.numModVerts*2))].co = SpawnOperator.mesh_name_mapping[f"Bmesh{str(j)}"].bm.verts[int(i +SpawnOperator.numModVerts )].co 
                SpawnOperator.mesh_name_mapping[f"Bmesh{str(j)}"].bm.verts[int(i +SpawnOperator.numModVerts )].co  = SpawnOperator.mesh_name_mapping[f"Bmesh{str(j)}"].bm.verts[int(i )].co
                v_local = SpawnOperator.mesh_name_mapping[f"MeshTrail{str(j)}"].data.vertices[i].co # local vertex coordinate
                v_global = SpawnOperator.mesh_name_mapping[f"MeshTrail{str(j)}"].matrix_world @ v_local
                SpawnOperator.mesh_name_mapping[f"Bmesh{str(j)}"].bm.verts[int(i )].co = v_global
            
                i+=1
            SpawnOperator.mesh_name_mapping[f"Bmesh{str(j)}"].bm.to_mesh(SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(j)}"].data)
            SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(j)}"].data.update()
            
        #SpawnOperator.bm.to_mesh(SpawnOperator.omeshTrail.data)
        #SpawnOperator.omeshTrail.data.update()
            
            
        
    def execute(self, context):
        
        if len(bpy.context.selected_objects) == 1:
            print("One")
            objType = getattr(bpy.context.selected_objects[0], 'type', '')

            if objType in ['CURVE']:
                SpawnOperator.iiii+=1
                print("and is curve")
                SpawnOperator.mesh_name_mapping[f"Empty{str(SpawnOperator.iiii)}"] = bpy.context.selected_objects[0]
                print(f"Empty{str(SpawnOperator.iiii)}")
                UID_short = "asd"
                name = f"color_{UID_short}"

                #bpy.context.selected_objects[0][name] = (1.0, 0.0, 0.0, 1.0)
                #ui_prop =  bpy.context.selected_objects[0].id_properties_ui(name)
                #ui_prop.update()
                
                
                SpawnOperator.EmptyInit(SpawnOperator.mesh_name_mapping[f"Empty{str(SpawnOperator.iiii)}"])
                #if len(bpy.app.handlers.frame_change_pre) == 0:            
                bpy.app.handlers.frame_change_pre.append(SpawnOperator.my_handler)
        return {'FINISHED'}


