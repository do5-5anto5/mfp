# print 'tarefa executada' apos 6 segundos de iniciar a execução do script

import time

for _ in range(6):
    time.sleep(1)
    print(abs(-5 + _))

print("tarefa executada")
