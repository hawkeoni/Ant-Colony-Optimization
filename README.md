# Ant Colony Optimization (ACO)

Here is an ACO solution to travelling salesman problem. 
The code implements basic and maxmin ant colony 
algorithm.
To generate a graph use `Generator.py` according to usage.
```
usage: Generator.py [-h] [--size SIZE] [--file FILE]

Graph generator

optional arguments:
  -h, --help   show this help message and exit
  --size SIZE  Graph size
  --file FILE  Serialized graph filename
```
It creates a complete graph serialized into and xml 
file. The encoding is highly impracticable and is here only to 
satisfy requirements of the task from `CMC-2018-Reliability` Course.

To generate a random complete graph and find shortest Hamiltonian path use 
`main.py`, which can also be used with xml file created with the help of `Generator.py`.

```
usage: main.py [-h] [--size SIZE] [--ants ANTS] [--tactics TACTICS]
               [--vaporize VAPORIZE] [--iter ITER] [--seed SEED] [--file FILE]

Ant Colony TS optimization. 

optional arguments:
  -h, --help           show this help message and exit
  --size SIZE          TS graph size
  --ants ANTS          Amount of ants
  --tactics TACTICS    Tactics (default is simple, can be maxmin)
  --vaporize VAPORIZE  Vaporize rate
  --iter ITER          Iterations
  --seed SEED          Iterations
  --file FILE          Serialized graph in xml format
```
