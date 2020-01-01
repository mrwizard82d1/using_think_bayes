"""Solving the cookie problem - but I eat every cookie drawn!

This file implements a solution to exercise 2-1.
"""

import fractions

from thinkbayes import Suite


class Bowl:
    """Models a bowl of cookies that is a mixture of vanilla and chocolate cookies."""

    def __init__(self, vanilla, chocolate):
        """Constructs a bowl containing vanilla and chocolate cookies.

        Args:
            vanilla(int): The number of vanilla cookies initially in the bowl.
            chocolate(int): The number of chocolate cookies initially in the bowl.
        """
        super().__init__()
        self._mixture = {'vanilla': vanilla, 'chocolate': chocolate}

    def decrement(self, cookie):
        """Decrement the number of cookie(s) in this bowl.

        Args:
            cookie(string): The cookie whose number I am to decrement.
        """
        self._mixture[cookie] -= 1

    def fraction_of(self, cookie):
        """Calculate the fraction of cookie in this bowl.

        Args:
            cookie(string): The cookie whose fraction is sought.
        """
        return fractions.Fraction(self._mixture[cookie], sum(self._mixture.values()))


class Cookie(Suite):
    """Models the cookie problem - but I eat the cookies!"""

    def __init__(self, hypotheses, bowls):
        """Construct an instance from hypotheses and corresponding bowls of cookies.

        Args:
            hypotheses(iterator): The hypotheses to test.
                Each hypothesis models the situation in which **all** cookies are drawn from the corresponding bowl.
                A hypothesis is represented by a string identifying the bowl.
            bowls(iterator): The bowls of cookies corresponding to each hypothesis.
                Each bowl is represented by a Pmf mapping a kind of cookie (a string) to the probability of drawing
                that cookie from the bowl.
        """
        super().__init__(hypotheses)
        self._bowls = {hypothesis: bowl for hypothesis, bowl in zip(hypotheses, bowls)}

    def update(self, data):
        """Updates each hypothesis based on the data.

        data: any representation of the data

        returns: the normalizing constant
        """
        for hypo in self.values():
            like = self.likelihood(data, hypo)
            self.multiply(hypo, like)
            self._bowls[hypo].decrement(data)
        return self.normalize()

    def likelihood(self, data, hypothesis):
        """Computes the likelihood of the data under the hypothesis.

        Args:
            hypothesis: some representation of the hypothesis
            data: some representation of the data
        """
        return self._bowls[hypothesis].fraction_of(data)


def main():
    suite = Cookie(['Bowl 1', 'Bowl 2'], [Bowl(30, 10), Bowl(20, 20)])
    for datum in ['vanilla', 'chocolate', 'vanilla']:
        suite.update(datum)
        print(f'After seeing {datum}')
        suite.print()


if __name__ == '__main__':
    main()
