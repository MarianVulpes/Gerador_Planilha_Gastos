import pandas as pd

def main():
    categorias = ['Moradia', 'Alimentação', 'Transporte', 'Saúde', 'Educação', 'Entretenimento', 'Despesas Pessoais']
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    gastos = pd.DataFrame(index=meses, columns=categorias)

    moradia = pd.DataFrame(index=meses, columns=['Aluguel', 'Contas de serviços públicos', 'Internet e TV a cabo'])
    alimentacao = pd.DataFrame(index=meses, columns=['Compras de supermercado', 'Refeições fora de casa'])
    transporte = pd.DataFrame(index=meses, columns=['Combustível', 'UBER', 'Manutenção do Veículo', 'Parcelas do Veículo', 'IPVA', 'Licenciamento'])
    saude = pd.DataFrame(index=meses, columns=['Consultas Médicas', 'Medicamentos'])
    educacao = pd.DataFrame(index=meses, columns=['Material Escolar', 'Cursos Extracurriculares'])
    entretenimento = pd.DataFrame(index=meses, columns=['Shows e Eventos'])
    despesas_pessoais = pd.DataFrame(index=meses, columns=['Roupas', 'Calçados', 'Cosméticos', 'Presentes', 'Academia'])

    with pd.ExcelWriter('gastos.xlsx') as writer:
        gastos.to_excel(writer, sheet_name='Gastos')
        moradia.to_excel(writer, sheet_name='Moradia')
        alimentacao.to_excel(writer, sheet_name='Alimentação')
        transporte.to_excel(writer, sheet_name='Transporte')
        saude.to_excel(writer, sheet_name='Saúde')
        educacao.to_excel(writer, sheet_name='Educação')
        entretenimento.to_excel(writer, sheet_name='Entretenimento')
        despesas_pessoais.to_excel(writer, sheet_name='Despesas Pessoais')

if __name__ == '__main__':
    main()
    
