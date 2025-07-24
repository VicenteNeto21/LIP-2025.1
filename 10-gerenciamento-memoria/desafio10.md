# 10 – Gerenciamento de Memória

## O que é?

O gerenciamento de memória é uma parte fundamental da execução de programas. Ele determina como a memória é alocada, utilizada e liberada durante a execução de um software. Diferentes linguagens de programação adotam abordagens distintas para esse gerenciamento.

Neste comparativo, analisamos duas linguagens bastante contrastantes nesse aspecto: **Java**, que utiliza coleta de lixo automática (Garbage Collection), e **C**, onde o programador é responsável por alocar e liberar a memória manualmente. A seguir, apresentamos uma tabela comparativa entre essas abordagens.


## Comparação entre Java e C

| Característica                  | Java (Gerenciamento Automático)                       | C (Gerenciamento Manual)                         |
|--------------------------------|--------------------------------------------------------|--------------------------------------------------|
| Alocação de Memória            | Automática (uso de `new`)                             | Manual (`malloc`, `calloc`, `realloc`)           |
| Liberação de Memória           | Feita automaticamente pelo Garbage Collector (GC)     | Deve ser feita manualmente com `free`            |
| Coletor de Lixo (GC)           | Sim – executa em segundo plano                        | Não possui                                       |
| Controle do Programador        | Menor controle (GC decide quando liberar memória)     | Total controle sobre alocação/liberação          |
| Risco de Vazamento de Memória  | Baixo (se programado corretamente)                    | Alto (se esquecer de usar `free`)                |
| Risco de Acesso Inválido       | Baixo (verificações de tempo de execução)             | Alto (ponteiros inválidos ou memória já liberada)|
| Facilidade para Iniciantes     | Mais fácil, menos propenso a erros graves             | Mais difícil, exige maior atenção do programador |
| Performance em Tempo Real      | Menor previsibilidade (GC pode pausar execução)       | Maior controle e previsibilidade                 |

