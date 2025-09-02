# Lista para armazenar alunos
alunos = []

# Quantos alunos cadastrar
quantidade = int(input("Quantos alunos deseja cadastrar? "))

# Loop para cadastrar cada aluno
for i in range(quantidade):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    nota = int(input("Digite a nota do aluno: "))
    
    # Adiciona aluno como dicionário na lista
    alunos.append({"nome": nome, "idade": idade, "nota": nota})

# Mostra a lista de alunos cadastrados
print("\nLista de alunos cadastrados:")
for aluno in alunos:
    print("Nome:", aluno["nome"], "- Idade:", aluno["idade"], "- Nota:", aluno["nota"])