# problem 1 - importing a module
# import using import module syntax
import calculateGC_module

# must use module.function when calling
# I can use ANY function from this module
gc = calculateGC_module.calculateGC('ATGC')
print(gc)

"""# explicitly import only certain functions from  my module
from calculateGC_module import calculateGC

# I can use imported functions without the module name
# but I can't use functions I didn't import
gc = calculateGC('ATGC')
print(gc)"""

# problem 2 - importing a package

"""# use from package.module import class syntax
# I only explicitly import the classes I want
from Sequences.Sequences import DNASequence, ProteinSequence
from Sequences.Fasta import FastaFile

fasta_file = '/home/kathryn/BIOL4292/Lab6/FIKK_kinases.fasta'

# make a FastaFile object
# I can use class names without a module
# but I can only use the classes I explicitly imported
fasta = FastaFile(fasta_file)
# the get_seq_record method yields, so I can use it in a for loop
for record in fasta.get_seq_record(DNASequence):
    # make a Protein Sequence record with the id and the translated sequence
    protein = ProteinSequence(record.id, record.translate_seq())
    # write this to a fasta file using our create_fasta function
    print(protein.make_fasta())"""

# import a module from a package and declare a namespace (...as namespace)
"""import Sequences.Sequences as Sequences
import Sequences.Fasta as Fasta

fasta_file = '/home/kathryn/BIOL4292/Lab6/FIKK_kinases.fasta'

# make a FastaFile object
# you must declare the namespace when using the class (namespace.class)
# you can use any classes in the imported module(s)
fasta = Fasta.FastaFile(fasta_file)
# the get_seq_record method yields, so I can use it in a for loop
for record in fasta.get_seq_record(Sequences.DNASequence):
    # make a Protein Sequence record with the id and the translated sequence
    protein = Sequences.ProteinSequence(record.id, record.translate_seq())
    # write this to a fasta file using our create_fasta function
    print(protein.make_fasta())"""

"""# from package import module
# I do not declare a namespace here 
# instead, the namespace is declared in the __init__.py file
# this is will not work if __init__.py is not configured correctly
from Sequences import Sequences
from Sequences import Fasta

fasta_file = '/home/kathryn/BIOL4292/Lab6/FIKK_kinases.fasta'

# make a FastaFile object
# I still need to use the namespace here
fasta = Fasta.FastaFile(fasta_file)
# the get_seq_record method yields, so I can use it in a for loop
for record in fasta.get_seq_record(Sequences.DNASequence):
    # make a Protein Sequence record with the id and the translated sequence
    protein = Sequences.ProteinSequence(record.id, record.translate_seq())
    # write this to a fasta file using our create_fasta function
    print(protein.make_fasta())"""