# create a converter from a chainfile
from liftover import ChainFile
converter = ChainFile('/home/ptv/hg19ToHg38.over.chain.gz', 'hg19', 'hg38')
converter[chrom][pos]

# using the built-in data
from liftover import get_lifter

converter = get_lifter('hg19', 'hg38')
chrom = '1'
pos = 103786442
converter[chrom][pos]

# synonyms for the lift call
converter.convert_coordinate(chrom, pos)
converter.query(chrom, pos)

