# Você recebe uma lista de nomes, e uma lista de alturas que consiste de números inteiros positivos distintos.
# Ambas as listas são de comprimento `n`.
#
# Para cada índice `i`, `nomes[i]` e `alturas[i]` denotam o nome e a altura da i-ésima pessoa.
#
# Retorne os nomes ordenados em ordem decrescente pelas alturas das pessoas.
#
# ### Exemplo 1
#
# ```
# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# ```
#
# ### Exemplo 2
#
# ```
# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# ```

def q1(names, heights):
        names = ["Mary","John","Emma"]
    heights = [180,165,170]
    dict_nomes_alturas = {}
    for i,j in zip(names, heights):
        dict_nomes_alturas[i] = j
        dict_ordenado = sorted(dict_nomes_alturas.items(), key=lambda item : item[1], reverse = True)
        lista_altura = []
        for k,v in dict_ordenado:
            lista_altura.append(k)
    return lista_altura

if __name__ == '__main__':
    print(q1(["Mary", "John", "Emma"], [180, 165, 170]))
