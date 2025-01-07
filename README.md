# Redu-o-de-Dimensionalidade-em-Imagens-para-Redes-Neurais
Transformação de Imagens: Níveis de Cinza e Binarização

Introdução O objetivo é demonstrar a conversão de uma imagem colorida para: Níveis de Cinza: Tons variando de 0 (preto) a 255 (branco). Binarizada: Apenas dois valores possíveis (0 e 255), criando uma imagem preto e branco.
Processo de Conversão Imagem Colorida:
Contém informações em três canais: R (vermelho), G (verde) e B (azul). Níveis de Cinza:

Fórmula para conversão: 𝑌 = 0.299 ⋅ 𝑅 + 0.587 ⋅ 𝐺 + 0.114 ⋅ 𝐵 Y=0.299⋅R+0.587⋅G+0.114⋅B Essa ponderação reflete como o olho humano percebe as cores. Binarização:

Definimos um limiar (threshold). Intensidades maiores que o limiar são definidas como 255 (branco), e menores ou iguais como 0 (preto).

Código Desenvolvido O código foi implementado sem bibliotecas específicas para processamento de imagens. Utilizamos apenas numpy para operações matemáticas e manipulação de arrays.
Resultado As imagens processadas são salvas como: gray_image.png (Níveis de cinza). binary_image.png (Preto e branco). Visualização: Imagem original (entrada). Imagem em níveis de cinza. Imagem binarizada.
Demonstração Imagem Original: Representa a entrada em RGB. Imagem em Níveis de Cinza: Mostra a intensidade de luz dos pixels. Imagem Binarizada: Destaca regiões principais com contraste acentuado.
Conclusão Este processo é essencial para pré-processamento de imagens em diversas aplicações, como: Reconhecimento de padrões. Segmentação de imagens. Compressão de dados.
