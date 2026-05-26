from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Banco de dados temporário em memória
tarefas = [
    {"id": 1, "titulo": "Configurar o ambiente Python", "status": "Concluído"},
    {"id": 2, "titulo": "Desenvolver o Front-end e Back-end", "status": "Concluído"},
    {"id": 3, "titulo": "Fazer o deploy da aplicação", "status": "Pendente"}
]

@app.route('/')
def index():
    return render_template('index.html', tarefas=tarefas)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    titulo = request.form.get('titulo')
    if titulo:
        novo_id = len(tarefas) + 1
        tarefas.append({"id": novo_id, "titulo": titulo, "status": "Pendente"})
    return redirect(url_for('index'))

@app.route('/alternar/<int:tarefa_id>')
def alternar(tarefa_id):
    for tarefa in tarefas:
        if tarefa['id'] == tarefa_id:
            tarefa['status'] = "Concluído" if tarefa['status'] == "Pendente" else "Pendente"
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
  
