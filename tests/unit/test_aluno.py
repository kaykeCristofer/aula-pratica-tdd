import pytest
from unittest.mock import MagicMock
from aluno.aluno import Aluno


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug descrito no guia da atividade.
# =============================================================

def test_retornar_menor_nota():
    aluno = Aluno(nome="Julia", notas=[6, 7, 4, 9], faltas=2)
    assert aluno.menor_nota() == 4

def test_calcular_media():
    aluno = Aluno(nome="Carlos", notas=[7, 7, 7], faltas=1)
    assert aluno.calcular_media() == 7

def test_calcular_media_arredondada():
    aluno = Aluno(nome="Carol", notas=[5, 6, 7, 9], faltas=9)
    assert aluno.calcular_media_arredondada() == 7

def test_situacao_aprovado():
    aluno = Aluno(nome="Ana", notas=[6, 5, 7, 6], faltas=12)
    assert aluno.situacao() == "Aprovado"

def test_situacao_reprovado():
    aluno = Aluno(nome="Pedro", notas=[5, 5, 5, 5], faltas=15)
    assert aluno.situacao() == "Reprovado"

def test_nota_maxima():
    aluno = Aluno(nome="Lucas", notas=[8, 9, 7, 10], faltas=0)
    assert aluno.maior_nota() == 10

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função

def test_contar_aprovados_com_todos_aprovados():
    alunos = [
        Aluno(nome="Julia", notas=[9, 8, 9, 10], faltas=3),
        Aluno(nome="Maria", notas=[7, 6, 5, 8], faltas=5),
        Aluno(nome="Caroline", notas=[10, 10, 10, 10], faltas=0),
    ]

    assert contar_aprovados(alunos) == 3

def test_contar_aprovados_com_todos_reprovados():
    alunos = [
        Aluno(nome="Jon", notas=[4, 3, 2, 4], faltas=14),
        Aluno(nome="Danilo", notas=[1, 3, 3, 7], faltas=15),
        Aluno(nome="Carla", notas=[5, 5, 5, 5], faltas=11),
    ]

    assert contar_aprovados(alunos) == 0

def test_contar_aprovados_com_lista_mista():
    alunos = [
        Aluno(nome="Lara", notas=[9, 8, 7, 6], faltas=2),
        Aluno(nome="Nerez", notas=[3, 4, 5, 4], faltas=13),
        Aluno(nome="Evaniele", notas=[6, 6, 6, 6], faltas=9),
        Aluno(nome="Italo", notas=[5, 5, 5, 5], faltas=12),
    ]

    assert contar_aprovados(alunos) == 2

def test_contar_aprovados_com_lista_vazia():
    assert contar_aprovados([]) == 0

# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
