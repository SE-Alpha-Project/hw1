def fib(n):
  if(n == 0): return 0
  elif(n == 2 or n == 1): return 1
  return fib(n-1) + fib(n-2)

def main():
    #n = int(input("Which fibonacci number do you want to find? "))
    n=10
    print(fib(n))
    
main()
