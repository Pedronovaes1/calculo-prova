# Documentação do Projeto de Calculadora

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados em sua máquina:

- **Python**: necessário para executar o projeto.
- **Pip**: usado para instalar as bibliotecas do projeto.
- **Bibliotecas necessárias**: 
  - Sympy
  - Numpy
  - Matplotlib
  - Plotly

## Passos para Rodar o Código

### 1. Criar um Ambiente Virtual
Para gerenciar as dependências do projeto, crie e ative um ambiente virtual:

```bash
# Criar o ambiente virtual
python -m venv venv

# Ativar o ambiente virtual (Windows)
.\venv\Scripts\activate

# Ativar o ambiente virtual (Linux/Mac)
source venv/bin/activate
```
2. Instalar as Dependências
Com o ambiente virtual ativado, instale as bibliotecas listadas no arquivo requirements.txt:

```bash
pip install -r requirements.txt
```
3. Executar o Código
Execute o programa principal com o ambiente virtual ativado:
```bash
python main.py
```

## Interação com a Calculadora

Quando o programa estiver em execução, siga as instruções exibidas no terminal:

Digite a função: Insira a função matemática que deseja calcular. Exemplo:
```bash
2*x*y**2
```
Digite as variáveis: Insira as variáveis separadas por espaço. Exemplo:
```bash
x y
```
O programa calculará automaticamente:

- Derivadas parciais
- Segundas derivadas
- Terceiras derivadas

Além disso, gráficos serão gerados e exibidos em janelas separadas utilizando a biblioteca Plotly.
