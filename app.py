from flask import Flask, request, render_template
import sympy as sp

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    solution = None
    if request.method == 'POST':
        equation = request.form['equation']
        x = sp.symbols('x')
        try:
            # Dividir a equação em lado esquerdo e direito
            lhs, rhs = equation.split('=')
            lhs_expr = sp.sympify(lhs)
            rhs_expr = sp.sympify(rhs)
            # Criar a equação simbólica
            expr = sp.Eq(lhs_expr, rhs_expr)
            # Resolver a equação
            solution = sp.solve(expr, x)
        except Exception as e:
            solution = f"Erro ao resolver a equação: {e}"
    return render_template('index.html', solution=solution)

if __name__ == '__main__':
    app.run(debug=True)
