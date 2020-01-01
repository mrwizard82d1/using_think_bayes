"""Solution to the Euro problem; that is, do the observed results give evidence of bias in a coin?"""

import fractions

import thinkbayes
import thinkplot


class Euro(thinkbayes.Suite):
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

    summarize(suite)

    thinkplot.preplot(1)
    thinkplot.plot_pmf(suite)
    thinkplot.save(root='euro', xlabel='Probability of heads', ylabel='Probability')


def summarize(suite):
    """Summarize the suite using different point values.

    Args:
          suite(Suite): The Suite to summarize.
    """
    print(f'Summary of suite, {suite.name}')
    print(f'  MLE (Most Likely Estimate)={suite.maximum_likelihood()}')
    print(f'  Mean={int(suite.mean())}')

    print(f'  5th percentile={thinkbayes.percentile(suite, 5)}')
    print(f'  Median={thinkbayes.percentile(suite, 50)}')
    print(f'  95th percentile={thinkbayes.percentile(suite, 95)}')

    print(f'  Credible interval={suite.credible_interval()}')


if __name__ == '__main__':
    main()
