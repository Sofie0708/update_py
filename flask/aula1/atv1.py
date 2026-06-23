from flask import Flask

app = Flask(__name__)

@app.route('/')
def vazio():
    return ''

@app.route('/decorator')
def decorator():
    return 'Um decorator em Python é uma função que envolve outra função, permitindo modificar ou estender seu comportamento sem alterar seu código original. Eles servem para reutilizar códigos (como logging, autenticação, timing) de forma elegante e limpa usando a sintaxe @nome_do_decorator. No Flask, são cruciais para definir rotas (@app.route).'

if __name__ == '__main__':
    app.run(debug=True)