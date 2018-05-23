# tulip-examples
Examples of discrete synthesis using the TuLiP toolbox

## Steps to set up TuLiP to run the examples

This assumes that Python 2.7 is installed on the system, and that the `virtualenv` package is installed. Create and activate a virtual environment
  
    virtualenv -p python2.7 ~/.venvs/tulip
    source ~/.venvs/tulip/bin/activate # run this every time you want to work on the project

Make sure that `pip` is up-to-date (if required install a [fresh version](https://pip.pypa.io/en/stable/installing/)) and use it to install `tulip`, `jupyter`, `matplotlib` and `cvxopt`.

    pip install --upgrade pip
    pip install tulip  
    pip install jupyter matplotlib cvxopt

For TuLiP plotting, [Graphviz](http://graphviz.org/download/) is required with the Python interface `pydot`. Install Graphviz using your preferred method (`sudo apt install graphviz` (Debian/Ubuntu), `brew install graphviz` (MacOS), or manually from the homepage), and install `pydot` with `pip`:

    pip install pydot


Clone this repo, browse to it, and start notebook server
  
    git clone https://github.com/pettni/tulip-examples.git
    cd tulip-examples
    jupyter-notebook



## Easy FTS

Example of synthesis in a small non-deterministic finite transition system with a recurrence objective.

## River Crossing

The [classical puzzle](https://en.wikipedia.org/wiki/River_crossing_puzzle) where a farmer needs to bring a fox, a chicken, grain, and himself across a river in a boat that can only carry himself and one object.

## Animal Herding

The single-agent example from the paper

Kress-Gazit, H., Fainekos, G. E., & Pappas, G. J. (2009). Temporal-logic-based reactive mission and motion planning. IEEE Transactions on Robotics, 25(6), 1370–1381. [DOI 10.1109/TRO.2009.2030225](https://doi.org/10.1109/TRO.2009.2030225)
