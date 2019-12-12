def media(nota_1, nota_2):
    media = (nota_1 + nota_2)/2
    if media >= 6:
        return f'Parabéns! Você foi aprovad com média {media}'
    else:
        return media


print(media(5, 7))
