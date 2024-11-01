# API de Filmes

## Criando ambiente virtual

- Windows:
```
python3.12 -m venv .venv
```

Caso o powerShell não esteja habilitado para executar scripts:
execute no powerShell:
```
Set-ExecutionPolicy Unrestricted
```
Ativando a venv:
```
.venv\Scripts\activate
```

Para desativar basta executar deactivate no PowerShell

- Distribuição Linux:
```
python3.12 -m venv .venv
```

Ativando venv:
```
source .venv/bin/activate
```

## Instalando as Bibliotecas

Com o ambiente virtual ativado execute:

```
pip install -r requirements.txt
```

## Para executar a API
```
uvicorn app.main:app --reload
```
