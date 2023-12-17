from pysam import VariantFile
import numpy as np
from sklearn import decomposition
import pandas as pd

vcf_filename = "1.176558700-176563472.ALL.chr1.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz"
panel_filename = "phase1_integrated_calls.20101123.ALL.panel"

genotypes = []
samples = []
variant_ids = []

# List of specific variant IDs you're interested in
# target_variants = []  # INSERT with the measle susceptible variant IDs here ['rs1', 'rs2', etc.]


with VariantFile(vcf_filename) as vcf_reader:
    counter = 0
    for record in vcf_reader:
        alleles = [record.samples[x].allele_indices for x in record.samples]
        samples = [sample for sample in record.samples]
        genotypes.append(alleles)
        variant_ids.append(record.id)

        # if record.id in target_variants:
        #     alleles = [record.samples[x].allele_indices for x in record.samples]
        #     samples = [sample for sample in record.samples]
        #     genotypes.append(alleles)
        #     variant_ids.append(record.id)
        
        # counter += 1
        # if counter % 100 == 0:
        #     alleles = [record.samples[x].allele_indices for x in record.samples]
        #     samples = [sample for sample in record.samples]
        #     genotypes.append(alleles)
        #     variant_ids.append(record.id)
        # if counter % 4943 == 0:
        #     print(counter)
        #     print(f'{round(100 * counter / 494328)}%')

with open(panel_filename) as panel_file:
    labels = {}  # {sample_id: population_code}
    for line in panel_file:
        line = line.strip().split('\t')
        labels[line[0]] = line[1]


print(variant_ids)
genotypes = np.array(genotypes)
print(genotypes.shape)

matrix = np.count_nonzero(genotypes, axis=2)

matrix = matrix.T
print(matrix.shape)

pca = decomposition.PCA(n_components=2)
pca.fit(matrix)
print(pca.singular_values_)
to_plot = pca.transform(matrix)
print(to_plot.shape)

df = pd.DataFrame(matrix, columns=variant_ids, index=samples)
df['Population code'] = df.index.map(labels)
df.to_csv("matrix_1_1.csv")