#dfs
def find_letter_case_string_permutations(str):
    list1=list(str)
    lists=[str]
    visited=[]
    for i in str:
        visited.append(0)
    helper(list1,lists,visited,0)
    return lists
def helper(list1,lists,visited,start):
    if start>=len(list1):
        return
    for i in range(start,len(list1)):
        if visited[i] ==0 :
            if list1[i]>='0' and list1[i]<='9':
                continue
            visited[i]=1
            list1[i]=list1[i].upper()
            strtmp=''.join(list1)
            lists.append(strtmp)
            helper(list1,lists,visited,i+1)
            list1[i]=list1[i].lower()
            visited[i]=0

def main():
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ad52")))
  print("String permutations are: " +
        str(find_letter_case_string_permutations("ab7c")))


main()
