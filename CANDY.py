 while True:
 	n = int(input())
 	if n == -1:
 		break
 	ar = [int(input()) for _ in range(n)]
 	if sum(ar)%n != 0:
 		print(-1)
 		continue
 	c = sum(ar)//n
 	print(sum(i-c for i in ar if i >c))
