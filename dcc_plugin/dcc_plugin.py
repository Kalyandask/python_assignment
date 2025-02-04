import maya.cmds as cmds
import requests

# Function to get selected object's transform data
def get_transform_data():
    selection = cmds.ls(selection=True)
    if not selection:
        print("No object selected!")
        return None
    obj = selection[0]
    position = cmds.xform(obj, query=True, translation=True, worldSpace=True)
    rotation = cmds.xform(obj, query=True, rotation=True, worldSpace=True)
    scale = cmds.xform(obj, query=True, scale=True)
    return {
        "object": obj,
        "position": position,
        "rotation": rotation,
        "scale": scale
    }

# Function to send data to the server
def send_to_server(endpoint):
    data = get_transform_data()
    if not data:
        return
    url = f"http://127.0.0.1:5000/{endpoint}"
    response = requests.post(url, json=data)
    print(f"Server Response: {response.status_code}, {response.text}")

# Create a simple UI
def create_ui():
    window_name = "dcc_plugin_window"
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    cmds.window(window_name, title="DCC Plugin", widthHeight=(300, 200))
    cmds.columnLayout(adjustableColumn=True)

    cmds.button(label="Select Object", command=lambda x: cmds.select(clear=True))
    cmds.button(label="Send Transform Data", command=lambda x: send_to_server("transform"))
    cmds.button(label="Send Translation Data", command=lambda x: send_to_server("translation"))
    cmds.button(label="Send Rotation Data", command=lambda x: send_to_server("rotation"))
    cmds.button(label="Send Scale Data", command=lambda x: send_to_server("scale"))

    cmds.showWindow()

# Run the UI
create_ui()