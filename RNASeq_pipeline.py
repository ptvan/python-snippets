### using bioPython

from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein

# handling sequences
my_dna = Seq("AGTACACTGGTC", generic_dna)
my_dna.complement()
my_rna = my_dna.transcribe()

# will throw errors if there aren't complete codons
my_protein = my_rna.translate()