import pytest
from pathlib import Path

def test_data_directories_exist():
    """Verifica se os diretórios de dados existem"""
    assert Path("data/raw").exists(), "Diretório data/raw não existe"
    assert Path("data/processed").exists(), "Diretório data/processed não existe"

def test_scripts_exist():
    """Verifica se os scripts principais existem"""
    assert Path("scripts/extract.py").exists(), "extract.py não existe"
    assert Path("scripts/transform.py").exists(), "transform.py não existe"
    assert Path("scripts/upload_s3.py").exists(), "upload_s3.py não existe"

def test_dashboard_exists():
    """Verifica se o dashboard existe"""
    assert Path("dashboard/app.py").exists(), "dashboard/app.py não existe"

def test_config_files_exist():
    """Verifica se os arquivos de config existem"""
    assert Path("requirements.txt").exists(), "requirements.txt não existe"
    assert Path(".env.example").exists(), ".env.example não existe"
    assert Path("README.md").exists(), "README.md não existe"
