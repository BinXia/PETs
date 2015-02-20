import os

filename = '../../blast/PDBtestset164/'
nr = './nr'

for protein in os.listdir(filename):
	if protein[0] == '.':
		continue;
	os.system('../../blast/ncbi-blast-2.2.29+/bin/psiblast -query {1} -num_iterations 3 -db {2} -inclusion_ethresh 0.001 -out_ascii_pssm ./PSSM/{3}'.format(filename+protein,nr,protein[10:]));