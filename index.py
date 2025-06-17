quiz = [
    {"pergunta": "1) Qual o coeficiente angular da função f(x) = -3x + 2?", "alternativas": ["a) -3", "b) 2", "c) 3", "d) -2"], "correta": "a"},
    {"pergunta": "2) O ponto onde f(x) = 2x - 5 corta o eixo y é:", "alternativas": ["a) (0, -5)", "b) (-5, 0)", "c) (0, 2)", "d) (2, 0)"], "correta": "a"},
    {"pergunta": "3) A função f(x) = 0x + 4 representa:", "alternativas": ["a) Uma reta horizontal", "b) Uma parábola", "c) Uma reta vertical", "d) Uma exponencial"], "correta": "a"},
    {"pergunta": "4) A raiz da função f(x) = 4x - 8 é:", "alternativas": ["a) 2", "b) -2", "c) 8", "d) 4"], "correta": "a"},
    {"pergunta": "5) A função f(x) = -2x - 1 é:", "alternativas": ["a) Crescente", "b) Decrescente", "c) Constante", "d) Par"], "correta": "b"},
    {"pergunta": "6) Qual o valor do discriminante da função f(x) = x² - 6x + 9?", "alternativas": ["a) 0", "b) 3", "c) -3", "d) 9"], "correta": "a"},
    {"pergunta": "7) O vértice da função f(x) = x² - 2x + 1 é:", "alternativas": ["a) (1, 0)", "b) (0, 1)", "c) (1, 1)", "d) (-1, 0)"], "correta": "a"},
    {"pergunta": "8) A concavidade da parábola f(x) = -x² + 4x - 5 é:", "alternativas": ["a) Voltada para cima", "b) Voltada para baixo", "c) Não tem concavidade", "d) É uma reta"], "correta": "b"},
    {"pergunta": "9) A função f(x) = x² - 1 corta o eixo y em:", "alternativas": ["a) (0, -1)", "b) (1, 0)", "c) (-1, 0)", "d) (0, 1)"], "correta": "a"},
    {"pergunta": "10) A equação x² - 4 = 0 tem como soluções:", "alternativas": ["a) x = ±2", "b) x = 2", "c) x = -2", "d) x = 0"], "correta": "a"},
    {"pergunta": "11) O valor de |–8| é:", "alternativas": ["a) 8", "b) -8", "c) 0", "d) 1"], "correta": "a"},
    {"pergunta": "12) O gráfico de f(x) = |x| tem vértice no ponto:", "alternativas": ["a) (0, 0)", "b) (1, 0)", "c) (0, 1)", "d) (1, 1)"], "correta": "a"},
    {"pergunta": "13) A equação |x - 2| = 3 tem como solução:", "alternativas": ["a) x = -1 ou 5", "b) x = 1 ou -5", "c) x = -1", "d) x = 5"], "correta": "a"},
    {"pergunta": "14) A inequação |x + 1| < 4 tem como solução:", "alternativas": ["a) -5 < x < 3", "b) -3 < x < 3", "c) -4 < x < 4", "d) -1 < x < 4"], "correta": "c"},
    {"pergunta": "15) O gráfico de f(x) = |x - 3| desloca-se:", "alternativas": ["a) 3 unidades para a direita", "b) 3 unidades para a esquerda", "c) 3 para cima", "d) 3 para baixo"], "correta": "a"},
    {"pergunta": "16) O valor de 2^3 é:", "alternativas": ["a) 6", "b) 8", "c) 9", "d) 10"], "correta": "b"},
    {"pergunta": "17) O gráfico de f(x) = 2^x passa por qual ponto fixo?", "alternativas": ["a) (1, 0)", "b) (0, 1)", "c) (2, 0)", "d) (0, 2)"], "correta": "b"},
    {"pergunta": "18) Qual a base da função que passa por (0, 1) e (1, 5)?", "alternativas": ["a) 4", "b) 5", "c) 6", "d) 3"], "correta": "b"},
    {"pergunta": "19) f(x) = (1/2)^x é:", "alternativas": ["a) Crescente", "b) Decrescente", "c) Constante", "d) Logarítmica"], "correta": "b"},
    {"pergunta": "20) 3^x = 9, então x =", "alternativas": ["a) 2", "b) 3", "c) 1", "d) 0"], "correta": "a"},
    {"pergunta": "21) log₁₀(100) é igual a:", "alternativas": ["a) 1", "b) 2", "c) 3", "d) 10"], "correta": "b"},
    {"pergunta": "22) log₂(8) =", "alternativas": ["a) 2", "b) 3", "c) 4", "d) 1"], "correta": "b"},
    {"pergunta": "23) O domínio de f(x) = log(x - 4) é:", "alternativas": ["a) x > 4", "b) x < 4", "c) x ≥ 4", "d) x > 0"], "correta": "a"},
    {"pergunta": "24) log₃(1) é:", "alternativas": ["a) 1", "b) 3", "c) 0", "d) Indefinido"], "correta": "c"},
    {"pergunta": "25) A função logarítmica f(x) = logₐ(x) é crescente se:", "alternativas": ["a) a < 0", "b) 0 < a < 1", "c) a = 1", "d) a > 1"], "correta": "d"}
]

pontuacao = 0
print("===== Quiz de Funções (Completo) =====\n")

for i, q in enumerate(quiz):
    print(f"Questão {i+1}:")
    print(q["pergunta"])
    for alt in q["alternativas"]:
        print(alt)
    resp = input("Sua resposta: ").strip().lower()
    if resp == q["correta"]:
        print("✅ Correto!\n")
        pontuacao += 1
    else:
        print(f"❌ Errado! A resposta certa era: {q['correta']}\n")

print(f"Sua pontuação final: {pontuacao} de {len(quiz)}")
