# Comparação de Tipagem: Python, C e JavaScript

## Resumo da Tipagem

| Linguagem   | Tipo de Tipagem     | Forte vs Fraca | Estática vs Dinâmica |
|-------------|---------------------|----------------|-----------------------|
| Python      | Dinâmica e forte    | Forte          | Dinâmica              |
| C           | Estática e fraca    | Fraca          | Estática              |
| JavaScript  | Dinâmica e fraca    | Fraca          | Dinâmica              |

---

## Python

### Características
- Tipagem **dinâmica**: o tipo é determinado em tempo de execução.
- Tipagem **forte**: não permite operar diretamente entre tipos incompatíveis.

### Exemplo

```python
x = 10        # inteiro
x = "dez"     # agora é uma string

print(x + 5)  # Erro! Não é possível somar string com inteiro
```
Python detecta e bloqueia operações inválidas entre tipos, mesmo sendo dinamicamente tipada.


## Linguagem C

### Características
- Tipagem **estática:** o tipo é definido em tempo de compilação.

- Tipagem **fraca:** permite conversões implícitas entre tipos.

Exemplo
```c
#include <stdio.h>

int main() {
    int x = 10;
    float y = 2.5;
    float resultado = x + y;
    printf("%f\n", resultado);
    return 0;
}
```
**Obs:** O compilador converte x (int) para float automaticamente. Essa conversão implícita mostra a fraqueza da tipagem.

---
## JavaScript

### Características

- Tipagem **dinâmica**: tipo dos dados é definido durante a execução.
- Tipagem **fraca**: permite coerção entre tipos automaticamente.

Exemplo
```javascript
let x = "10";
let y = 5;
let resultado = x + y;

console.log(resultado);  // "105"
```
**Obs:** JavaScript converte y em string e concatena — comportamento típico da tipagem fraca e dinâmica.

---
# Conclusão
 - Python prioriza segurança ao evitar operações ambíguas.
 - C é rígido na definição dos tipos, mas permissivo nas conversões.
 - JavaScript é flexível, mas pode gerar comportamentos inesperados.