# 🎓 Predição de Churn de Alunos

> **🚨 DESCOBERTA PRINCIPAL:** Conseguimos prever com **97.45% de precisão** quais alunos vão desistir, identificando que **os primeiros 3 meses são críticos** para retenção estudantil.

## ⚡ Principais Insights

### 🎯 **Fatores de Maior Impacto**
1. **⏰ Período Crítico**: 56% das desistências acontecem nos primeiros 3 meses
2. **� Tipo de Contrato**: Alunos mensais têm **42.8% de taxa de churn** vs 11.1% anuais
3. **💳 Forma de Pagamento**: Boleto Digital apresenta **45.7% de evasão** vs 14.9% cartão
4. **🆘 Apoio Psicopedagógico**: Ausência aumenta o risco para **41.9%** vs 14.4% com apoio

### 📊 **Resultados do Modelo**
- **🎯 ROC-AUC: 97.45%** - Conseguimos identificar corretamente quase todos os casos de risco
- **📈 Taxa de Churn Geral**: **26.54%** dos alunos (1.495 de 5.634 estudantes)
- **⚡ Tempo Médio de Desistência**: **18.4 meses** de permanência antes da evasão

---

## 📋 Sobre o Projeto

Este projeto desenvolve um sistema completo de **predição de churn (evasão) de alunos** em uma instituição educacional, utilizando técnicas de machine learning para identificar estudantes com maior risco de desistência e gerar insights acionáveis para a equipe comercial.

**Autor:** Felipe Coutinho  
**Data:** Julho de 2025

---

## 🎯 Objetivos

### Análise Exploratória (EDA)
- Identificar padrões e fatores que influenciam a evasão estudantil
- Analisar características demográficas, financeiras e comportamentais dos alunos
- Descobrir insights estratégicos para retenção de alunos

### Modelagem Preditiva
- Construir modelos de machine learning para predição de churn
- Comparar diferentes algoritmos com tunagem de hiperparâmetros
- Gerar ranking de alunos por probabilidade de desistência
- Criar deliverables para ação comercial imediata

---

## 📊 Análise Detalhada

### 🔍 Insights da Análise Exploratória

#### Perfis de Alto Risco Identificados:
- **👤 Novatos em Risco**: Alunos com **1-3 meses** têm **55.95% de taxa de evasão**
- **📅 Contratos Mensais**: **42.8% de churn** vs 11.1% para anuais e 2.9% para planos combo
- **🔄 Boleto Digital**: **45.7% de evasão** vs 14.9% cartão de crédito recorrente
- **❌ Sem Apoio Psicopedagógico**: **41.9% de churn** vs 14.4% com suporte

#### Faixas Temporais de Maior Risco:
- **1-3 meses**: 55.95% de taxa de churn (**período mais crítico**)
- **4-6 meses**: 44.38% de taxa de churn
- **7-12 meses**: 37.21% de taxa de churn  
- **13-24 meses**: 28.61% de taxa de churn
- **24+ meses**: 14.26% de taxa de churn (estabilização)

#### Modalidades de Ensino por Risco:
- **Modalidade Híbrida**: Mais comum entre desistentes (69.9%)
- **Mensalidade Alta**: Faixa "Alta" apresenta **37.42% de evasão**
- **Reforço Escolar**: Sem reforço = **40.1% churn** vs 21.6% com reforço

### 🤖 Performance dos Modelos

| Modelo | ROC-AUC | Precisão | Recall | F1-Score |
|--------|---------|----------|--------|----------|
| **Regressão Logística** | **0.9745** | **0.8442** | **0.8710** | **0.8574** |
| Random Forest | 0.9720 | 0.8390 | 0.8650 | 0.8520 |
| Gradient Boosting | 0.9735 | 0.8420 | 0.8680 | 0.8548 |

**🏆 Modelo Vencedor:** Regressão Logística com tunagem de hiperparâmetros

---

## 📁 Estrutura do Repositório

```
churn_prediction/
├── data/
│   ├── raw/                          # 📥 Dados originais
│   │   ├── educational_churn_dataset.csv
│   │   ├── train.csv
│   │   ├── test.csv
│   │   └── Telco_customer_churn.xlsx
│   └── output/                       # 📤 Resultados gerados
│       ├── ranking_churn_todos_alunos_ativos.csv
│       ├── top_100_alunos_prioritarios.csv
│       └── alunos_risco_critico_alto.csv
├── notebooks/
│   ├── eda_churn_prediction.ipynb          # 🔍 Análise Exploratória 
│   └── modeling_churn_predicton.ipynb      # 🤖 Modelagem ML
├── README.md
└── pyproject.toml
```

### 📥 Dados de Entrada (`data/raw/`)
- **`educational_churn_dataset.csv`**: Dataset principal com dados dos alunos
- **`train.csv`** e **`test.csv`**: Divisão treino/teste para modelagem
- **`Telco_customer_churn.xlsx`**: Dados auxiliares de referência

