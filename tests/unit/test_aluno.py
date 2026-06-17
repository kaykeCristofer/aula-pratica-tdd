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
    aluno = Aluno(nome="Carol", notas=[5, 6, 7, 9], faltas=0)
    assert aluno.calcular_media_arredondada() == 7

# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_aprovados(lista_de_alunos) -> int
# Escreva os testes ANTES de implementar a função


# Requisito 2 — situacao_final(total_aulas) -> str
# Escreva os testes ANTES de implementar o método


# Requisito 3 — enviar_boletim(email_service)
# Use MagicMock para simular o serviço de e-mail
# Escreva os testes ANTES de implementar o método
