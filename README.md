PETs
====
The Predictor of Protein-Protein interaction sites based on Extremely-randomized Trees(PETs)


Table of Contents
=================

- Introduction
- Installation
- Quick Start
- Design Description
- Additional Information

Introduction
============

PETs is a Predictor of Protein-Protein interaction sites based on Extremely-randomized Trees. In PETs, a new sampling strategy is proposed to ensure and improve the stability of predictor, features are used to divide training dataset into sub datasets, these datasets would be clustered through k-means, and the samples could be selected based the distance. Through this kind of sampling, samples which have different types of significant features could be selected uniformly. The performance shows that PETs has better results and keeps a good stability.

Installation
============
(Note: If the github version is not feasible, the dropbox version can be available at  https://www.dropbox.com/sh/44d321ghh0e9l3y/AABpRHlLQzajaFxlnshn3sKqa?dl=0)
PETs requires:
- Python (>= 2.6 or >= 3.3)------https://www.python.org/downloads/
- Scikit-learn (>= 0.15)-----------http://scikit-learn.org/stable/install.html
- NumPy (>= 1.6.1)
- SciPy (>= 0.9)
- IPythonNotebook----------------http://ipython.org/install.html

Python is a programming language suitable for rapid development, and it could be available at https://www.python.org/downloads/.

Scikit-learn is a simple and efficient tools for data mining and data analysis, and it could be available at http://scikit-learn.org/stable/install.html. The installation of Scikit-learn, NumPy, and SciPy is described in the website completely.

IPythonNotebook is a browser-based notebook with support for code, text, mathematical expressions, inline plots and other rich media, the complete installation manual could be available at http://ipython.org/install.html. IPythonNotebook is excellent in storing the history running result, embedded in the website, and many other characteristics.
  
Quick Start
===========

Step 1: Open 'PETs_ez2use.ipynb' using IPythonNotebook, and search for the area which is described in the following in tail of code:

#######################################
def main():

    definition = 'ASA_Change'
#######################################

Modify the definition of PPIs which you require.

Step 2: Enter the folder 'YourDatasetHere' in the root of our project.
- Folder 'dataset': 'myDataset' is stored FASTA format of protein, please be sure the name of file must be 'myDataset', and name of protein must be like '1ak4A' (the name uses lower words and the chain uses upper words).
- Folder 'PRSA': This feature could be available at http://scratch.proteomics.ics.uci.edu/, it has a off-line version at http://scratch.proteomics.ics.uci.edu/explanation.html#ACCpro20. Please be sure the name of file is 'myDataset.out.acc20'.
- Folder 'PSA': This feature could be available at http://lee.kias.re.kr/~newton/sann/, and please be sure that the name of file is like '1AK4A.prsa' (the name and chain use both upper words).
- Folder 'PSS': This feature could be also available at http://scratch.proteomics.ics.uci.edu/, and its off-line version could be obtained at http://scratch.proteomics.ics.uci.edu/explanation.html#SSpro. The rule of name is the same as 'PRSA' but the suffix is '.out.ss'.
- Folder 'PSSM': This feature is available at http://blast.ncbi.nlm.nih.gov/Blast.cgi, I think this the only one which I don't need to explain in details. But make sure that the name of file is like '1ak4_A' (the name uses lower words and the chain uses upper words, and '_' is used to divide).

Step 3: Just run 'PETs_ez2use', and a complete report could be available in folder 'result' for each protein.

Tips: These folders are in 'YourDatasetHere', DO NOT MODIFY THE FOLDERS IN THE ROOT OF PROJECT!

Design Description
==============

- PETs_final.ipynb

This is the code which is doing loading, sampling, training, testing from starting to finishing. It contains our sampling strategy completely.
- PETs_ourDatasets.ipynb

This is the code which is loading the model directly to test Dtestset72 and PDBtestset164.
- PETs_ez2use.ipynb

This is the code for 'easy to use'.
- dataset/PRSA/PSA/PSS/PSSM/subDataset

The storage of datasets and features used in our experiments.
- ETsModel

The storage of model files in different definition of interface.
- YourDatasetHere

The storage of datasets and features for PETs_ez2use.ipynb.  

Additional Information
=================

Feel free to give us a  email if you have questions or concerns.

E-mail: ben.binxia@gmail.com






