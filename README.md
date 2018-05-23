# tulip-examples
Examples of discrete synthesis using the TuLiP toolbox

## Steps to set up TuLiP to run the examples

Create and activate a virtual env
  
    virtualenv -p python2.7 ~/.venvs/tulip
    source ~/.venvs/tulip/bin/activate
    pip install --upgrade pip
    pip install tulip  
    pip install jupyter matplotlib cvxopt

Clone this repo, browse to it, and start notebook server
  
    git clone git@github.com:pettni/tulip-examples.git
    cd tulip-examples
    jupyter-notebook

## Easy FTS

Example of synthesis in a small non-deterministic finite transition system with a recurrence objective.

## River Crossing

The [classical puzzle](https://en.wikipedia.org/wiki/River_crossing_puzzle) where a farmer needs to bring a fox, a chicken, grain, and himself across a river in a boat that can only carry himself and one object.

## Animal Herding

The single-agent example from the paper

Kress-Gazit, H., Fainekos, G. E., & Pappas, G. J. (2009). Temporal-logic-based reactive mission and motion planning. IEEE Transactions on Robotics, 25(6), 1370–1381. [DOI 10.1109/TRO.2009.2030225](https://doi.org/10.1109/TRO.2009.2030225)
