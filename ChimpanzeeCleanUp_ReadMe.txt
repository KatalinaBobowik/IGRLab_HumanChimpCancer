Created on 15.01.17 by Katalina Bobowik

Objective: the purpose of this script is to clean up the PanTro5 chimpanzee genome downloaded from UCSC (http://hgdownload.cse.ucsc.edu/goldenPath/panTro5/bigZips/ - panTro5.fa.gz), i.e., cut out the unnecessary contigs and only keep chromosomes 1-22 (including 2A and 2B), X, Y, and the mitochondrial DNA.

The wanted file was created using a blank text file and populating it line by line with the desired chromosomes (as stated above). This was then “grabbed’ from the fasta_file and the data was written into the empty result_file fasta document.