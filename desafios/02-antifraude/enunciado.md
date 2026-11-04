# Desafio 02 — Verificação antifraude de cartão virtual

Em um banco digital, o sistema antifraude faz uma verificação simples antes de liberar um cartão virtual para compras. Durante um turno, um analista recebe uma sequência de códigos de operações e precisa identificar rapidamente se a conta deve ser liberada, revisada ou bloqueada. Para treinar novos desenvolvedores, a equipe criou uma versão reduzida dessa regra, baseada apenas na contagem de operações suspeitas.

## O que implementar

Leia uma lista de códigos inteiros e conte quantos deles são suspeitos. Um código é suspeito se for negativo ou se for múltiplo de 7.

Ao final, aplique a regra:

- nenhuma operação suspeita: `LIBERAR`;
- de 1 a 2 suspeitas: `REVISAR`;
- 3 ou mais suspeitas: `BLOQUEAR`.

Cada código deve ser avaliado de forma independente, mesmo que um mesmo valor atenda às duas condições; nesse caso, ele conta apenas uma vez como suspeito.

## Entrada

A primeira linha contém um inteiro N, indicando a quantidade de códigos. A segunda linha contém N inteiros separados por espaço, representando os códigos das operações.

## Saída

Exiba uma única string: `LIBERAR`, `REVISAR` ou `BLOQUEAR`, de acordo com a quantidade de códigos suspeitos encontrada.

## Exemplos

| Entrada | Saída |
| --- | --- |
| `4` / `1 2 3 5` | `LIBERAR` |
| `5` / `7 1 2 3 4` | `REVISAR` |
| `5` / `-1 14 2 3 4` | `REVISAR` |
| `6` / `-7 14 -3 8 21 1` | `BLOQUEAR` |
