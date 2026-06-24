from flask import Blueprint, redirect, render_template, request, url_for
from models import Filme, Sala, Sessao, db
from datetime import datetime

cinema_bp = Blueprint("cinema", __name__, url_prefix="/cinema")

@cinema_bp.route("/")
def index():
    sessoes = Sessao.listar_com_detalhes()
    return render_template("cinema/lista_sessoes.html", sessoes=sessoes)


@cinema_bp.route("/sessao/cadastrar", methods=["GET", "POST"])
def cadastrar_sessao():
    filmes = Filme.listar()
    salas = Sala.listar()

    if request.method == "POST":
        sessao = Sessao(filme_id = request.form.get("filme_id", "").strip(),
        sala_id = request.form.get("sala_id", "").strip(),
        data_hora = request.form.get("data_hora", "").strip('%Y-%m-%DT%H:%M'),
        preco = request.form.get("preco", "").strip())
        db.session.add(sessao)
        db.session.commit()
        return redirect(url_for("sessao.listar"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
