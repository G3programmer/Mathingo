import random
from math import log10, log2

def formatar_alternativas(valores, resposta_certa):
    random.shuffle(valores)
    letras = ['a', 'b', 'c', 'd']
    alternativas_formatadas = [f"{letras[i]}) {valores[i]}" for i in range(len(valores))]
    letra_correta = letras[valores.index(resposta_certa)]
    return alternativas_formatadas, letra_correta

def gerar_questao_logaritmo():
    base = random.choice([2, 10])
    expoente = random.randint(1, 4)
    valor = base ** expoente
    resposta = expoente

    alternativas, correta = formatar_alternativas(
        [resposta, resposta + 1, resposta - 1, resposta + 2], resposta
    )

    return {
        "pergunta": f"Qual o valor de log base {base} de {valor}?",
        "alternativas": alternativas,
        "correta": correta
    }

def gerar_questao_exponencial():
    base = random.randint(2, 5)
    expoente = random.randint(1, 3)
    resultado = base ** expoente

    alternativas, correta = formatar_alternativas(
        [resultado, resultado + 1, resultado - 1, resultado + 2], resultado
    )

    return {
        "pergunta": f"Quanto é {base}^{expoente}?",
        "alternativas": alternativas,
        "correta": correta
    }

# Gera quiz com 5 perguntas aleatórias
geradores = [gerar_questao_logaritmo, gerar_questao_exponencial]
quiz = [random.choice(geradores)() for _ in range(10)]

# Execução do quiz
pontuacao = 0
print("===== Quiz Matemático Dinâmico =====\n")

for i, q in enumerate(quiz):
    print(f"Questão {i + 1}: {q['pergunta']}")
    for alt in q["alternativas"]:
        print(alt)
    resp = input("Sua resposta: ").strip().lower()
    if resp == q["correta"]:
        print("✅ Correto!\n")
        pontuacao += 1
    else:
        print(f"❌ Errado! A resposta correta era: {q['correta']}\n")

print(f"🏁 Pontuação final: {pontuacao} de {len(quiz)}")
