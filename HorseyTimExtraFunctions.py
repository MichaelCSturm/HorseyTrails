import bpy
import bmesh

class ExtraFunc():
   
    def SelectDelete(ObjectToBeDeleted):
        objs = bpy.data.objects
        objs.remove(ObjectToBeDeleted, do_unlink=True)
    def SpawnOnce(Empty):
        from . HorseyTimeSpawnButton import SpawnOperator
        SpawnOperator.CopyAndConvert(Empty)
        ExtraFunc.OtherCopyAndConvert(Empty)
        # ExtraFunc.OtherCopyAndConvert(Empty)
        # ExtraFunc.OtherCopyAndConvert(Empty)
        #bpy.data.objects['OtherMeshTrail.003'].select_set(True) 
        # bpy.data.objects['OtherMeshTrail.002'].select_set(True) 
        # bpy.data.objects['OtherMeshTrail.001'].select_set(True) 
        SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(SpawnOperator.iiii)}"].select_set(True) 
        
        bpy.context.view_layer.objects.active = SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(SpawnOperator.iiii)}"]
        SpawnOperator.omeshTrail = SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(SpawnOperator.iiii)}"]
        #bpy.ops.object.join()
        OMeshTrail = SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(SpawnOperator.iiii)}"]
        
        
        #print(OMeshTrail.id)
        
        totalvertNum = len(SpawnOperator.bm.verts)
        numModVerts = totalvertNum/3
        bpy.context.view_layer.objects.active =OMeshTrail 
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_mode(type="VERT")
        SpawnOperator.bm.select_mode |= {'VERT'}
        #SpawnOperator.bm.edges.ensure_lookup_table()
        SpawnOperator.mesh_name_mapping[f"Bmesh{str(SpawnOperator.iiii)}"].ogBm.verts.ensure_lookup_table()
        bpy.ops.mesh.select_all(action='SELECT')

        #bmesh.ops.extrude_edge_only(SpawnOperator.bm,edges=edgey)
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.589937), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.mesh.extrude_region_move(MESH_OT_extrude_region={"use_normal_flip":False, "use_dissolve_ortho_edges":False, "mirror":False}, TRANSFORM_OT_translate={"value":(0, 0, 0.379738), "orient_type":'GLOBAL', "orient_matrix":((1, 0, 0), (0, 1, 0), (0, 0, 1)), "orient_matrix_type":'GLOBAL', "constraint_axis":(False, False, True), "mirror":False, "use_proportional_edit":False, "proportional_edit_falloff":'SMOOTH', "proportional_size":1, "use_proportional_connected":False, "use_proportional_projected":False, "snap":False, "snap_elements":{'INCREMENT'}, "use_snap_project":False, "snap_target":'CLOSEST', "use_snap_self":True, "use_snap_edit":True, "use_snap_nonedit":True, "use_snap_selectable":False, "snap_point":(0, 0, 0), "snap_align":False, "snap_normal":(0, 0, 0), "gpencil_strokes":False, "cursor_transform":False, "texture_space":False, "remove_on_cancel":False, "use_duplicated_keyframes":False, "view2d_edge_pan":False, "release_confirm":False, "use_accurate":False, "use_automerge_and_split":False})
        bpy.ops.object.mode_set( mode = 'OBJECT' )
       
                        
        i= 0
       
        j=0
        SpawnOperator.mesh_name_mapping[f"Bmesh{str(SpawnOperator.iiii)}"].bm.from_mesh(OMeshTrail.data)
        
        print(F" Total verts {totalvertNum} Mode verts {numModVerts}")
        SpawnOperator.mesh_name_mapping[f"Bmesh{str(SpawnOperator.iiii)}"].bm.to_mesh(SpawnOperator.omeshTrail.data)
        SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(SpawnOperator.iiii)}"].data.update()
        print(F" Total verts {totalvertNum} Mode verts {numModVerts}")
        
        SpawnOperator.mesh_name_mapping[f"Bmesh{str(SpawnOperator.iiii)}"].bm.verts.ensure_lookup_table()
        
        
        bpy.ops.object.mode_set(mode='OBJECT')
        # print(f"{SpawnOperator.mesh_name_mapping["Empty"].location } {SpawnOperator.mesh_name_mapping["OtherMeshTrail"].location}")
        # print(f"{SpawnOperator.mesh_name_mapping["MeshTrail"].location} {SpawnOperator.mesh_name_mapping["OtherMeshTrail"].location}")
        # SpawnOperator.mesh_name_mapping["Empty"].location = SpawnOperator.mesh_name_mapping["OtherMeshTrail"].location
        # SpawnOperator.mesh_name_mapping["MeshTrail"].location = SpawnOperator.mesh_name_mapping["OtherMeshTrail"].location
        # print(f"{SpawnOperator.mesh_name_mapping["Empty"].location } {SpawnOperator.mesh_name_mapping["OtherMeshTrail"].location}")
        # print(f"{SpawnOperator.mesh_name_mapping["MeshTrail"].location} {SpawnOperator.mesh_name_mapping["OtherMeshTrail"].location}")
        

        
        
        
    def OtherCopyAndConvert(Empty):
        from .  HorseyTimeSpawnButton import SpawnOperator
        ob = Empty.copy()
        ob.data = Empty.data

        bpy.context.collection.objects.link(ob)
        #ob.data.convert(target='MESH')
        mesh = bpy.data.meshes.new_from_object(ob)
        new_obj = bpy.data.objects.new("OtherMeshTrail", mesh)
        
        SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(SpawnOperator.iiii)}"] = new_obj
        SpawnOperator.mesh_name_mapping[f"MeshTrail{str(SpawnOperator.iiii)}"]["OTrails"] = new_obj
        new_obj.matrix_world = ob.matrix_world
        
        ExtraFunc.SelectDelete(ob)
        bpy.context.collection.objects.link(new_obj)
        
        SpawnOperator.mesh_name_mapping[f"OtherMeshTrail{str(SpawnOperator.iiii)}"].select_set(True)
        

        #SpawnOperator.meshs.append(new_obj)
        #ob.location = SpawnOperator.locations[1]
        #ob.select_set(True)
        