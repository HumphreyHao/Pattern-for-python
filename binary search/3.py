import bisect
def search_next_letter(letters, key):
    index=bisect.bisect(letters,key)%len(letters)
    return letters[index]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()