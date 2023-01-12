from pyboolnet.repository import get_primes
from pyboolnet.state_transition_graphs import primes2stg
from pyboolnet.attractors import compute_attractors_tarjan, compute_attractors, find_attractor_state_by_randomwalk_and_ctl
from pyboolnet.file_exchange import bnet2primes


if __name__ == "__main__":
    # attractor computation with Tarjan
    repre = """
    v1, !v3
    v2, !v1
    v3, !v2
    """

    primes = get_primes("xiao_wnt5a")
    # primes = bnet2primes(repre)
    

    # stg = primes2stg(primes, "asynchronous")
    stg = primes2stg(primes, "asynchronous")
    steady, cyclic = compute_attractors_tarjan(stg)
    print("steady", steady)
    print("cyclic", cyclic)

    # random walk attractor detection

    state = find_attractor_state_by_randomwalk_and_ctl(primes, "synchronous")
    print("+++++++++++++++++++", state)

    # model checking based attractor detection
    print("blabla")
    attrs = compute_attractors(primes, "synchronous", fname_json="attrs.json")

    print("----------------------------", attrs["is_complete"])
    for x in attrs["attractors"]:
        print(x["is_steady"])
        print(x["state"]["str"])