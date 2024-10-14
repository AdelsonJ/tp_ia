# Solução para o Problema do Caixeiro Viajante utilizando PSO

Este trabalho apresenta uma solução para o problema do Caixeiro Viajante (TSP) utilizando o algoritmo de Otimização por Enxame de Partículas (PSO). O método PSO, apesar de algumas inconsistências dependendo da forma como é aplicado, mostra-se uma abordagem satisfatória devido à sua fácil implementação.

## Como Executar o Algoritmo

Para executar o algoritmo, utilize o seguinte comando:

```bash
    python TP1.py p i g
```
onde:
- python: Sua versão do Python.
- p: Número de partículas.
- i: Número de iterações.
- g: Opção para plotar o grafo. Use 1 para sim e 0 para não.

## Exemplos de Uso
```bash
    python TP1.py 30 100 1
```
Neste exemplo, o algoritmo será executado com 30 partículas, 100 iterações e o grafo será plotado.

## Observações Importantes
Este estudo foi crucial para entender melhor as técnicas de resolução de problemas NP-completos. Através da análise realizada, foi possível observar a importância de balancear adequadamente o número de partículas, iterações e cidades:

- Número de Partículas: Um maior número de partículas tende a melhorar o desempenho do algoritmo.
- Número de Cidades: Um aumento no número de cidades resulta em uma queda na eficiência- .
- Número de Iterações: Deve ser ajustado conforme o número de partículas e cidades para otimizar a performance.
Essas descobertas destacam a necessidade de uma implementação equilibrada e bem ajustada para alcançar os melhores resultados possíveis.

## Conclusão
O método PSO, com suas vantagens de fácil implementação e capacidade de exploração do espaço de soluções, mostra-se uma técnica promissora para a resolução do problema do Caixeiro Viajante. Este trabalho contribui tanto para o entendimento teórico quanto para a aplicação prática do PSO em problemas complexos.
