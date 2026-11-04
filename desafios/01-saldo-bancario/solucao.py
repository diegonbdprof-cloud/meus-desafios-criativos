# Desafio 01 - Verificador de saldo do caixa automatico
# Entrada: N na primeira linha, depois N inteiros (um por linha).
# Saida: "saldo X" ou "saldo insuficiente".

n = int(input())
saldo = 0
insuficiente = False

for _ in range(n):
    operacao = int(input())

    if operacao > 0:          # deposito
        saldo += operacao
    elif operacao < 0:        # saque
        saldo += operacao
        if saldo < 0:
            insuficiente = True
            break
    # operacao == 0 e invalida e o laco simplesmente segue

if insuficiente:
    print("saldo insuficiente")
else:
    print(f"saldo {saldo}")
