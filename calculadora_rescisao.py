# =========================================
# CALCULADORA DE RESCISÃO CLT
# Versão Acadêmica Aprimorada
# =========================================

# Salário
salario = float(input("Digite o salário do trabalhador: R$ "))

# =========================================
# TIPO DE RESCISÃO
# =========================================
print("\nTipo de rescisão:")
print("1 - Demissão sem justa causa")
print("2 - Pedido de demissão")

tipo_rescisao = input("Escolha uma opção: ")

# =========================================
# TEMPO TRABALHADO
# =========================================
print("\nComo deseja informar o tempo trabalhado?")
print("1 - Em anos")
print("2 - Em meses")

tipo_tempo = input("Escolha uma opção: ")

if tipo_tempo == "1":

    anos = int(input("Quantos anos trabalhou? "))
    meses = int(input("Meses adicionais: "))

    total_meses = (anos * 12) + meses

else:

    total_meses = int(
        input("Quantos meses trabalhou? ")
    )

    anos = total_meses // 12
    meses = total_meses % 12

# =========================================
# MESES PARA 13º
# =========================================
meses_ano = int(
    input(
        "\nMeses trabalhados no ano atual: "
    )
)

# =========================================
# DIAS TRABALHADOS NO MÊS DA RESCISÃO
# =========================================
dias_trabalhados = int(
    input(
        "Dias trabalhados no mês da rescisão: "
    )
)

# =========================================
# REGRA DOS 15 DIAS
# =========================================
if dias_trabalhados >= 15:

    if meses_ano < 12:
        meses_ano += 1

# =========================================
# AVISO PRÉVIO
# =========================================
print("\nAviso prévio:")
print("1 - Cumpriu")
print("2 - Não cumpriu")

opcao_aviso = input("Escolha: ")

# =========================================
# SALDO DE SALÁRIO
# =========================================
valor_dia = salario / 30

saldo_salario = (
    valor_dia *
    dias_trabalhados
)

# =========================================
# DÉCIMO TERCEIRO
# =========================================
decimo_terceiro = (
    salario / 12
) * meses_ano

# =========================================
# AVISO PRÉVIO PROPORCIONAL
# =========================================
dias_aviso = 30 + (anos * 3)

if dias_aviso > 90:
    dias_aviso = 90

valor_aviso = (
    salario / 30
) * dias_aviso

# Pedido de demissão
if tipo_rescisao == "2":

    if opcao_aviso == "2":
        valor_aviso = -valor_aviso

# Sem justa causa
else:

    if opcao_aviso == "1":
        valor_aviso = valor_aviso

# =========================================
# FGTS ACUMULADO
# =========================================
fgts = (
    salario *
    0.08 *
    total_meses
)

# =========================================
# MULTA FGTS
# =========================================
if tipo_rescisao == "1":

    multa_fgts = (
        fgts * 0.40
    )

else:

    multa_fgts = 0

# =========================================
# FÉRIAS VENCIDAS
# =========================================
periodos_vencidos = (
    total_meses // 12
)

ferias_vencidas = (
    periodos_vencidos *
    salario
)

terco_ferias_vencidas = (
    ferias_vencidas / 3
)

total_ferias_vencidas = (
    ferias_vencidas +
    terco_ferias_vencidas
)

# =========================================
# FÉRIAS PROPORCIONAIS
# =========================================
meses_restantes = (
    total_meses % 12
)

ferias_proporcionais = (
    salario / 12
) * meses_restantes

terco_ferias_proporcionais = (
    ferias_proporcionais / 3
)

total_ferias_proporcionais = (
    ferias_proporcionais +
    terco_ferias_proporcionais
)

# =========================================
# TOTAL DA RESCISÃO
# =========================================
total_rescisao = (

    saldo_salario +

    decimo_terceiro +

    valor_aviso +

    multa_fgts +

    total_ferias_vencidas +

    total_ferias_proporcionais
)

# =========================================
# STATUS DO AVISO
# =========================================
if opcao_aviso == "1":
    status_aviso = "Cumpriu"

else:
    status_aviso = "Não cumpriu"

# =========================================
# RESULTADO
# =========================================
print("\n================================")
print("      RESCISÃO TRABALHISTA")
print("================================")

print(f"\nSalário: R$ {salario:.2f}")

print(
    f"Tempo trabalhado: "
    f"{anos} anos e {meses_restantes} meses"
)

print(
    f"\nDias trabalhados no mês: "
    f"{dias_trabalhados}"
)

print(
    f"Saldo de salário: "
    f"R$ {saldo_salario:.2f}"
)

print(
    f"\n13º proporcional: "
    f"R$ {decimo_terceiro:.2f}"
)

print(
    f"\nAviso prévio: "
    f"{status_aviso}"
)

print(
    f"Dias de aviso: "
    f"{dias_aviso}"
)

print(
    f"Valor do aviso: "
    f"R$ {valor_aviso:.2f}"
)

print(
    f"\nFGTS acumulado: "
    f"R$ {fgts:.2f}"
)

print(
    f"Multa de 40% do FGTS: "
    f"R$ {multa_fgts:.2f}"
)

print(
    f"\nPeríodos de férias vencidas: "
    f"{periodos_vencidos}"
)

print(
    f"Férias vencidas + 1/3: "
    f"R$ {total_ferias_vencidas:.2f}"
)

print(
    f"Férias proporcionais + 1/3: "
    f"R$ {total_ferias_proporcionais:.2f}"
)

print("\n================================")

print(
    f"TOTAL DA RESCISÃO: "
    f"R$ {total_rescisao:.2f}"
)

print("================================")