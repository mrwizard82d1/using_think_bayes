"""A solution to the locomotive problem assuing a power law distribution of locomotives."""


import math

import thinkplot

from dice import Dice


class Train(Dice):
    """Models a solution to the locomotive problem assuming a uniform distribution of locomotives."""


class Train2(Dice):
    """Models a solution to the locomotive problem assuming a power law distribution of locomotives."""

    def __init__(self, hypotheses, alpha=1.0):
        super().__init__()
        for hypothesis in hypotheses:
            self.set(hypothesis, math.pow(hypothesis, (- alpha)))
        self.normalize()


def make_posterior(high, dataset, constructor):
    """Calculate the posterior distribution of the suite built by constructor with parameter high.

    Args:
        high(int): The largest hypothesis in the suite.
        dataset(iterator): The observed data.
        constructor(function): The function used to construct the suite.
    """

    suite = constructor(range(1, high + 1))
    suite.name = high
    for datum in dataset:
        suite.update(datum)

    return suite


def compare_priors():
    """Compares the posteriors resulting from different priors."""
    dataset = [60]
    high = 1000

    thinkplot.clear_figures()
    thinkplot.preplot(2)

    constructors = [Train, Train2]
    labels = ['uniform', 'power law']

    for constructor, label in zip(constructors, labels):
        suite = make_posterior(high, dataset, constructor)
        suite.name = label
        thinkplot.plot_pmf(suite)

    thinkplot.save(root='train4', xlabel='Number of trains', ylabel='Probability', formats=['png'])


def main():
    compare_priors()


if __name__ == '__main__':
    main()
