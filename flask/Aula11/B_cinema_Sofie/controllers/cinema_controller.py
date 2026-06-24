from flask import Blueprint, redirect, render_template, request, url_for
from models import Filme, Sala, Sessao, db

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
        filme_id = request.form.get("filme_id", "").strip()
        sala_id = request.form.get("sala_id", "").strip()
        data_hora = request.form.get("data_hora", "").strip('%Y-%m-%DT%H:%M')
        preco = request.form.get("preco", "").strip()
        if not filme_id or sala_id:
            render_template(
            "cinema/formulario_sessao.html",
            titulo="Selecione um filme e uma sala.",
            erro="Filme e sala são obrigatórios.",
            filme_id=filme_id,
            sala_id=sala_id,
            data_hora=data_hora,
            preco=preco)
        Sessao.adicionar(filme_id, sala_id, data_hora, preco)
        return redirect(url_for("cinema.listar"))

    return render_template(
        "cinema/formulario_sessao.html",
        filmes=filmes,
        salas=salas,
    )
