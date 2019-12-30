"""A solution to the dice problem from chapter 3."""

import fractions

from thinkbayes import Suite


class Dice(Suite):
    """Models the dice problem from chapter 3."""

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of data given hypothesis.

        Args:
            data(object): The observed datum.
            hypothesis(object): The hypothesis assumed to be true.
        """

        if hypothesis < data:
            # If the actual value rolled is greater than the hypothesis (maximum number of pips),
            # The likelihood of that hypothesis **must** be zero.
            return 0
        else:
            # Otherwise, it is uniformly distributed over all the possible pips.
            return fractions.Fraction(1, hypothesis)


def main():
    suite = Dice([4, 6, 8, 12, 20])
    suite.update(6)
    print('After seeing 6')
    suite.print()

    for roll in [6, 8, 7, 7, 5, 4]:
        suite.update(roll)

    print('\nAfter seeing [6, 8, 7, 7, 5, 4]')
    suite.print()


if __name__ == '__main__':
    main()
