"""Aplicativo simples que usa caixas de diálogo do Tkinter para solicitar o nome do usuário.

O programa abre uma janela pedindo ao usuário que digite seu nome. Se o nome fornecido for
"Thiago" (sem considerar maiúsculas ou minúsculas), o programa executará uma rotina de boas-vindas.
Para qualquer outro nome ou entrada vazia, uma mensagem de acesso negado é exibida.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, simpledialog


def solicitar_nome() -> str | None:
    """Exibe uma janela solicitando o nome do usuário.

    Returns:
        A string com o nome digitado pelo usuário ou ``None`` caso a caixa de diálogo
        seja cancelada.
    """

    root = tk.Tk()
    root.withdraw()
    root.update_idletasks()

    try:
        return simpledialog.askstring("Identificação", "Digite seu nome:", parent=root)
    finally:
        root.destroy()


def rotina_principal() -> None:
    """Executa a rotina principal do programa."""

    nome = solicitar_nome()

    if nome and nome.casefold() == "thiago":
        messagebox.showinfo("Acesso permitido", "Bem-vindo, Thiago! Rotina iniciada.")
    else:
        messagebox.showerror(
            "Acesso negado",
            "Acesso negado! Polícia a caminho.",
        )


if __name__ == "__main__":
    rotina_principal()
