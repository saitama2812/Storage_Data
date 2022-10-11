def sum_and_compare(thomas_sum) :
  result = 1  # Initially assume Thomas' rank is 1
  for i in range(n-1) :
    eng, ger, mat, his = map(int, input().split())
    another_sum = eng + ger + mat + his
    if (another_sum > thomas_sum) :  # if someone scored more than Thomas
      #print("if condition entered")
      result = result + 1            # Thomas's rank increases by 1
      #print("Thomas rank now is",result)
      #break
  return result

n = int(input())
t_eng,t_ger,t_mat,t_his = map(int, input().split())

thomas_sum = t_eng + t_ger + t_mat + t_his
result = sum_and_compare(thomas_sum)

print(result)
