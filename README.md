# 🎲 Random Thermal Laughs

> Um pequeno projeto que imprime imagens engraçadas aleatórias em uma impressora térmica — apenas para dar risada.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey)
![Printer](https://img.shields.io/badge/Printer-POS--58-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Just%20for%20Fun-yellow)
![Hardware](https://img.shields.io/badge/Hardware-Thermal%20Printer-black)

---

## 😂 Sobre

**Random Thermal Laughs** é um pequeno script em Python que transforma sua impressora térmica em uma máquina de memes aleatórios.
Ele seleciona uma imagem engraçada de uma pasta e imprime automaticamente — sem lógica, sem produtividade, apenas caos e risadas.

Perfeito para:

* 🖨️ Gadgets de mesa
* 😂 Imprimir memes aleatórios
* 🎉 Surpreender amigos
* 🧪 Experimentos com hardware
* ☕ Diversão no escritório

---

## 🖼️ Como funciona

1. Coloque imagens dentro da pasta `images/`
2. Execute o script
3. Uma imagem aleatória é selecionada
4. Ela é redimensionada e convertida para formato compatível com impressora térmica
5. Impressa instantaneamente

Cada execução = uma surpresa 🎲

---

## 📁 Estrutura do Projeto

```
Random-Thermal-Laughs/
│
├── imprimir_imagem.py
└── images/
    ├── meme1.png
    ├── cat.jpg
    ├── random.png
    └── ...
```

---

## ⚙️ Requisitos

* Python 3.9+
* Impressora térmica (POS-58 recomendada)
* Impressora USB ou compartilhada no Windows

Instale as dependências:

```bash
pip install python-escpos pillow pywin32
```

---

## ▶️ Como usar

Basta executar:

```bash
python imprimir_imagem.py
```

O script irá:

* escolher uma imagem aleatória 🎲
* preparar para impressão térmica 🧾
* imprimir automaticamente 🖨️

---

## 🧠 Funcionalidades

* Seleção aleatória de imagens
* Otimizado para impressoras térmicas
* Dithering Floyd–Steinberg para melhor qualidade
* Redimensionamento automático
* Impressão centralizada
* Compatível com impressoras POS-58
* Sem necessidade de configuração

---

## 🖨️ Impressoras suportadas

A maioria das impressoras compatíveis com ESC/POS, incluindo:

* POS-58
* Impressoras térmicas genéricas 58mm
* Impressoras USB ESC/POS

---

## 🎯 Personalização

Alterar nome da impressora:

```python
PRINTER_NAME = "POS-58"
```

Alterar pasta de imagens:

```python
IMAGES_FOLDER = "images"
```

---

## 💡 Ideias para expansão

* ⏱️ Imprimir a cada X minutos
* 🎲 Imprimir múltiplas imagens
* 🧾 Imprimir imagem + frase aleatória
* 🌐 Buscar memes da internet
* 🎮 Impressão acionada por botão (Raspberry Pi)
* 🧠 Imagens geradas por IA

---

## ⚠️ Aviso

Este projeto existe puramente para diversão.
Ele pode gastar papel, confundir colegas e produzir humor questionável.

Use com responsabilidade 😄

---

## 📜 Licença

MIT — faça o que quiser, apenas se divirta.

---

## ✨ Exemplo

Execute o script e sua impressora vira:

```
[ DISPENSADOR DE MEMES ALEATÓRIOS ]
            ↓
        🖨️ imprimindo...
            ↓
         😂 surpresa
```

---

Feito para risadas, não para produtividade.
