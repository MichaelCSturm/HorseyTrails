import bpy

class MyPropertyGroup(bpy.types.PropertyGroup):
    nameOfEmpty: bpy.props.StringProperty(name="String Value")