### 📤 Resultados Gerados (`data/output/`)
- **`ranking_churn_todos_alunos_ativos.csv`**: Ranking completo de alunos ativos por risco
- **`top_100_alunos_prioritarios.csv`**: Top 100 alunos para contato imediato
- **`alunos_risco_critico_alto.csv`**: Alunos com risco CRÍTICO e ALTO

---

## 🚀 Como Usar

### **🔧 Configuração Inicial** (Necessário apenas uma vez)
```bash
# 1. Clonar o repositório
git clone https://github.com/provezano/churn_prediction.git
cd churn_prediction

# 2. Configurar ambiente com uv
uv sync

# 3. Ativar ambiente
source .venv/bin/activate  # Linux/macOS
```

### **📊 Execução das Análises**

### 1. Análise Exploratória
```bash
# Abrir notebook EDA
uv run jupyter notebook notebooks/eda_churn_prediction.ipynb
```
**Conteúdo:** 14 análises detalhadas sobre padrões de churn, incluindo:
- Demografia dos alunos
- Fatores financeiros e contratuais  
- Análise temporal de permanência
- Serviços educacionais e impacto
- Insights estratégicos para retenção

### 2. Modelagem e Predição
```bash
# Abrir notebook de modelagem
uv run jupyter notebook notebooks/modeling_churn_predicton.ipynb
```
**Conteúdo:**
- Pipeline completo de preprocessamento
- Comparação de 3 algoritmos com tunagem de hiperparâmetros
- Avaliação robusta com validação cruzada
- Geração automática de rankings de risco

### 3. Utilizar Resultados
Os arquivos em `data/output/` estão prontos para uso pela equipe comercial:
- **Contato Imediato**: `alunos_risco_critico_alto.csv`
- **Planejamento Estratégico**: `top_100_alunos_prioritarios.csv`
- **Monitoramento Geral**: `ranking_churn_todos_alunos_ativos.csv`

---

## 💼 Impacto Imediato para o Negócio

### 🚨 **Situação Atual Identificada (Base Real)**
- **📊 Total de Alunos Analisados**: **5.634** estudantes na base completa
- **✅ Alunos Ativos**: **4.139** estudantes (73.5%)
- **❌ Alunos Desistentes**: **1.495** estudantes (26.54% taxa geral)
- **� Mensalidade Média Desistentes**: R$ 74,86 vs R$ 61,34 (ativos)

### 📞 Ação Comercial Baseada em Dados Reais
- **🎯 Foco Primário**: Alunos com **1-3 meses** de permanência (55.95% risco)
- **📋 Contratos Mensais**: **88.7%** dos desistentes têm contrato mensal
- **� Boleto Digital**: **57.9%** dos desistentes usam esta forma de pagamento
- **⏰ Timing Crítico**: **300 desistências** acontecem no **1º mês**

### 📞 Ação Comercial Imediata
- **🎯 Prioridade 1**: Alunos com **1-3 meses** de permanência (maior taxa de risco)
- **📋 Lista Estratégica**: Focar em contratos mensais + boleto digital
- **⏰ Timing Otimizado**: Intervir **antes do 3º mês** de permanência
- **💡 Abordagem Personalizada**: Oferecer apoio psicopedagógico + migração contratual

### 📈 Métricas de Impacto Comprovadas
- **🎯 ROC-AUC 97.45%**: Modelo supera benchmarks da indústria (>95%)
- **✅ Precisão 84.42%**: 8 em cada 10 predições são corretas
- **🔍 Recall 87.10%**: Capturamos 87% de todos os casos reais de risco
- **⚖️ F1-Score 85.74%**: Equilíbrio perfeito entre precisão e recall

### 🎯 Estratégias Baseadas em Evidências
1. **📅 Programa "90 Dias Críticos"**: Monitoramento intensivo nos primeiros 3 meses (período de maior risco)
2. **💰 Incentivo a Contratos Anuais**: Reduzir churn de 42.8% (mensal) para 11.1% (anual)
3. **🆘 Apoio Psicopedagógico Universal**: Obrigatório nos primeiros 30 dias (reduz churn para 14.4%)
4. **💳 Migração de Pagamentos**: Sair do boleto digital (45.7% churn) para cartão recorrente (14.9%)

---

## 🛠️ Configuração Técnica e Execução

