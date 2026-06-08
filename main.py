from flask import Flask, render_template, request

app = Flask(__name__)

# Função para formatar valores em Real (R$)
def moeda(valor):
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        salario = float(request.form["salario"])
        tipo_rescisao = request.form["tipo_rescisao"]

        anos = int(request.form["anos"])
        meses = int(request.form["meses"])

        meses_ano = int(request.form["meses_ano"])

        dias_trabalhados = int(
            request.form["dias_trabalhados"]
        )

        opcao_aviso = request.form["opcao_aviso"]

        total_meses = (anos * 12) + meses

        # Regra dos 15 dias
        if dias_trabalhados >= 15:

            if meses_ano < 12:
                meses_ano += 1

        # Saldo de salário
        valor_dia = salario / 30

        saldo_salario = (
            valor_dia *
            dias_trabalhados
        )

        # 13º proporcional
        decimo_terceiro = (
            salario / 12
        ) * meses_ano

        # Aviso prévio proporcional
        dias_aviso = 30 + (anos * 3)

        if dias_aviso > 90:
            dias_aviso = 90

        valor_aviso = (
            salario / 30
        ) * dias_aviso

        # Pedido de demissão sem cumprir aviso
        if tipo_rescisao == "2":

            if opcao_aviso == "2":
                valor_aviso = -valor_aviso

        # FGTS
        fgts = (
            salario *
            0.08 *
            total_meses
        )

        # Multa FGTS
        if tipo_rescisao == "1":

            multa_fgts = (
                fgts * 0.40
            )

        else:

            multa_fgts = 0

        # Férias vencidas
        periodos_vencidos = (
            total_meses // 12
        )

        ferias_vencidas = (
            periodos_vencidos *
            salario
        )

        total_ferias_vencidas = (
            ferias_vencidas +
            (ferias_vencidas / 3)
        )

        # Férias proporcionais
        meses_restantes = (
            total_meses % 12
        )

        ferias_proporcionais = (
            salario / 12
        ) * meses_restantes

        total_ferias_proporcionais = (
            ferias_proporcionais +
            (ferias_proporcionais / 3)
        )

        # Total da rescisão
        total_rescisao = (

            saldo_salario +

            decimo_terceiro +

            valor_aviso +

            multa_fgts +

            total_ferias_vencidas +

            total_ferias_proporcionais
        )

        # Status do aviso
        status_aviso = (
            "Cumpriu"
            if opcao_aviso == "1"
            else "Não cumpriu"
        )

        resultado = {

            "salario": moeda(salario),

            "anos": anos,

            "meses_restantes": meses_restantes,

            "saldo_salario":
            moeda(saldo_salario),

            "decimo_terceiro":
            moeda(decimo_terceiro),

            "status_aviso":
            status_aviso,

            "dias_aviso":
            dias_aviso,

            "valor_aviso":
            moeda(valor_aviso),

            "fgts":
            moeda(fgts),

            "multa_fgts":
            moeda(multa_fgts),

            "periodos_vencidos":
            periodos_vencidos,

            "ferias_vencidas":
            moeda(total_ferias_vencidas),

            "ferias_proporcionais":
            moeda(total_ferias_proporcionais),

            "total_rescisao":
            moeda(total_rescisao)
        }

        return render_template(
            "index.html",
            resultado=resultado
        )

    return render_template(
        "index.html",
        resultado=None
    )


if __name__ == "__main__":
    app.run(debug=True)