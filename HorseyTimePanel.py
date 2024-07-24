import bpy

from bpy.types import Panel
from . HorseyTimeSpawnButton import SpawnOperator
from . HorseyTimeSettings import MyPropertyGroup

class HorseyTime_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "BJiggle Vs .001"
    bl_category = "HorseyTime Util"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        #column.prop(obj.my_custom_props, "NumOfCirc", text="Number of slowdowns")
        row = layout.row()
        col = row.column()
        row.operator(SpawnOperator.bl_idname,text="Testing")
        row = layout.row()
        #row.prop(obj.my_prop_grp, "nameOfEmpty", text="test")
        row.label(text="")
        
        
        