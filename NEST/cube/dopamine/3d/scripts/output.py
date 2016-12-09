import nest
import nest.topology as tp

txt_result_path = ""    # path for txt results


def print_connections(f):
    f.write('edgedef> node, node2')
    for conn in nest.GetConnections():
        f.write("%d, %d\n" % (conn[0], conn[1]))


def print_gdf(f):
    f.write("nodedef> label\n")
    for node in nest.GetNodes((0,))[0]:
        f.write("%d\n" % node)

    print_connections(f)