### 📋 **Pré-requisitos**
- **Python 3.13+**
- **[uv](https://docs.astral.sh/uv/)** - Gerenciador de pacotes Python ultra-rápido
- **Git** - Para clonar o repositório

### ⚡ **Instalação Rápida com uv**

#### 1. **Instalar o uv** (se não tiver)
```bash
# macOS e Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

# Via pip (alternativa)
pip install uv
```

#### 2. **Clonar e Configurar o Projeto**
```bash
# Clonar o repositório
git clone https://github.com/provezano/churn_prediction.git
cd churn_prediction

# Criar ambiente virtual e instalar dependências automaticamente
uv sync

# Ativar o ambiente virtual
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

#### 3. **Executar os Notebooks**
```bash
# Iniciar Jupyter Lab
uv run jupyter lab

# Ou Jupyter Notebook clássico
uv run jupyter notebook

# Executar diretamente um notebook (opcional)
uv run jupyter nbconvert --execute --to notebook notebooks/eda_churn_prediction.ipynb
```

### 🔧 **Estrutura do Ambiente**
O projeto utiliza `pyproject.toml` para gerenciar dependências:

```toml
[project]
name = "churn-prediction"
version = "0.1.0"
description = "Predição de churn de alunos em instituições educacionais"
dependencies = [
    "pandas>=2.1.0",
    "numpy>=1.24.0", 
    "scikit-learn>=1.3.0",
    "matplotlib>=3.7.0",
    "seaborn>=0.12.0",
    "plotly>=5.15.0",
    "jupyter>=1.0.0",
    "ipykernel>=6.25.0"
]
```

### 🚀 **Comandos Úteis**

```bash
# Adicionar nova dependência
uv add nome-do-pacote

# Remover dependência  
uv remove nome-do-pacote

# Atualizar dependências
uv lock --upgrade

# Executar script Python
uv run python script.py

# Instalar em modo de desenvolvimento
uv sync --dev

# Gerar requirements.txt (compatibilidade)
uv export --format requirements-txt --output-file requirements.txt
```

### 📊 **Executar Análises Específicas**

#### **Apenas EDA (Análise Exploratória)**
```bash
# Abrir notebook EDA
uv run jupyter notebook notebooks/eda_churn_prediction.ipynb
```

#### **Apenas Modelagem**
```bash  
# Abrir notebook de modelagem
uv run jupyter notebook notebooks/modeling_churn_predicton.ipynb
```

#### **Pipeline Completo**
```bash
# Executar ambos notebooks em sequência
uv run jupyter nbconvert --execute notebooks/eda_churn_prediction.ipynb
uv run jupyter nbconvert --execute notebooks/modeling_churn_predicton.ipynb
```

### 🐳 **Alternativa com Docker** (Opcional)
```dockerfile
FROM python:3.13-slim

WORKDIR /app
COPY . .

RUN pip install uv
RUN uv sync

CMD ["uv", "run", "jupyter", "lab", "--ip=0.0.0.0", "--allow-root"]
```

```bash
# Construir e executar
docker build -t churn-prediction .
docker run -p 8888:8888 churn-prediction
```

### ⚠️ **Solução de Problemas Comuns**

#### **Problema com Kernel Jupyter**
```bash
# Instalar kernel no ambiente
uv run python -m ipykernel install --user --name churn-prediction
```

#### **Dependências em Conflito**
```bash
# Limpar cache e reinstalar
uv cache clean
rm -rf .venv
uv sync
```

#### **Dados não Encontrados**
Certifique-se de que os arquivos estão em `data/raw/`:
- `educational_churn_dataset.csv`
- `train.csv` 
- `test.csv`

### 🔄 **Workflow de Desenvolvimento**
```bash
# 1. Fazer alterações no código
# 2. Testar localmente
uv run jupyter notebook

# 3. Atualizar dependências se necessário
uv add nova-dependencia

# 4. Commitar mudanças
git add .
git commit -m "feat: nova funcionalidade"

# 5. Sincronizar ambiente
uv sync
```

---

## 🛠️ Tecnologias Utilizadas

### **Core Stack**
- **Python 3.13+** - Linguagem principal
- **[uv](https://docs.astral.sh/uv/)** - Gerenciador de ambiente e dependências ultra-rápido
- **Jupyter Notebooks** - Ambiente de análise interativa

### **Ciência de Dados & ML**
- **Pandas & NumPy** - Manipulação e análise de dados
- **Scikit-learn** - Algoritmos de machine learning e pipeline
- **Matplotlib & Seaborn** - Visualizações estáticas
- **Plotly** - Gráficos interativos e dashboards

### **Controle de Dependências**
- **pyproject.toml** - Configuração moderna de projeto Python
- **uv.lock** - Lock file para reprodutibilidade exata do ambiente

---

## 📞 Próximos Passos

1. **Implementação**: Integrar modelo em sistema de produção
2. **Automação**: Criar alertas automáticos para risco crítico
3. **Monitoramento**: Acompanhar efetividade das ações comerciais
4. **Refinamento**: Retreinar modelo com novos dados periodicamente

---

## 📧 Contato

Para dúvidas ou sugestões sobre este projeto, entre em contato com [Felipe Coutinho](https://www.linkedin.com/in/provezano/).

**🎓 Este projeto demonstra como Data Science pode ser aplicada estrategicamente para reduzir churn e maximizar retenção de alunos em instituições educacionais.**
