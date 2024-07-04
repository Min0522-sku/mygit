x,y,z,a,b = map(int, input().split())
ans = (x*x+y*y+z*z+a*a+b*b)%10
print(ans)