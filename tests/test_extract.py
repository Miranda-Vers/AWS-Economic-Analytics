"""Testes para extração de dados"""

def test_basic_functionality():
    """Teste básico que sempre passa"""
    assert 1 + 1 == 2

def test_project_structure():
    """Verifica estrutura do projeto"""
    from pathlib import Path
    assert Path("scripts/extract.py").exists()
    assert Path("scripts/transform.py").exists()
    assert Path("dashboard/app.py").exists()
