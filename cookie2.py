"""A class to solve the cookie problem more generically."""

import fractions

from thinkbayes import Pmf


class Cookie(Pmf):
    """More general solution to the cookie problem."""

    def __init__(self, hypotheses, mixtures):
        """Construct an instance from a set of hypotheses.

        Args:
            hypotheses (iterator): The sequence of hypotheses for this instance.

        Attributes:
            mixtures (dict): A mapping from hypotheses to cookie mixtures.
        """
        super().__init__()

        self.mixtures = mixtures
        for hypothesis in hypotheses:
            self.set(hypothesis, 1)

        self.normalize()

    def update(self, data):
        """Updates the prior probabilities based on the data.

        Args:
            data (object): The data observed to calculate the posterior probability mass.
        """

        for hypothesis in self.values():
            likelihood = self.likelihood(hypothesis, data)
            self.multiply(hypothesis, likelihood)

        self.normalize()

    def likelihood(self, hypothesis, data):
        cookie_mixture = self.mixtures[hypothesis]
        result = cookie_mixture[data]
        return result


def main():

    cookie_mixtures = {
        'Bowl 1': dict(vanilla=fractions.Fraction(3, 4),
                       chocolate=fractions.Fraction(1, 2)),
        'Bowl 2': dict(vanilla=fractions.Fraction(1, 2),
                       chocolate=fractions.Fraction(1, 2))
    }
    cookie_hypotheses = cookie_mixtures.keys()

    pmf = Cookie(cookie_hypotheses, cookie_mixtures)

    # Updating with single datum
    pmf.update('vanilla')

    # Updating with a data stet
    # for data in ['vanilla', 'chocolate', 'vanilla']:
    #     pmf.update(data)

    # Print the posterior probabilities
    for cookie_hypothesis, probability in pmf.items():
        print(cookie_hypothesis, probability)


if __name__ == '__main__':
    main()
