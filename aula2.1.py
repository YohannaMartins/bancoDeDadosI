import pandas as pd

# Dados de exemplo
data = {
    'ID': [1, 2, 3, 4, 5],
    'Nome': ['Alice Silva', 'Bruno Souza', 'Carlos Lima', 'Diana Mendes', 'Eva Costa'],
    'Ano': [1, 2, 1, 3, 2],
    'Nota': [8.5, 6.0, 9.0, 7.5, 5.5],
    'PNome': ['Alice', 'Bruno', 'Carlos', 'Diana', 'Eva'],
    'UNome': ['Silva', 'Souza', 'Lima', 'Mendes', 'Costa'],
    'Nome_Professor': ['Prof. A', 'Prof. B', 'Prof. A', 'Prof. C', 'Prof. B']
}

df = pd.DataFrame(data)

aprovados = df[df['Nota'] > 7.0]
print(aprovados)

primeiro_ano_acima_8 = df[(df['Ano'] == 1) & (df['Nota'] >= 8.0)]
print(primeiro_ano_acima_8)

nomes_notas = df[['Nome', 'Nota']]
print(nomes_notas)

professores_data = {
    'Nome_Professor': ['Prof. A', 'Prof. B', 'Prof. C'],
    'PNome': ['Ana', 'Bruno', 'Carlos'],
    'UNome': ['Almeida', 'Barros', 'Cardoso']
}

professores = pd.DataFrame(professores_data)
professores_table = professores[['PNome', 'UNome']]
print(professores_table)

alunos_table = df[['PNome', 'UNome']].drop_duplicates()
print(alunos_table)

uniao = pd.concat([alunos_table, professores_table]).drop_duplicates().reset_index(drop=True)
print(uniao)

intersecao = pd.merge(alunos_table, professores_table, how='inner', on=['PNome', 'UNome'])
print(intersecao)

diferenca = pd.concat([alunos_table, professores_table]).drop_duplicates(keep=False)
print(diferenca)

