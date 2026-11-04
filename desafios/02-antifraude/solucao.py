# Desafio 02 - Verificacao antifraude de cartao virtual
# Entrada: N na primeira linha, N inteiros separados por espaco na segunda.
# Saida: LIBERAR, REVISAR ou BLOQUEAR.

n = int(input())
codigos = list(map(int, input().split()))

suspeitos = 0

for codigo in codigos:
    # O "or" curto-circuita: um valor negativo e multiplo de 7 conta uma vez so.
    if codigo < 0 or codigo % 7 == 0:
        suspeitos += 1

if suspeitos == 0:
    print("LIBERAR")
elif suspeitos <= 2:
    print("REVISAR")
else:
    print("BLOQUEAR")
