import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup


def extrair_cursos():
    url = "https://gratuitos.netlify.app"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()

        soup = BeautifulSoup(resposta.text, "html.parser")

    
        tabela = soup.find("table", class_="table table-sm bg-light text-left")

        if tabela is None:
            messagebox.showerror("Erro", "Tabela de cursos não encontrada!")
            return

        caixa_texto.delete("1.0", tk.END)

    
        cabecalho = tabela.find("thead")
        colunas = cabecalho.find_all("th")

        texto_cabecalho = " | ".join(
            coluna.get_text(strip=True) for coluna in colunas
        )

        caixa_texto.insert(tk.END, texto_cabecalho + "\n")
        caixa_texto.insert(tk.END, "-" * 100 + "\n")

    
        corpo = tabela.find("tbody")
        linhas = corpo.find_all("tr")

        for linha in linhas:
            celulas = linha.find_all(["th", "td"])

            dados = [
                celula.get_text(" ", strip=True)
                for celula in celulas
            ]

            caixa_texto.insert(
                tk.END,
                " | ".join(dados) + "\n"
            )

    except Exception as erro:
        messagebox.showerror(
            "Erro",
            f"Erro ao acessar o site:\n{erro}"
        )


janela = tk.Tk()
janela.title("Tabela de Cursos")
janela.geometry("1000x500")


botao = tk.Button(
    janela,
    text="Extrair Cursos",
    command=extrair_cursos
)

botao.pack(pady=10)


caixa_texto = scrolledtext.ScrolledText(
    janela,
    width=120,
    height=25,
    font=("Arial", 10)
)

caixa_texto.pack(
    padx=10,
    pady=10,
    fill=tk.BOTH,
    expand=True
)

janela.mainloop()

from bs4 import BeautifulSoup
import requests

url = 'https://tabelatest.netlify.app/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

for linha in soup.find_all('tr')[1:]:
    colunas = linha.find_all('td')
    print(colunas[1].get_text(strip=True))