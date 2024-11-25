import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go

def main():
    try:
        # Solicitar a função do usuário
        funcao_str = input("Digite a função (por exemplo, '2*x*y**2' ou 'x**2 + y**2 + z**2'): ")

        # Solicitar as variáveis do usuário
        variaveis_str = input("Digite as variáveis separadas por espaço (por exemplo, 'x y' ou 'x y z'): ")
        variaveis = sp.symbols(variaveis_str)
        
        # Converter a string da função para uma expressão sympy
        funcao = sp.sympify(funcao_str)
        print(f"Função simbólica: {funcao}")

        # Calcular as derivadas parciais
        derivadas = [sp.diff(funcao, var) for var in variaveis]
        for var, deriv in zip(variaveis, derivadas):
            print(f"Derivada parcial em relação a {var}: {deriv}")

        # Calcular derivadas de ordem superior
        segundas_derivadas = [sp.diff(deriv, var) for deriv in derivadas for var in variaveis]
        terceiras_derivadas = [sp.diff(seg_deriv, var) for seg_deriv in segundas_derivadas for var in variaveis]
        
        for var, seg_deriv in zip(variaveis, segundas_derivadas):
            print(f"Segunda derivada em relação a {var}: {seg_deriv}")
        for var, ter_deriv in zip(variaveis, terceiras_derivadas):
            print(f"Terceira derivada em relação a {var}: {ter_deriv}")

        # Definir o domínio
        dominio = np.linspace(-10, 10, 400)
        dominios = np.meshgrid(*[dominio]*len(variaveis))
        print(f"Domínio: {variaveis_str} = [-10, 10]")

        # Converter a função para uma função numérica
        funcao_num = sp.lambdify(variaveis, funcao, 'numpy')
        imagem = funcao_num(*dominios)

        # Calcular a imagem da função
        imagem_min = np.min(imagem)
        imagem_max = np.max(imagem)
        print(f"Imagem da função: [{imagem_min}, {imagem_max}]")

        # Função para plotar com plotly
        def plot_with_plotly(z_vals, title):
            surface = go.Surface(x=dominios[0], y=dominios[1], z=z_vals)
            layout = go.Layout(title=title, autosize=True)
            fig = go.Figure(data=[surface], layout=layout)
            fig.show()

        # Plotar a função original
        plot_with_plotly(imagem, 'Função Original em 3D')

        # Plotar as derivadas parciais
        derivadas_funcs = [sp.lambdify(variaveis, deriv, 'numpy') for deriv in derivadas]
        derivadas_imagens = [deriv_func(*dominios) for deriv_func in derivadas_funcs]
        for var, deriv_imagem in zip(variaveis, derivadas_imagens):
            plot_with_plotly(deriv_imagem, f'Derivada Parcial em relação a {var}')

        # Plotar as segundas derivadas
        segundas_derivadas_funcs = [sp.lambdify(variaveis, seg_deriv, 'numpy') for seg_deriv in segundas_derivadas]
        segundas_derivadas_imagens = [seg_deriv_func(*dominios) for seg_deriv_func in segundas_derivadas_funcs]
        for var, seg_deriv_imagem in zip(variaveis, segundas_derivadas_imagens):
            plot_with_plotly(seg_deriv_imagem, f'Segunda Derivada em relação a {var}')

        # Plotar as terceiras derivadas
        terceiras_derivadas_funcs = [sp.lambdify(variaveis, ter_deriv, 'numpy') for ter_deriv in terceiras_derivadas]
        terceiras_derivadas_imagens = [ter_deriv_func(*dominios) for ter_deriv_func in terceiras_derivadas_funcs]
        for var, ter_deriv_imagem in zip(variaveis, terceiras_derivadas_imagens):
            plot_with_plotly(ter_deriv_imagem, f'Terceira Derivada em relação a {var}')

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()