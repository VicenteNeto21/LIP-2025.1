import re

# ====== TOKENS DEFINIÇÕES ======
TOKEN_REGEX = {
    'ACT': r'@([A-Z]+)',
    'CHAR': r'#([a-zA-Z0-9_]+)',
    'POW': r'\^([A-Z_]+)',
    'EXP': r'~([a-z]+)',
    'MSG': r'"([^"]+)"',
    'SEP': r':',
    'END': r'!',
}

# ====== ANALISADOR LÉXICO ======
def lexer(line):
    tokens = []
    while line:
        matched = False
        line = line.lstrip()
        for token_type, pattern in TOKEN_REGEX.items():
            match = re.match(pattern, line)
            if match:
                if match.lastindex:  # existe grupo de captura
                    value = match.group(1)
                else:
                    value = match.group(0)
                tokens.append((token_type, value))
                line = line[match.end():]
                matched = True
                break
        if not matched:
            raise SyntaxError(f"Token desconhecido: {line}")
    return tokens

# ====== ANALISADOR SINTÁTICO ======
def parser(tokens):
    if not tokens or tokens[0][0] != 'ACT':
        raise SyntaxError("Esperado comando de ação começando com @")

    ast = {
        'action': tokens[0][1],
        'character': None,
        'effect': None,
        'message': None
    }

    idx = 1
    if tokens[idx][0] != 'SEP': raise SyntaxError("Esperado ':' após ação")
    idx += 1

    if tokens[idx][0] != 'CHAR': raise SyntaxError("Esperado personagem (#Nome)")
    ast['character'] = tokens[idx][1]
    idx += 1

    if tokens[idx][0] != 'SEP': raise SyntaxError("Esperado ':' após personagem")
    idx += 1

    if tokens[idx][0] not in ('POW', 'EXP'): raise SyntaxError("Esperado efeito (^PODER ou ~expressão)")
    ast['effect'] = tokens[idx][1]
    idx += 1

    # Verifica se há mensagem opcional
    if idx < len(tokens) and tokens[idx][0] == 'SEP':
        idx += 1
        if tokens[idx][0] == 'MSG':
            ast['message'] = tokens[idx][1]
            idx += 1

    # Verifica se termina com END (!)
    if tokens[-1][0] != 'END':
        raise SyntaxError("Esperado '!' no final")

    return ast

# ====== INTERPRETADOR ======
def interpret(ast):
    action = ast['action']
    char = ast['character']
    effect = ast['effect']
    msg = ast['message']

    if action == "TRANSFORM":
        resultado = f"{char} se transforma usando {effect}!"
    elif action == "ATTACK":
        resultado = f"{char} ataca com {effect}!"
    elif action == "FEEL":
        resultado = f"{char} expressa emoção: {effect}!"
    elif action == "EAT_RAMEN":
        resultado = f"{char} está comendo ramen como um verdadeiro protagonista de slice of life!"
    else:
        resultado = f"{char} executa a ação '{action}' com {effect}!"

    if msg:
        resultado += f' E grita: "{msg}"'

    return resultado

# ====== COMPILADOR PRINCIPAL ======
def compile_otakuscript(code_line):
    print("Código:", code_line)
    tokens = lexer(code_line)
    print("Tokens:", tokens)
    ast = parser(tokens)
    print("AST:", ast)
    output = interpret(ast)
    print("Interpretação:", output)

# ====== EXEMPLOS ======
if __name__ == "__main__":
    exemplos = [
        '@TRANSFORM:#Sakura:^MAGICAL_GIRL_MODE:"Yatta!"!',
        '@FEEL:#Asuka:~baka:"Não é como se eu gostasse de você!"!',
        '@ATTACK:#Goku:^KAMEHAMEHA:"HAAAAAAA!"!',
        '@EAT_RAMEN:#Naruto:~happy:"Oishiii~"!',
        '@JUMP:#Luffy:^GOMU_GOMU_NO_ROCKET!',
    ]
    for linha in exemplos:
        print("\n----------------------------")
        try:
            compile_otakuscript(linha)
        except SyntaxError as e:
            print("Erro:", e)
