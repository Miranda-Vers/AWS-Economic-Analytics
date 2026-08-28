# 📐 Arquitetura

## Pipeline de Dados

API SGS → Extract → S3 → Transform → SQLite → Dashboard

## Componentes

- Extract: scripts/extract.py
- Transform: scripts/transform.py
- Upload: scripts/upload_s3.py
- Dashboard: dashboard/app.py
