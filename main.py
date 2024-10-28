# Devon Taylor
# DS
# U3L1
# 10/28/24

print("\n-----Recursion-----\n")
def sample(num):
    if num == 0:
        print("\nBASE CASE REACHED\n")
        return

    print(f"Recursing; num = {num}")
    sample(num-1)
    print(f"Returning; num = {num}")
    return

sample(5)

print("\n\n-----Loop-----\n")

def loop(num):
  baseNum = num
  while num >= 1:
    print(f"Recursing; num = {num}")
    num -= 1

  print("\nBASE CASE REACHED\n")

  while num < baseNum:
    num += 1
    print(f"Returning; num = {num}")


loop(5)