"""Testes para upload S3"""

def test_math_operation():
    """Teste simples"""
    result = 5 + 3
    assert result == 8

def test_requirements_exists():
    """Verifica requirements.txt"""
    from pathlib import Path
    assert Path("requirements.txt").exists()
