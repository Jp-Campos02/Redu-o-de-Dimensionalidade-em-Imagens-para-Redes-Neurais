import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Carregar a imagem (substitua 'lena.jpg' pelo caminho da sua imagem)
image_path = "/content/Lena COLAB.png"  # Caminho da imagem
image = Image.open(image_path)

# Converter a imagem para um array numpy
image_array = np.array(image)

# Conversão para níveis de cinza
def rgb_to_grayscale(rgb_image):
    # Pesos baseados na percepção humana (ITU-R BT.601)
    return np.round(
        0.299 * rgb_image[:, :, 0] + 0.587 * rgb_image[:, :, 1] + 0.114 * rgb_image[:, :, 2]
    ).astype(np.uint8)

gray_image = rgb_to_grayscale(image_array)

# Binarização
def binarize_image(gray_image, threshold=127):
    binary = np.where(gray_image > threshold, 255, 0)
    return binary.astype(np.uint8)

binary_image = binarize_image(gray_image)

# Salvar as imagens processadas
Image.fromarray(gray_image).save("gray_image.png")
Image.fromarray(binary_image).save("binary_image.png")

# Visualizar as imagens
plt.figure(figsize=(15, 5))

# Imagem original
plt.subplot(1, 3, 1)
plt.imshow(image)
plt.title("Imagem Colorida (Entrada)")
plt.axis("off")

# Imagem em níveis de cinza
plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Imagem em Níveis de Cinza")
plt.axis("off")

# Imagem binarizada
plt.subplot(1, 3, 3)
plt.imshow(binary_image, cmap="gray")
plt.title("Imagem Preto e Branco")
plt.axis("off")

plt.show()

print("As imagens processadas foram salvas como 'gray_image.png' e 'binary_image.png'.")
