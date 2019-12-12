#check all the substr, and change it to the length
def generate_generalized_abbreviation(word):
    left,right=0,0
    res=[word]
    words = list(word)
    for right in range(len(words)):
        for left in range(right+1):
            tmp=word[0:left]+str(right-left)+word[right:]
            res.append(tmp)
    return res


def main():
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
  print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))


main()