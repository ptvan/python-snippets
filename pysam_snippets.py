from pysam import VariantFile

# reading/writing VCFs
bcf_in = VariantFile("myfile.bcf")  
bcf_out = VariantFile('-', 'w', header=bcf_in.header)

for rec in bcf_in.fetch('chr1', 100000, 200000):
    bcf_out.write(rec)