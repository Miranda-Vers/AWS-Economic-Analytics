import pytest
from pathlib import Path

def test_data_directories_exist():
    assert Path('data/raw').exists()
    assert Path('data/processed').exists()

def test_scripts_exist():
    assert Path('scripts/extract.py').exists()
    assert Path('scripts/transform.py').exists()

def test_dashboard_exists():
    assert Path('dashboard/app.py').exists()

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
