# Desafio de Pintura

## Descrição

Este programa resolve um problema de pintura em uma imagem representada por uma matriz de pixels. A imagem é composta por pixels pretos e brancos, onde 0 representa branco e 1 representa preto. A operação permitida é inverter a cor dos pixels em uma área retangular selecionada. O objetivo é determinar o número mínimo de operações necessárias para transformar uma matriz de pixels totalmente branca em uma matriz de pixels desejada, ou indicar que a tarefa é impossível.

## Entrada

O programa recebe várias entradas, onde cada caso de teste começa com uma linha contendo quatro inteiros:

- `n`: número de linhas da matriz (1 ≤ n ≤ 100)
- `m`: número de colunas da matriz (1 ≤ m ≤ 100)
- `r`: número de linhas do retângulo de operação (1 ≤ r ≤ n)
- `c`: número de colunas do retângulo de operação (1 ≤ c ≤ m)

Seguem-se `n` linhas, cada uma contendo `m` caracteres (0 ou 1), representando a matriz desejada.

A entrada termina com uma linha contendo quatro zeros (`0 0 0 0`).

## Saída

Para cada caso de teste, o programa imprime uma linha contendo o número mínimo de operações necessárias para transformar a matriz inicial em uma matriz desejada. Se for impossível, imprime `-1`.

## Exemplo de Entrada

```
3 3 1 1
010
101
010
4 3 2 1
011
110
011
110
3 4 2 2
0110
0111
0000
0 0 0 0
```

## Exemplo de Saída

```
4
6
-1
```

## Como Executar

1. Certifique-se de ter o Python 3.11 instalado em sua máquina.
2. Salve o código em um arquivo com a extensão `.py`, por exemplo, `desafio_pintura.py`.
3. Execute o programa através do terminal ou prompt de comando com o seguinte comando:

   ```bash
   python desafio_pintura.py
   ```

4. Insira a entrada conforme o formato especificado.

## Notas

- O código foi projetado para resolver o problema de forma eficiente, mas pode haver casos em que o tempo de execução seja maior devido ao tamanho da matriz e ao número de operações necessárias. A eficiência do algoritmo pode ser melhorada se necessário.
