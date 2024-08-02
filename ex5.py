x = set()
x.add(1)  # Adiciona o valor 1 ao conjunto
x.add(2)  # Adiciona o valor 2 ao conjunto
print(x)  # Imprime o conjunto {1, 2}

x.add(1)  # Tenta adicionar o valor 1 novamente, mas conjuntos não permitem duplicatas
print(x)  # Imprime o conjunto {1, 2} novamente, sem alterações
#Os sets são conjuntos/coleções não ordenadas de itens únicos e podem ser construídos utilizando a função set().