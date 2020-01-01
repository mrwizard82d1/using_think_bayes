"""Solution to the Euro problem; that is, do the observed results give evidence of bias in a coin?"""

import fractions

from thinkbayes import Suite
import thinkplot


class Euro(Suite):
    """Models a solution to the Euro problem."""

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of observing data given hypothesis.

        Args:
            data(string): The observed data.
                This solution assumes two valid values for the data: 'H' or 'T'.
            hypothesis(int): A representation of the hypothesis assumed to be true.
        """

        if data == 'H':
            return fractions.Fraction(hypothesis, 100)
        else:
            return 1 - fractions.Fraction(hypothesis, 100)


def main():
    suite = Euro(range(0, 100 + 1))
    suite.name = 'uniform'

    # Assume the actual order of heads and tails does not matter
    dataset = 'H' * 140 + 'T' * 110
    for datum in dataset:
        suite.update(datum)

    print(f'Mean={suite.mean()}')

    thinkplot.preplot(1)
    thinkplot.plot_pmf(suite)
    thinkplot.save(root='euro', xlabel='Probability of heads', ylabel='Probability')


if __name__ == '__main__':
    main()
