# %%
import pandas as pd

def transformar_para_dominio_educacional(dataframe):
    """
    Transforma um DataFrame de churn de telecom para um de evasão escolar.

    Args:
        dataframe (pd.DataFrame): O DataFrame original de telecomunicações.

    Returns:
        pd.DataFrame: O DataFrame transformado para o domínio da educação.
    """
    # 1. Mapeamento de Nomes de Colunas
    mapeamento_colunas = {
        'CustomerID': 'Matricula_Aluno',
        'City': 'Cidade',
        'Zip Code': 'CEP',
        'Gender': 'Genero',
        'Senior Citizen': 'Aluno_Bolsista',
        'Partner': 'Responsavel_com_Parceiro',
        'Dependents': 'Aluno_Possui_Dependentes',
        'Tenure Months': 'Meses_na_Escola',
        'Phone Service': 'Participa_Atividade_Extra',
        'Multiple Lines': 'Multiplas_Atividades_Extra',
        'Internet Service': 'Modalidade_Ensino',
        'Online Security': 'Apoio_Psicopedagogico',
        'Online Backup': 'Reforco_Escolar',
        'Device Protection': 'Seguro_Material_Didatico',
        'Tech Support': 'Suporte_TI_Plataforma',
        'Streaming TV': 'Acesso_Aulas_Gravadas',
        'Streaming Movies': 'Acesso_Biblioteca_Digital',
        'Contract': 'Tipo_Contrato_Matricula',
        'Paperless Billing': 'Comunicados_Digitais',
        'Payment Method': 'Forma_Pagamento_Mensalidade',
        'Monthly Charges': 'Valor_Mensalidade',
        'Total Charges': 'Total_Pago_Curso',
        'Churn Label': 'Situacao',
        'Churn Value': 'Desistencia', # 0 = Ativo, 1 = Desistente
        'Churn Score': 'Risco_de_Desistencia',
        'CLTV': 'Valor_Total_Esperado_Aluno'
    }
    df_educ = dataframe.rename(columns=mapeamento_colunas)

    # 2. Mapeamento de Valores dentro das Colunas
    df_educ['Situacao'] = df_educ['Situacao'].map({'Yes': 'Desistente', 'No': 'Ativo'})
    df_educ['Aluno_Bolsista'] = df_educ['Aluno_Bolsista'].map({'Yes': 'Sim', 'No': 'Não'})
    df_educ['Responsavel_com_Parceiro'] = df_educ['Responsavel_com_Parceiro'].map({'Yes': 'Sim', 'No': 'Não'})
    df_educ['Aluno_Possui_Dependentes'] = df_educ['Aluno_Possui_Dependentes'].map({'Yes': 'Sim', 'No': 'Não'})
    df_educ['Participa_Atividade_Extra'] = df_educ['Participa_Atividade_Extra'].map({'Yes': 'Sim', 'No': 'Não'})
    df_educ['Comunicados_Digitais'] = df_educ['Comunicados_Digitais'].map({'Yes': 'Sim', 'No': 'Não'})

    # Mapeamentos mais complexos
    df_educ['Multiplas_Atividades_Extra'] = df_educ['Multiplas_Atividades_Extra'].replace({'No phone service': 'Não se aplica'}).map({'Yes': 'Sim', 'No': 'Não', 'Não se aplica': 'Não participa'})
    
    # Analogia: DSL e Fibra são tipos de serviço. Presencial, Híbrido e EAD são modalidades.
    df_educ['Modalidade_Ensino'] = df_educ['Modalidade_Ensino'].map({'DSL': 'Presencial', 'Fiber optic': 'Híbrido', 'No': 'EAD'})
    
    # Para serviços adicionais, 'No internet service' vira 'Não se aplica' pois dependem da modalidade.
    servicos_adicionais = ['Apoio_Psicopedagogico', 'Reforco_Escolar', 'Seguro_Material_Didatico', 
                           'Suporte_TI_Plataforma', 'Acesso_Aulas_Gravadas', 'Acesso_Biblioteca_Digital']
    for servico in servicos_adicionais:
        df_educ[servico] = df_educ[servico].replace({'No internet service': 'Não se aplica'}).map({'Yes': 'Sim', 'No': 'Não', 'Não se aplica': 'Não se aplica'})

    # Contrato: Mensal, Anual, ou o plano completo do curso.
    df_educ['Tipo_Contrato_Matricula'] = df_educ['Tipo_Contrato_Matricula'].map({
        'Month-to-month': 'Mensal',
        'One year': 'Anual',
        'Two year': 'Plano de Ciclo Completo' # Ex: Ensino Fundamental
    })

    # Forma de pagamento
    df_educ['Forma_Pagamento_Mensalidade'] = df_educ['Forma_Pagamento_Mensalidade'].map({
        'Mailed check': 'Boleto Impresso',
        'Electronic check': 'Boleto Digital',
        'Bank transfer (automatic)': 'Débito Automático',
        'Credit card (automatic)': 'Cartão de Crédito Recorrente'
    })
    
    # Remover colunas que não são mais necessárias ou são redundantes
    # Latitude e Longitude podem ser mantidas para análises geoespaciais
    # df_educ = df_educ.drop(columns=['Latitude', 'Longitude'])

    return df_educ


# Leitura do dataset original
df = pd.read_excel('data/raw/Telco_customer_churn.xlsx')

# Executar a transformação
df_educacional = transformar_para_dominio_educacional(df.copy())

# Exibir o resultado
print("✅ Dataset Transformado para o Domínio Educacional:")
print(df_educacional.head().to_markdown(index=False))

print("\n📊 Informações do Novo DataFrame:")
df_educacional.info()

# Salvar o DataFrame transformado
df_educacional.to_csv('data/raw/educational_churn_dataset.csv', index=False)
print("✅ Dataset transformado salvo em 'data/raw/educational_churn_dataset.csv'")

# %%
