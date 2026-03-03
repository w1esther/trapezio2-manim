# Área do Trapézio

Este repositório é dedicado a **scripts em Python**, utilizando a biblioteca **Manim**, para a elaboração de uma animação que mostra de onde vem a fórmula que usamos para calcular a  **Área de um trapézio**.

---

## 🎯 Para que serve?

mostrar, de forma **visual e dinâmica**, o motivo pelo qual a área do trapézio é calculada pela (base maior mais a base menor) vezes a altura tudo isso dividido por dois.

---

## 🧠 Por que executar o Manim em um ambiente virtual?

O Manim deve ser executado em um **ambiente virtual** para garantir que todas as dependências necessárias estejam instaladas e isoladas do sistema. Isso evita conflitos de versões, erros de execução e problemas com bibliotecas gráficas e de vídeo.

---

## 🐍 O que é o Anaconda?

O **Anaconda** é um software que instala o Python e fornece ferramentas para gerenciar **ambientes virtuais** e **bibliotecas**. Ele não é uma IDE, mas facilita a organização das dependências do projeto.

---

## 💻 Instalando o Anaconda

1. Acesse o site oficial do Anaconda:

   * [https://www.anaconda.com/download](https://www.anaconda.com/download)
2. Baixe a versão correspondente ao **seu sistema operacional** (Windows, macOS ou Linux).
3. Execute o instalador e siga as instruções padrão.

⚠️ **Importante:** utilize o **terminal fornecido pelo Anaconda** no seu sistema operacional.

---

## 🌱 Criando o ambiente virtual

No terminal do Anaconda, execute:

```bash
conda create -n manim-env python=3.12
```

Esse comando cria um ambiente virtual chamado `manim-env`.

Confirme digitando `y` quando solicitado.

Ative o ambiente com:

```bash
conda activate manim-env
```

Se aparecer `(manim-env)` no início da linha, o ambiente está ativo.

---

## 📦 Instalando dependências essenciais

Algumas bibliotecas são fundamentais para o funcionamento do Manim:

* **Cairo** – responsável pela renderização gráfica
* **FFmpeg** – responsável pela geração dos vídeos

Instale ambas com:

```bash
conda install -c conda-forge cairo ffmpeg
```

---

## 🎬 Instalando o Manim

Com o ambiente ativado, instale o Manim:

```bash
pip install manim
```

Verifique a instalação:

```bash
manim --version
```

---

## 🛠️ Tecnologias utilizadas

* **Python 3.12**
* **Biblioteca Manim (Manim Community)**

---

## 🔗 Clonando o repositório

No terminal, execute:

```bash
git clone https://github.com/w1esther/trapezio-manim.git
```

Entre na pasta do projeto:

```bash
cd trapezio2-manim
```

---

## ▶️ Executando a animação

Dentro da pasta do projeto, utilize um dos comandos abaixo:

### 🔹 Baixa resolução

```bash
manim -pql trapezio.py AreaTrapezio
```

### 🔹 Média resolução

```bash
manim -pqm trapezio.py AreaTrapezio
```

### 🔹 Alta resolução

```bash
manim -pqk trapezio.py AreaTrapezio
```

---

## 🔄 Como acessar o ambiente virtual depois

Sempre que quiser executar o projeto novamente:

```bash
conda activate manim-env
```

Depois, entre na pasta do projeto e execute o Manim normalmente.

---

✨ Projeto pronto para execução da Área do trapézio.
