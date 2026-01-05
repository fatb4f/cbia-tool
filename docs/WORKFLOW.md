# Workflow (workbench)

1. Populate `content/material/` via sparse-checkout from the build repo.
2. (Optional) copy build manifest to `content/manifest.json`.
3. Run:
   - `just sync` (uv env)
   - `just repl` (Konch REPL)
   - `just verify-material` (basic structure checks)
