__author__ = "Chris Varanese"
__version__ = "1.0"

import os
from BrawlCrate.NodeWrappers import *
from System.Windows.Forms import ToolStripMenuItem
from mawwwkLib import *

SCRIPT_NAME = "Export to ROA Anim"
VALID_GROUP_NAMES = ["AnmChr(NW4R)"]


## Start enable check functions
# Wrapper: BRRESWrapper
def enableCheckBRES(sender, event_args):
	node = BrawlAPI.SelectedNode
	sender.Enabled = (node and node.HasChildren)

	# Below code causes infinite loop, not sure why.

	# Enable node if it contains AnmChr(NW4R)
	# if node:
	# 	BrawlAPI.ShowMessage('Checked 2 ' + node.Name, "")
	# 	if node.HasChildren:
	# 		sender.Enabled = False
	# 		BrawlAPI.ShowMessage('Has children ' + node.Name, "")
	# 		for group in node.Children:
	# 			BrawlAPI.ShowMessage('Checking ' + group.Name, "")
	# 			if group.Name in VALID_GROUP_NAMES:
	# 				BrawlAPI.ShowMessage('WeWon ' + group.Name, "")
	# 				sender.Enabled = True
	# 				return
	# 	else: 
	# 		sender.Enabled = False
	# else:
	# 	sender.Enabled = False

## End enable check functions
## Start loader functions

# Base loader function (parent chr0 node)
def export_anim(sender, event_args):
	main(BrawlAPI.SelectedNode)

# Copy all keyframes from source_entry into a new entry in target_anim
def copy_entry(source_entry, target_anim):
	new_entry = target_anim.CreateEntry(source_entry.Name)
	for array_index in range(9):
		for frame_index in range(source_entry.Parent.FrameCount + 1):
			kf = source_entry.GetKeyframe(array_index, frame_index)
			if kf:
				new_kf = new_entry.SetKeyframe(array_index, frame_index, kf._value, True)
				new_kf._tangent = kf._tangent
	return new_entry

# Main function
def main(bresNode):
	# Select MDL0 for all exports
	file_filter = "MDL0 Model (*.mdl0)|*.mdl0|All files (*.*)|*.*"
	model_name = BrawlAPI.OpenFileDialog("Select the model for anim export", file_filter)
	if model_name == "":
		return
	model = NodeFactory.FromFile(None, model_name)
	for bone in getBones(model):
		if bone.Name == 'ThrowN':
			bone.Name = 'Grab_M'
			break

	os.makedirs("./animations_full", exist_ok=True)
	os.makedirs("./animations_no_trans", exist_ok=True)
	os.makedirs("./animations_no_x", exist_ok=True)

	for group in BrawlAPI.SelectedNode.Children:
		if group.Name in VALID_GROUP_NAMES:
			for chr0_node in group.Children:

				def make_anim():
					anim = CHR0Node()
					anim.Name = chr0_node.Name
					anim.FrameCount = chr0_node.FrameCount
					anim.Loop = chr0_node.Loop
					return anim

				anim_full     = make_anim()
				anim_no_trans = make_anim()
				anim_no_x     = make_anim()

				for bone in chr0_node.GetChildrenRecursive():
					entry_full = copy_entry(bone, anim_full)

					if bone.Name != 'TransN':
						entry_no_trans = copy_entry(bone, anim_no_trans)

					entry_no_x = copy_entry(bone, anim_no_x)
					if bone.Name == 'TransN':
						for i in range(anim_no_x.FrameCount + 1):
							entry_no_x.RemoveKeyframe(transZ, i)

					if bone.Name == 'ThrowN':
						entry_full.Name = 'Grab_M'
						entry_no_trans.Name = 'Grab_M'
						entry_no_x.Name = 'Grab_M'

				AnimFormat.Serialize(anim_full,     f"./animations_full/{chr0_node.Name}.anim",     model)
				AnimFormat.Serialize(anim_no_trans, f"./animations_no_trans/{chr0_node.Name}.anim", model)
				AnimFormat.Serialize(anim_no_x,     f"./animations_no_x/{chr0_node.Name}.anim",     model)
	return

## End loader functions
## Start context menu add

LONG_TEXT = "Strip Z translation from TransN and export all animations"
SHORT_TEXT = "Export all to anim..."

BrawlAPI.AddContextMenuItem(BRESWrapper, "", LONG_TEXT, enableCheckBRES, ToolStripMenuItem(SHORT_TEXT, None, export_anim))