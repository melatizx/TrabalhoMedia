import ast

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

boletim_lido = ast.literal_eval(conteudo)

pagina = open("notas.html", "w", encoding="utf-8")
pagina.write("""
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scaled=1.0">
        <title>Desempenho Final Dos Alunos</title>
        <style rel="stylesheet">
            h1{
                text-align: center;
                font-size: 50px;
            }
            table{
                width: 70%;
                text-align: left;
                border-collapse: collapse;
                margin: 0 auto;
            }
            th, td{
                padding: 15px;
                font-size: 25px;
            }
            .nome{
                text-align: center;
                font-size: 30px;
            }
            .auxilio{
                text-align: center;
                font-size: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Notas dos alunos do 3ºDS - JIM</h1>
        <p class="auxilio">Para localizar mais rapidamente, utilize o comando 'CTRL + F' e pesquise pelo seu nome</p>
        <table border="1">
""")
for aluno, desempenho in boletim_lido.items():
    pagina.write(f"""
            <tr>
                <th class="nome" colspan="6">{aluno}</th>
            </tr>
            <tr>
                <th>Materia</th>
                <th>1ºB</th>
                <th>2ºB</th>
                <th>3ºB</th>
                <th>4ºB</th>
                <th>Media</th>
            </tr>
        """)
    for materia, notas in desempenho:
        pagina.write(f"""
                <tr>
                    <td>{materia}</td>
                    <td>{notas[0]}</td>
                    <td>{notas[1]}</td>
                    <td>{notas[2]}</td>
                    <td>{notas[3]}</td>
                    <td>{notas[4]}</td>
                </tr>
            """)    
pagina.write("""
                    </tr>
            </table>
        </body>
    </html>

    """)    
pagina.close



