

import sys


# Load a fasta file
sequences = []  

#
# Your code here
#

# Calculate the total number of different nucleotides
total_diff = 0

#
# Your code here
#

# Calculate the total number of segregating sites
total_seg_sites = 0

#
# Your code here
#

# Calculate pi and d
num_sequences = len(sequences)
len_sequence = len(sequences[0])
combination = num_sequences*(num_sequences-1)/2
pi = total_diff/combination/len_sequence
x = sum([1/i for i in range(1, num_sequences)])
s = total_seg_sites/len_sequence
d = pi - (s/x)

print("Total differences =", total_diff)
print("nC2 =", combination)
print("Lenght of sequence =", len_sequence)
print("Nucleotide diversity pi =", pi)
print("Pair-wise difference PI =", PI)
print("Number of SNP sites (total segregating sites) S =", total_seg_sites)
print("Frequency of SNP sites s = S/sequence_length =", s)
print("sum_{i=1}^{n-1}(1/i) =", sum_)
print("estimated pi = s/sum(1/i) =", estimated_pi)

#
# Your code here
#


print("d = pi - estimated_pi =", d)
print("Tajima's D=", td)
