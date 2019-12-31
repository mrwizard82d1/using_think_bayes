"""First implementation of the locomotive problem."""

from dice import Dice
import thinkplot


class Train(Dice):
    """Models the first implementation of the locomotive problem."""


def main():
    suite = Train(range(1, 1000 + 1))
    suite.update(60)
    print(suite.mean())

    thinkplot.preplot(1)
    thinkplot.plot_pmf(suite)
    thinkplot.save(root='train1', xlabel='Number of trains', ylabel='Probability', formats=['png'])


if __name__ == '__main__':
    main()

