import random

print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")

escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()

if escolha_usuario not in ["pedra", "papel", "tesoura"]:
    print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
else:
    escolha_computador = random.choice(["pedra", "papel", "tesoura"])
    print(f"Você escolheu: {escolha_usuario}")
    print(f"O computador escolheu: {escolha_computador}")

    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (
        (escolha_usuario == "pedra" and escolha_computador == "tesoura") or
        (escolha_usuario == "papel" and escolha_computador == "pedra") or
        (escolha_usuario == "tesoura" and escolha_computador == "papel")
    ):
        print("Você venceu!")
    else:
        print("O computador venceu!")