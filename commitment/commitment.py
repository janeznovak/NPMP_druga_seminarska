from pyboolnet.attractors import compute_attractors
from pyboolnet.phenotypes import phenotype_diagram2image, compute_phenotype_diagram, create_phenotypes_piechart
from pyboolnet.repository import get_primes
from pyboolnet.file_exchange import bnet2primes

if __name__ == "__main__":
    # compute the commitment diagram
    repre = """
    v1, !v3
    v2, !v1
    v3, !v2
    """

    primes = get_primes("raf")
    # primes_repre = bnet2primes(repre)
    attractors = compute_attractors(primes, "asynchronous")
    diagram = compute_phenotype_diagram(attractors)
    phenotype_diagram2image(diagram, "commitment_diagram.pdf")

    # compute commitment pie chart

    create_phenotypes_piechart(diagram, "commitment_piechart.pdf")