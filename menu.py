import nuke
import edgeNode

nuke.menu("Nuke").addCommand("utilities/edgeNode/jump to first node", "edgeNode.jump_to_edge_node('top')", "Ctrl+Shift+.")
nuke.menu("Nuke").addCommand("utilities/edgeNode/Jump to last mode", "edgeNode.jump_to_edge_node('bottom')", "Ctrl+.")
nuke.menu("Nuke").addCommand("utilities/edgeNode/view first node", "edgeNode.view_edge_node('top')", "Ctrl+Shift+,")
nuke.menu("Nuke").addCommand("utilities/edgeNode/view last node", "edgeNode.view_edge_node('bottom')", "Ctrl+,")
