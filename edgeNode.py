import nuke
import nukescripts

'''
the functionality of this module is to jump to the first or last node 
and to connect the viewer with the first/last node
'''

def get_edge_node(which):
    edge_node = None
    for node in nuke.allNodes():
        if node.Class() != "Viewer":
            if edge_node is None:
                edge_node = node
            if which == "top":
                if node.ypos() < edge_node.ypos():
                    edge_node = node
            if which == "bottom":
                if node.ypos() > edge_node.ypos():
                    edge_node = node
    return edge_node





def view_edge_node(which):
    # print("view node: {}".format(get_edge_node(which).name()))
    viewer_port = 8
    edge_node = get_edge_node(which)
    sel = nuke.selectedNodes()
    if edge_node is None:
        return
    # several steps to connect viewer to edge_node:

    nukescripts.clear_selection_recursive() # now everything are deselected
    edge_node.setSelected(True)
    # connect the viewer to currently selected node we can do:
    nukescripts.connect_selected_to_viewer(viewer_port)
    #deselect our edge_node
    edge_node.setSelected(False)
    #we need to reselected nodes that we selected before running this method.
    # as we save them here as a list we can iterate through them one by one
    # and set the nodes to selected.

    for node in sel:
        node.setSelected(True)


    for node in nuke.allNodes("Viewer"):
        node.setSelected(False)



def jump_to_edge_node(which):

     # print("jump to edge node: {}".format(get_edge_node(which).name()))
    edge_node = get_edge_node(which)
    if edge_node is None:
        return
    nuke.zoom(1, [float(edge_node.xpos()), float(edge_node.ypos())])


