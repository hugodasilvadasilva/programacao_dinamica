from PIL import Image 

image = Image.open("input/gato01.jpeg")

# Imprime os valores dos píxels em uma imagem jpeg. Essa imagem
# terá uma tupla de 3 valores (RGB). As imagens .png permitem
# definir opacidade e por isso possuem 4 valores, sendo o último
# o valor do opaco de transarente (0) a opaco (255)
x = 100
y = 100
print("Pixel na posição", str(x), ",", str(y), "=", image.getpixel((x,y)))

image.show()