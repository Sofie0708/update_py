from flask import Flask

app = Flask(__name__)

@app.route('/')
def curriculo():
    return '''
        <!DOCTYPE html>
        <html lang="pt-BR">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Currículo</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    line-height: 1.6;
                    margin: 0;
                    padding: 0;
                    background-color: #f4f4f9;
                    color: #333;
                }

                .container {
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background: #fff;
                    border-radius: 8px;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
                }

                header {
                    text-align: center;
                    margin-bottom: 20px;
                }

                header h1 {
                    margin: 0;
                    color: #007BFF;
                }

                header p {
                    margin: 5px 0;
                    font-size: 1em;
                    color: #555;
                }

                h2 {
                    color: #007BFF;
                    border-bottom: 2px solid #007BFF;
                    padding-bottom: 5px;
                }

                ul {
                    list-style: none;
                    padding: 0;
                }

                ul li {
                    margin-bottom: 10px;
                }

                ul li strong {
                    color: #333;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <header>
                    <h1>Sofie Cirino</h1>
                    <p>Email: sofiecirino@gmail.com | Telefone: (11) 99999-9999</p>
                </header>

                <section>
                    <h2>Informações Pessoais</h2>
                    <ul>
                        <li><strong>Nome:</strong> Sofie Cirino e Castro</li>
                        <li><strong>Email:</strong> sofiecirino@gmail.com</li>
                        <li><strong>Telefone:</strong> (11) 99999-9999</li>
                    </ul>
                </section>

                <section>
                    <h2>Experiência</h2>
                    <ul>
                        <li><strong>Escolaridade:</strong> Cotemig - Tecnico</li>
                        <li><strong>Período:</strong> Jan 2025 - Presente</li>
                    </ul>
                </section>
            </div>
        </body>
        </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)