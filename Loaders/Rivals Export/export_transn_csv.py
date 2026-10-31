__author__ = "Chris Varanese"
__version__ = "1.0"

import csv
from BrawlCrate.NodeWrappers import *
from System.Windows.Forms import ToolStripMenuItem
from mawwwkLib import *

SCRIPT_NAME = "Export TransN Keyframes to CSV"
VALID_GROUP_NAMES = ["AnmChr(NW4R)"]


## Start enable check functions
# Wrapper: BRRESWrapper
def enableCheckBRES(sender, event_args):
	node = BrawlAPI.SelectedNode
	sender.Enabled = (node and node.HasChildren)

## End enable check functions
## Start loader functions

# Base loader function
def export_transn_csv(sender, event_args):
	main(BrawlAPI.SelectedNode)

# Main function
def main(bresNode):
	output_path = "./transn_keyframes.csv"

	with open(output_path, 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['animation', 'frame', 'x', 'y', 'z'])

		for group in BrawlAPI.SelectedNode.Children:
			if group.Name in VALID_GROUP_NAMES:
				for chr0_node in group.Children:
					for bone in chr0_node.GetChildrenRecursive():
						if bone.Name != 'TransN':
							continue
						for frame_index in range(chr0_node.FrameCount + 1):
							kf_x = bone.GetKeyframe(transX, frame_index)
							kf_y = bone.GetKeyframe(transY, frame_index)
							kf_z = bone.GetKeyframe(transZ, frame_index)
							if kf_x or kf_y or kf_z:
								x = kf_x._value if kf_x else bone.GetFrameValue(transX, frame_index)
								y = kf_y._value if kf_y else bone.GetFrameValue(transY, frame_index)
								z = kf_z._value if kf_z else bone.GetFrameValue(transZ, frame_index)
								writer.writerow([chr0_node.Name, frame_index, x, y, z])

	BrawlAPI.ShowMessage(f"Exported to {output_path}", SCRIPT_NAME)

## End loader functions
## Start context menu add

LONG_TEXT = "Export TransN keyframe data to CSV"
SHORT_TEXT = "Export TransN to CSV..."

BrawlAPI.AddContextMenuItem(BRESWrapper, "", LONG_TEXT, enableCheckBRES, ToolStripMenuItem(SHORT_TEXT, None, export_transn_csv))
