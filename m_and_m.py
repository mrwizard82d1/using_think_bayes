"""A solution to the M&M problem using a Suite."""

from thinkbayes import Suite


class MAndM(Suite):
    """Models a solution to the M&M problem using a Suite."""

    def likelihood(self, data, hypothesis):
        mix94 = dict(brown=30,
                     yellow=20,
                     red=20,
                     green=10,
                     orange=10,
                     tan=10)
        mix96 = dict(blue=24,
                     green=20,
                     orange=16,
                     yellow=14,
                     red=13,
                     brown=13)

        hypo_a = dict(bag1=mix94, bag2=mix96)
        hypo_b = dict(bag1=mix96, bag2=mix94)

        hypotheses = dict(A=hypo_a, B=hypo_b)
        bag, color = data
        mix = hypotheses[hypothesis][bag]
        result = mix[color]
        return result


def main():
    suite = MAndM('AB')
    suite.update(('bag1', 'yellow'))
    suite.update(('bag2', 'green'))
    suite.print()


if __name__ == '__main__':
    main()

