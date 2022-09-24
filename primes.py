"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
    list = []
    if number_of_primes <= 0:
        raise ValueError("Please provide a prime amount that is greater than 0!")
    # Parameter is valid, proceed with rest of code.
    else:
        remainingPrimes = number_of_primes
        numCount = 1
        while remainingPrimes > 0:
            numCount += 1

            for i in range(2, numCount):
                # primes can only be divided by 1 and itself. If any number in the range 2 to numCount-1 gives remainder of
                # 0, then non prime.
                # For the base case '2' the for loop looks in the range 2-2. But there are no integers between this!
                if numCount % i == 0:
                    break
            else:
                # Went through the whole for loop without finding another dividing number, so number is prime.
                list.append(numCount)
                remainingPrimes -= 1

    return list
