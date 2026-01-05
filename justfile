set dotenv-load := true

sync:
  uv sync --all-extras

repl:
  uv run konch -c repl/konch.py

test:
  uv run pytest -q

lint:
  uv run ruff check .

typecheck:
  uv run pyright

verify-material:
  uv run python tools/verify_material.py
