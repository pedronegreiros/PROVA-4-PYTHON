#PEDRO NEGREIROS ANDRADE

def calcular_media(notas):
    if len(notas) == 0:
        return 0
    else:
        return sum(notas) / len(notas)

def verificar_situacao(media):
    if media < 7:
        return "Reprovado"
    elif media == 10:
        return "Sua média é 10"
    else:
        return "Aprovado"

notas = []
while True:
    nota_str = input("Digite uma nota (ou 'fim' para encerrar): ")
    
    if nota_str.lower() == 'fim':
        break

    try:
        nota = float(nota_str)
        notas.append(nota)
    except ValueError:
        print("Digite um valor numérico válido.")

media = calcular_media(notas)

situacao = verificar_situacao(media)

print(f"\nMédia: {media:.2f}")
print(f"Situação: {situacao}")

