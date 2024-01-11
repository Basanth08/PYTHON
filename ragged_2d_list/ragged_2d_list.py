"""
    ragged_2d_list.py
"""

def ragged_2d_list(col_counts):
      return [[x for x in range(1, col+1)] for col in col_counts if col > 0]

def main():
    ragged = ragged_2d_list([3, -1, 1, 6, 0, 2, 8])
    for row in ragged:
        print(row)

if __name__ == "__main__":
    main()