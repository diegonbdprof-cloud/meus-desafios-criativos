# Desafio 01 — Verificador de saldo do caixa automático

Em um banco digital, o sistema de auditoria precisa revisar uma sequência de operações feitas por um caixa automático. Cada operação pode ser um depósito, um saque ou um valor inválido. Como a equipe quer um verificador simples para treinar novos programadores, você deve criar um programa que percorra todas as operações e decida o resultado final da conta.

## O que implementar

Leia a quantidade de operações e, em seguida, processe cada valor inteiro informado:

- valores positivos são depósitos;
- valores negativos são saques;
- o valor zero é uma operação inválida e deve ser ignorada.

O saldo inicial da conta é 0. Se em qualquer momento um saque fizer o saldo ficar negativo, o programa deve interromper o processamento imediatamente e exibir `saldo insuficiente`. Caso contrário, ao final, exiba `saldo X`, em que X é o saldo final.

O desafio exige o uso de condicionais para classificar cada operação e de laço para percorrer a lista de valores.

## Entrada

A primeira linha contém um inteiro N, indicando a quantidade de operações. As N linhas seguintes contêm um inteiro cada, representando uma operação bancária. Os valores devem ser processados na ordem em que aparecem.

## Saída

Se algum saque tornar o saldo negativo, imprima exatamente `saldo insuficiente`. Caso isso não aconteça, imprima exatamente `saldo X`, em que X é o saldo final após processar todas as operações válidas.

## Exemplos

| Entrada | Saída |
| --- | --- |
| `4 / 10 / -3 / 0 / 5` | `saldo 12` |
| `3 / 8 / -10 / 4` | `saldo insuficiente` |
| `5 / 0 / 0 / 7 / -2 / -1` | `saldo 4` |
| `2 / 0 / 0` | `saldo 0` |

As barras separam uma linha da seguinte.
