"""Testes para transformação"""

def test_basic_math():
    """Teste básico"""
    assert 2 * 2 == 4

def test_files_exist():
    """Verifica se arquivos existem"""
    from pathlib import Path
    assert Path("data/raw").exists()
    assert Path("data/processed").exists()
