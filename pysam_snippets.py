from pysam import VariantFile

# reading/writing BAMs
samfile = pysam.AlignmentFile("mybam.bam", "rb")

# reading/writing VCFs
bcf_in = VariantFile("mybcf.bcf")  
bcf_out = VariantFile('-', 'w', header=bcf_in.header)

for rec in bcf_in.fetch('chr1', 100000, 200000):
    bcf_out.write(rec)