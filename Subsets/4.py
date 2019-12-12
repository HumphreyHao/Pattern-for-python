def generate_valid_parentheses(num):
    lists=[]
    list1=[]
    helper(num,num,list1,lists)
    return lists

def helper(left,right,list1,lists):
    if left ==0 and right==0:
        str1="".join(list1)
        lists.append(str1)
        return
    if left>0:
        list1.append('(')
        helper(left-1,right,list1,lists)
        del list1[-1]
    if right>0 and right>left:
        list1.append(')')
        helper(left,right-1,list1,lists)
        del list1[-1]


def main():
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
  print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()