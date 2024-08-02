dicionario2 = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
# Podemos chamar itens de uma lista presente na posição referente à chave 'key3'
dicionario2['key3'][0]
# Podemos chamar métodos nos itens também
dicionario2['key3'][0].upper()
dicionario2['key1'] = dicionario2['key1'] - 123