# count duration from a loop that counts 1 to 1_000_000.
# usar o modulo time para capturar o tempo antes e depois da execução
# exibir quanto tempo foi gasto

import time

nums = []


before = time.perf_counter()
print(before)

for num in range(1, 1_000_001):
    nums.append(num)

after = time.perf_counter()
print(after)

print(after - before)
print(nums[999_999])
