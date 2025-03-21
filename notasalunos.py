soma = 0
boletim = {}
nome = []
media = []
desempenho_aluno = []
materia = ["Portugues", "Matematica", "Fisica", "Historia", "Programacao"]
x = int(input("Quantos alunos tem na sala?: "))
for p in range(0, x):
    desempenho = tuple()
    desempenho_aluno = []
    nota = []
    nome = (input(f"Digite o nome do {p+1}º aluno: "))
    for m in materia:
        print(m)
        for bimestre in range(1, 5):
            nota.append(int(input(f"{bimestre}º bimestre: ")))
        nota.append(sum(nota) / 4)
        desempenho = m, nota
        desempenho_aluno.append(desempenho)
        nota = []
        desempenho = tuple()
    boletim[nome] = desempenho_aluno

with open("notas.txt","w") as arquivo:
    arquivo.write(f"{boletim}")