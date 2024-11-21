import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go

def main():
    try:
        # Solicitar a função do usuário
        funcao_str = input("Digite a função em várias variáveis (por exemplo, '2*x*y**2'): ")

        # Definir as variáveis simbólicas
        x, y = sp.symbols('x y')

        # Converter a string da função para uma expressão sympy
        funcao = sp.sympify(funcao_str)
        print(f"Função simbólica: {funcao}")

        # Calcular as derivadas parciais
        derivada_x = sp.diff(funcao, x)
        derivada_y = sp.diff(funcao, y)
        print(f"Derivada parcial em relação a x: {derivada_x}")
        print(f"Derivada parcial em relação a y: {derivada_y}")

        # Calcular a segunda derivada em relação a x
        segunda_derivada_xx = sp.diff(derivada_x, x)
        print(f"Segunda derivada em relação a x: {segunda_derivada_xx}")

        # Preparar os valores para plotar
        dominio_x = np.linspace(-10, 10, 400)
        dominio_y = np.linspace(-10, 10, 400)
        dominio_x, dominio_y = np.meshgrid(dominio_x, dominio_y)

        # Lambdificar as funções para avaliação numérica
        f_lambdified = sp.lambdify((x, y), funcao, 'numpy')
        derivada_x_func = sp.lambdify((x, y), derivada_x, 'numpy')
        derivada_y_func = sp.lambdify((x, y), derivada_y, 'numpy')

        # Avaliar numericamente as funções
        imagem = f_lambdified(dominio_x, dominio_y)
        derivada_x_imagem = derivada_x_func(dominio_x, dominio_y)
        derivada_y_imagem = derivada_y_func(dominio_x, dominio_y)

        # Plotar a função original com Matplotlib
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        ax.plot_surface(dominio_x, dominio_y, imagem, cmap='viridis')
        ax.set_title('Função Original em 3D')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('f(x, y)')
        plt.show()

        # Função para plotar gráficos interativos com Plotly
        def plot_with_plotly(z_vals, title):
            surface = go.Surface(x=dominio_x, y=dominio_y, z=z_vals)
            layout = go.Layout(title=title, autosize=True)
            fig = go.Figure(data=[surface], layout=layout)
            fig.show()

        # Plotar a função original
        plot_with_plotly(imagem, 'Função Original em 3D')

        # Plotar as derivadas parciais
        plot_with_plotly(derivada_x_imagem, 'Derivada Parcial em relação a x')
        plot_with_plotly(derivada_y_imagem, 'Derivada Parcial em relação a y')

        # Plotar a segunda derivada em relação a x, se não for zero
        if segunda_derivada_xx != 0:
            segunda_derivada_xx_func = sp.lambdify((x, y), segunda_derivada_xx, 'numpy')
            segunda_derivada_xx_imagem = segunda_derivada_xx_func(dominio_x, dominio_y)
            plot_with_plotly(segunda_derivada_xx_imagem, 'Segunda Derivada em relação a x')
        else:
            print("Segunda derivada em relação a x é zero em todos os pontos.")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    main()
