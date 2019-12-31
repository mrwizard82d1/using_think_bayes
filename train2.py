"""Solution to locomotive problem with additional data."""

from dice import Dice
import thinkplot


class Train(Dice):
    """Solution to the locomotive problem with three observed locomotives."""


def make_posterior(high, dataset):
    suite = Train(range(1, high + 1))
    suite.name = high

    for data in dataset:
        suite.update(data)

    thinkplot.plot_pmf(suite)
    return suite


def main():
    dataset = [60, 30, 90]
    for high in [500, 1000, 2000]:
        suite = make_posterior(high, dataset)
        print(high, suite.mean())

    thinkplot.save(root='train2', xlabel='Number of trains', ylabel='Probability', formats=['png'])


if __name__ == '__main__':
    main()

