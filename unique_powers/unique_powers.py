"""
  unique_powers.py
"""
def unique_powers(bases, exponents):
    powers = set()
    for base in bases:
      for exponent in exponents:
        power = base ** exponent
        if power not in powers:
          powers.add(power)
    return powers
          
def main():
    bases = {1, 2, 3}
    exponents = {0, 1, 2} 
    print(unique_powers(bases, exponents))

if __name__ == "__main__":
  main()