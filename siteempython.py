from flask import Flask, render_template

app = Flask(__name__)
#criar a primeira pagina do site
@app.route("/")
def homepage():
    return(render_template("homepage.html"))

#criando outras paginas
@app.route("/contatos")
def contatos():
    return(render_template("contatos.html"))

@app.route("/usuarios/<nomedousuario>")
def usuarios(nomedousuario):
    return (render_template("usuarios.html", nomedousuario=nomedousuario))

#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)