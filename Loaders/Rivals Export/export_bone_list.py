__author__ = "Chris Varanese"
__version__ = "1.0"

from BrawlCrate.NodeWrappers import *
from System.Windows.Forms import ToolStripMenuItem
from mawwwkLib import *

SCRIPT_NAME = "Export all bones"

## Start enable check functions
# Wrapper: CHR0Wrapper, VIS0Wrapper
def EnableCheckMDL0(sender, event_args):
    node = BrawlAPI.SelectedNode
    sender.Enabled = (node and node.HasChildren)

## End enable check functions
## Start of main script

def extract_bones(sender, event_args):
    # Get parent brres
    selNode = BrawlAPI.SelectedNode
    allBoneNames = []
    
    bonesGroup = selNode.FindChild("Bones")
    if not bonesGroup:
        BrawlAPI.ShowWarning("No bones found.", SCRIPT_NAME)
        
    for bone in bonesGroup.GetChildrenRecursive():
        if bone.Parent:
            allBoneNames.append((bone.Name, bone.Parent.Name))
        else: 
            allBoneNames.append((bone.Name, None))

    file_name = "./bones.csv"
    with open(file_name, "w") as f:
        f.write(f"index, bone, parent\n") 
        for idx, bone_data in enumerate(allBoneNames):
            f.write(f"{idx}, {bone_data[0]}, {bone_data[1]}\n") 
    
    BrawlAPI.ShowMessage(f'Wrote bones to {file_name}', SCRIPT_NAME)

LONG_TEXT = "Extract all bones and indices to a file"
SHORT_TEXT = "Extract Bones"

BrawlAPI.AddContextMenuItem(MDL0Wrapper, "", LONG_TEXT, EnableCheckMDL0, ToolStripMenuItem(SHORT_TEXT, None, extract_bones))