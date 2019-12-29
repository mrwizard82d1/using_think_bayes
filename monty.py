"""Script to solve the Monty Hall problem."""


import fractions

from thinkbayes import Pmf


class Monty(Pmf):
    """A generic framework for solving the Monty Hall problem."""

    def __init__(self, hypotheses):
        """Construct a specific solution to the Monty Hall problem.

        Args:
            hypotheses (iterator): the sequence of hypotheses.
        """

        super().__init__()
        for hypothesis in hypotheses:
            self.set(hypothesis, 1)

        self.normalize()

    def update(self, data):
        """Calculate the posterior probabilities after seeing data.

        Args:
            data (object): The observed datum.
        """

        for hypothesis in self.values():
            self.multiply(hypothesis, self.likelihood(hypothesis, data))

        self.normalize()

    def likelihood(self, hypothesis, data):
        """Calculate the likelihood of observing data given hypothesis is true.

        Args:
            hypothesis (object): The hypothesis assumed to be true.
            data (object): The observed datum.
        """

        if hypothesis == data:
            # If the car is behind door, hypothesis, Monty **cannot** open the door
            return 0
        elif hypothesis == 'A':
            # If the car is behind door 'A', Monty can show door 'B' **or** door 'C' with equal probability.
            return fractions.Fraction(1, 2)
        else:
            # Otherwise, the car must behind door 'C' so Monty **must** show door 'B'
            return 1


def main():
    monty_hypotheses = 'ABC'
    pmf = Monty(monty_hypotheses)
    pmf.update('B')
    for hypothesis, probability in pmf.items():
        print(hypothesis, probability)


if __name__ == '__main__':
    main()
