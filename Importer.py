import bpy
import os


FILEPATH_ = "C:\\Users\\yoshioca\\Documents\\Rhino6_Export_FBX\\Models\\"

for i in range(len(os.listdir(FILEPATH_))):
    path = FILEPATH_ + str(i) + ".fbx"
    print(path)
    ### Import FBX
    bpy.ops.import_scene.fbx(filepath = path)
