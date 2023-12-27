import random

def escolher_categoria():
    categorias = {"objetos" : ["óculos", "cadeira", "mesa", "tesoura", "controle", "cortina", "caixa de som", "ventilador", "bolsa"], 
                "animais" : ["gato", "cachorro", "baleia", "girafa", "elefante", "tigre"]}

    print("Escolha uma categoria: ")
    for categoria in categorias:
        print(f"- {categoria}")

    categoria_escolhida = input("Digite o nome da categoria: ").lower()

    while categoria_escolhida not in categorias:
        print("Categoria inválida. Tente novamente. ")
        categoria_escolhida = input("Digite o nome da categoria: ").lower()

    return random.choice(categorias[categoria_escolhida])

def exibir_palavra_oculta(palavra, letras_corretas):
    return ' '.join(l if l in letras_corretas else '_' for l in palavra)


palavra_escolhida = escolher_categoria()
palavra_oculta = "_" * len(palavra_escolhida)
tentativas_maxima = 6 
tentativas_restantes = tentativas_maxima
letras_incorretas = []
letras_corretas = []

while tentativas_restantes > 0 and "_" in palavra_oculta:
    print(f"Palavra: {exibir_palavra_oculta(palavra_escolhida, letras_corretas)} ({len(palavra_oculta)} letras")
    print(f"Tentativas restantes: {tentativas_restantes}")
    print(f"Letras incorretas: {', '.join(letras_incorretas)}")

    letra = input("Digite uma letra: ") .lower()

    if letra in palavra_escolhida and letra not in palavra_oculta: 
        print("Letra correta!")

        letras_corretas.append(letra) 

        # Atualizar a palavra oculta com a letra correta na posição correta
        nova_palavra_oculta = ''.join(l if l in letras_corretas else '_' for l in palavra_escolhida)
        palavra_oculta = nova_palavra_oculta
    else:
        if letra in letras_incorretas or letra in letras_corretas:
            print("Você já tentou essa letra. Tente outra")
        else:
            print("Letra incorreta.")
            letras_incorretas.append(letra)
            tentativas_restantes -= 1   

if "_" not in palavra_oculta:
    print(f"Parabéns! Você acertou! A palava era '{palavra_escolhida}'.") 
else:
    print(f"Você perdeu! A palava era '{palavra_escolhida}'.")     
