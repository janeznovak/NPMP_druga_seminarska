

import pyboolnet.state_space
from pyboolnet.file_exchange import bnet2primes
from pyboolnet.interaction_graphs import primes2igraph, igraph2image, local_igraph_of_state, add_style_interactionsigns
from pyboolnet.repository import get_primes
from pyboolnet.state_transition_graphs import create_stg_image

if __name__ == "__main__":
    bnet = """
    v1,    !v1
    v2,    1
    v3,    v2 & (!v1 | v3)
    """
    represilator = """
    v1, !v3
    v2, !v1
    v3, !v2
    """
    primes = bnet2primes(represilator)
    # primes = get_primes("faure_cellcycle")

    igraph = primes2igraph(primes)
    print("igraph", igraph)
    igraph2image(igraph, "interaction_graph.pdf")
    # primes = bnet2primes("test.bnet")
    print("here")
    create_stg_image(primes, update="asynchronous", fname_image="py_represilator_interaction.pdf")
    create_stg_image(primes, update="asynchronous", fname_image="py_represilator.cycles.pdf", styles=["sccs"])

    # advances drawing

    igraph = primes2igraph(primes)

    for x in igraph.nodes:
        print("x", x)
        if "GF" in x:
            print("in gf")
            igraph.nodes[x]["shape"] = "square"
            igraph.nodes[x]["fillcolor"] = "lightblue"

    igraph2image(igraph, "igraph3.pdf")

    # local interaction graphs

    state = pyboolnet.state_space.random_state(primes)
    local_igraph = local_igraph_of_state(primes, state)
    add_style_interactionsigns(local_igraph)
    igraph2image(local_igraph, "py_represilator_shema.pdf")