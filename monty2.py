"""A second solution to the Monty Hall problem using Suite."""

import fractions

from thinkbayes import Suite


class Monty(Suite):
    """A general solution to the Monty Hall problem."""

    def likelihood(self, data, hypothesis):
        """Calculate the likelihood of observing data if hypo is true.
        
        Args:
            data (object): The observed datum.
            hypothesis (object): The hypothesis assumed to be true.
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
    suite = Monty('ABC')
    suite.update('B')
    suite.print()


if __name__ == '__main__':
    main()
