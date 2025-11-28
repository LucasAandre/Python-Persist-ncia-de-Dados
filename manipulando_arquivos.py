# Escrevendo um arquivo com a função open()
with open('dados.txt', 'w') as f: # Esse modo substitui todo o conteúdo do arquivo pelo que será escrito
    f.write('Hello, world!')

# Lendo um arquivo com a função open()
with open('dados.txt', 'r') as f:
    conteudo = f.read()

print(conteudo) # Hello, world!

# Adicionando uma informação na última linha do arquivo
with open('dados.txt', 'a') as f: # a: modo append. Esse modo não substitui como o modo write.
    f.write('última linha')
