import pysam

# reading/writing BAMs
samfile = pysam.AlignmentFile("myfile.bam", "rb")

# reading/writing VCFs
bcf_in = VariantFile("mybcf.bcf")  
bcf_out = VariantFile('-', 'w', header=bcf_in.header)

for rec in bcf_in.fetch('chr1', 100000, 200000):
    bcf_out.write(rec)

bcf_out.close()

# equivalent to `samtools sort -o output.bam myfile.bam`
pysam.sort("-o", "output.bam", "myfile.bam")
