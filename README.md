# SupAgro Modelling Course 2021

Material for the SupAgro Modelling Course

## Install

### Conda Installation

[Conda](https://docs.conda.io) is a package manager that can be installed on Linux, Windows, and Mac.
If you have not yet installed conda on your computer, follow these instructions:

[Conda Installation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html). Follow instructions for Miniconda.

[Conda Download](https://docs.conda.io/en/latest/miniconda.html). 

#### Windows, Linux, Mac

Create an environment named *openalea*:
Launch a console (See Anaconda Prompt in Start menu on windows)
    
    conda create -n training -c openalea3 -c conda-forge openalea.plantgl openalea.lpy alinea.caribu alinea.astk

Activate the *openalea* environment:

    conda activate training
    pip install matplotlib pandas

