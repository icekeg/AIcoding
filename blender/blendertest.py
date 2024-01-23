import bpy
import json


with open("D:/AI/luciddreamer/cameras/headbanging.json",'r',encoding='utf-8') as f :
    uu = json.load(f)

ob = bpy.context.active_object

cframe = 1
for i in uu['frames']:
    ob.matrix_world = (tuple(i["transform_matrix"][0]), tuple(i["transform_matrix"][1]), tuple(i["transform_matrix"][2]), (1,0,0,1))
    ob.keyframe_insert("location",frame = cframe)
    ob.keyframe_insert("rotation_euler",frame = cframe)
    cframe += 1