# Previsão de Preços de Ativos com LSTM (Deep Learning)

**AVISO DE ISENÇÃO DE RESPONSABILIDADE:**  
Este projeto tem finalidade estritamente educacional e de aprendizado.  
Os resultados e previsões gerados não devem ser utilizados como conselhos financeiros ou recomendações de investimento.  
Modelos de Machine Learning possuem limitações e riscos significativos.

---

## Objetivo do Projeto

Este projeto demonstra a implementação de modelos de **Deep Learning** para a previsão de **séries temporais financeiras**.  
O objetivo é projetar o comportamento de um ativo para os **próximos 30 dias**, utilizando **redes neurais recorrentes (LSTM)**.

---

## Diferenciais Técnicos e Soluções

Diferente de implementações básicas, este projeto foca na **robustez estatística** para evitar erros comuns em previsões financeiras.

### Estacionariedade com Log-Returns

O modelo treina sobre **variações percentuais logarítmicas (log-returns)** em vez de preços brutos.  
Isso evita que a rede neural apresente instabilidades quando o preço atinge escalas não observadas no treinamento.

### Previsão Recursiva Dinâmica

Implementação de um loop que projeta **um dia por vez**.  
A cada passo, indicadores técnicos como **RSI** e **Médias Móveis (MA7 / MA21)** são recalculados matematicamente com base na previsão anterior.

### Blindagem contra Data Leakage

O escalonamento dos dados (**MinMaxScaler**) é ajustado **exclusivamente com os dados de treino**, garantindo que informações do futuro não contaminem o aprendizado do modelo.

---

## Arquitetura do Modelo

O projeto utiliza uma arquitetura **LSTM empilhada**, com camadas de **Dropout** para mitigação de **overfitting**.

---

## Tecnologias Utilizadas

- **Python 3**
- **TensorFlow / Keras** — construção e treinamento da rede neural
- **yFinance** — coleta de dados reais do mercado
- **Pandas & NumPy** — manipulação e tratamento de dados
- **Matplotlib** — visualização de históricos e projeções
- **Scikit-learn** — pré-processamento e normalização

---

## Como Usar

### 1. Preparação

Certifique-se de ter um ambiente **Jupyter Notebook** ou **Google Colab** pronto para uso.

### 2. Instalação das Dependências

Execute o comando abaixo no terminal ou em uma célula do notebook:

pip install tensorflow yfinance pandas numpy matplotlib scikit-learn

### 3. Execução

Baixe o arquivo .ipynb mais recente deste repositório.

Execute todas as células sequencialmente.

### 4. Personalização (Troca de Ativo)

Para analisar uma empresa diferente, altere a variável ticker no início do código. Você pode usar códigos da NASDAQ, NYSE ou B3 (ex: PETR4.SA para Petrobras).

## Resultados

Graças ao uso de Log-Returns, o modelo demonstra uma continuidade orgânica entre o histórico real e a projeção futura. Essa abordagem mitiga o erro de propagação comum em modelos recursivos simples, gerando uma curva de previsão estatisticamente mais estável e visualmente integrada.

👤 Autor
Lorenzo Nakayama Machado

Graduando em Ciência da Computação pela Pontifícia Universidade Católica do Paraná (PUCPR).

Interesse em IA, Ciência de Dados e Desenvolvimento Python.
