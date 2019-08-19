from math import gcd

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).

           Argument:
                takes 2 int or float in parameter.
        """
        if not isinstance(numerator, int) or isinstance(numerator, float):
            return TypeError
        if not isinstance(denominator, int) or isinstance(denominator, float):
            return TypeError
        if denominator == 0:
            if numerator ==0:
                raise ValueError('can be 0 on both parameter')
            elif numerator > 0:
                self.numerator = 1
                self.denominator = 0
            else:
                self.numerator = -1
                self.denominator = 0
        else:
                # my Fraction can take float
            while (denominator != int(denominator)) or (numerator != int(numerator)):
                    denominator *= 10
                    numerator *= 10
            numerator = int(numerator)
            denominator = int(denominator)
            
            # positive or negative ?
            if denominator < 0  and numerator > 0:
                denominator = abs(denominator)
                numerator = -numerator
            elif numerator < 0  and denominator < 0:
                denominator = abs(denominator)
                numerator = abs(numerator)

            # make into proper form
            self.gcd = gcd(numerator, denominator)
            self.numerator = numerator/self.gcd
            self.denominator = denominator/self.gcd
        
        

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        if not isinstance(frac, Fraction):
            return False
        else:
            new_deno = self.denominator * frac.denominator
            new_numa = self.numerator*frac.denominator + self.denominator*frac.numerator
            return Fraction(new_numa,new_deno) 


    #TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    #Optional have fun and overload other operators such as 
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __mul__(self, frac):
        if not isinstance(frac, Fraction):
            return False
        else:
            return Fraction((self.numerator*frac.numerator),(self.denominator*frac.denominator))

    def __str__(self):
        if self.numerator% self.denominator == 0:
            return f"{int(self.numerator/self.denominator)}"
        return f"{int(self.numerator)}/{int(self.denominator)}"

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
