"""The (first) cookie problem."""

import fractions

from thinkbayes import Pmf

pmf = Pmf()
pmf.set('Bowl 1', fractions.Fraction(1, 2))
pmf.set('Bowl 2', fractions.Fraction(1, 2))

pmf.multiply('Bowl 1', fractions.Fraction(3, 4))
pmf.multiply('Bowl 2', fractions.Fraction(1, 2))

pmf.normalize()

print(pmf.prob('Bowl 1'))
