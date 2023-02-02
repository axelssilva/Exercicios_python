num = str(input('Digite um número entre 0 e 9999: '))
nums = num.replace(""," ")
nums = nums.strip()
m = nums[0]
c = nums[2]
d = nums[4]
u = nums[6]
print(f'Milhar: {m}\nCenteza: {c}\nDezena: {d}\nUnidade: {u}')
