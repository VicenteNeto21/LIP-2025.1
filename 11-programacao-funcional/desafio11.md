# Programação Funcional

## Introdução

A programação funcional é um paradigma que trata a computação como a avaliação de funções matemáticas, evitando estados mutáveis e dados mutáveis. Dois conceitos importantes desse paradigma são:

- **Funções de alta ordem**: funções que recebem outras funções como argumento ou retornam funções.
- **Recursão**: técnica onde uma função chama a si mesma para resolver subproblemas.

---

## Problema: Soma de números pares ao quadrado de uma lista

Queremos pegar uma lista de inteiros, filtrar apenas os números pares, elevar cada um ao quadrado e somar os resultados.

---

## Solução em Python (programação funcional)

```python
from functools import reduce

def soma_pares_ao_quadrado(lista):

    pares = filter(lambda x: x % 2 == 0, lista)
    ao_quadrado = map(lambda x: x ** 2, pares)
    return reduce(lambda acc, x: acc + x, ao_quadrado, 0)

# Exemplo de uso
numeros = [1, 2, 3, 4, 5, 6]
resultado = soma_pares_ao_quadrado(numeros)
print(f"Resultado: {resultado}")
```

## Exemplo: Recursão com Fatorial
```python
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print(f"Fatorial de 5: {fatorial(5)}")
```
#### Resultado:
```python
Resultado: 56
Fatorial de 5: 120
```
## Vantagens da Programação Funcional

A programação funcional oferece uma série de benefícios que a tornam uma escolha atrativa para diversos tipos de problemas, especialmente aqueles que exigem maior previsibilidade, modularidade e segurança. Abaixo estão algumas das principais vantagens explicadas:

### Código mais limpo e conciso
Como a programação funcional evita estados mutáveis e utiliza funções puras, o código tende a ser menor e mais fácil de entender. A combinação de funções como `map`, `filter` e `reduce` permite escrever lógicas complexas em poucas linhas, promovendo a legibilidade.

### Facilidade de paralelização
Como as funções funcionais não dependem de estados externos e não causam efeitos colaterais, elas podem ser executadas em paralelo com segurança. Isso facilita o uso de programação concorrente ou paralela, aproveitando melhor os recursos de sistemas multi-core.

### Menor risco de efeitos colaterais
Funções puras sempre retornam o mesmo resultado para os mesmos argumentos e não alteram variáveis externas. Isso reduz bugs relacionados a estado compartilhado, facilitando a manutenção e testes do código.

### Modularidade e reusabilidade
Funções são tratadas como cidadãos de primeira classe, podendo ser passadas como argumentos ou retornadas. Isso favorece a criação de componentes reutilizáveis e uma estrutura de código mais modular.

### Testabilidade
Como as funções puras são isoladas e previsíveis, é fácil escrever testes para elas, o que aumenta a confiabilidade do sistema como um todo.
