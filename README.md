# DataStructuresAndAlgo
A repository for common Data Structures and Algorithms code base in python.
This template draws a lot of inspiration from [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/). Please read their awesome explanations!
# Getting Started
## Installing Dependencies and Packages
The following steps can be used to installing the dependencies on your machine and getting started with development:
1) Set up a Python 3 virtual environment using [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#) or [Virtualenv](https://virtualenv.pypa.io/en/latest/index.html). Read [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/#the-virtualenv-project) for details on how to get started with virtual environments and why you need them.
```commandline
$ conda create -n setup python=3.10 -y
```
2) Activate your virtual environment.
```
$ conda activate setup
```
3) Install the package.
```commandline
$ pip install .
```

## Directory Structure
A small description of each directory and subdirectory files in the project. This should be updated with every commit.
```
DataStructuresAndAlgo
├── Graphs     # The python module with Graph specific DSA scripts
│   ├── DisjointSet.py    # A script with an optimized class that encapsulates the methods for creating a disjoint set
│   ├── MinimumSpanningTree.py    # A script that contains most frequently used algorithms for finding the Minimum SPanning Tree
│   ├── ShortestPath.py   # A script that finds Single Source Shortest Path in a directed graph 
│   ├── TopologicalSort.py    # A script that performs Topological Sorting using Kahn's ALgorithm
│   ├── Traversal.py    # A script for performing Depth First and Breadth First Search in a graph
├── Heap     # The python module for building MinHeap and MaxHeap
│   ├── MaxHeap.py    # A script that allows building a max heap
│   └── MinHeap.py    # A script that allows building a min heap
├── Trie     # The python module for building Tries or Prefix Trees
│   └── Trie.py    # A script that allows building a trie/prefix tree
├── tests     # The python module for performing automated tests on various methods
│   └── tests.py    # Unit tests for methods in Traversal.py of Graphs module
├── pyproject.toml    # Script that installs setuptools build tools for easy installation of other dependencies using setup.cfg
├── README.md     # A guide to the repository
└── setup.cfg   # A script for proper installation of requirements and dependencies.
```
