# OtakuScript: Mini-Gramática Fictícia

**Desafio 03 – Descrições Sintáticas e Semânticas**  
Linguagem fictícia baseada em comandos de transformação e ação mágica inspirados em animes.

---

## Análise Léxica

| Tipo       | Exemplo                   | Descrição                            |
|------------|---------------------------|--------------------------------------|
| `@PERSONA` | `@Sakura`                 | Nome de personagem                   |
| `#FORM`    | `#MagicalGirl`            | Forma mágica                         |
| `^ACTION`  | `^TRANSFORM`, `^ATTACK`   | Tipo de ação                         |
| `:`        | `:`                       | Separador entre entidade e ação      |
| `STRING`   | `"Yatta!"`, `"Rasengan!"` | Expressão literal                    |
| `!`        | `!`                       | Finalizador de comando               |

---

## Gramática

```bnf
<programa>     ::= <comando> { <comando> }

<comando>      ::= <personagem> ":" <acao> ":" <expressao> "!"

<personagem>   ::= "@" <identificador>
<acao>         ::= "^" <verbo_acao> [ "#" <forma> ]
<forma>        ::= <identificador>
<expressao>    ::= "\"" <texto> "\""

<identificador>::= [A-Za-z_][A-Za-z0-9_]*
<verbo_acao>   ::= "TRANSFORM" | "ATTACK" | "SUMMON"
<texto>        ::= qualquer sequência de caracteres
```
---
## Sematica
| Ação          | Significado                                                |
|---------------|------------------------------------------------------------|
| `^TRANSFORM`  | Transforma o personagem na forma mágica indicada           |
| `^ATTACK`     | Executa um golpe especial com nome simbólico               | 
| `^SUMMON`     | Invoca um aliado ou monstro com uma fala de invocação      |

---

## Análise Léxica + Sintática (Exemplo)

```bnf
@Sakura:^TRANSFORM:#MagicalGirl:"Yatta!"!
@Naruto:^ATTACK:"Rasengan!"!
@Yugi:^SUMMON:"Dark Magician, apareça!"!
```
---

## Codigo:

```python
import re

def parse_otakuscript(code):
    pattern = re.compile(r'@(\w+):\^(\w+)(:#(\w+))?:\"(.+?)\"!')
    for match in pattern.finditer(code):
        personagem, acao, _, forma, fala = match.groups()
        print(f" {personagem} executa {acao} {'com forma ' + forma if forma else ''}: '{fala}'")

codigo = '''
@Sakura:^TRANSFORM:#MagicalGirl:"Yatta!"!
@Naruto:^ATTACK:"Rasengan!"!
@Yugi:^SUMMON:"Dark Magician, apareça!"!
'''S

parse_otakuscript(codigo)

```