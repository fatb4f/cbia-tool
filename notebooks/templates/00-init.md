---
jupytext:
  formats: md
  text_representation:
    extension: .md
    format_name: markdown
    format_version: "1.3"
    jupytext_version: 1.16.0
---

# 00 — Init

```python
from cbia_workbench.notebook import bootstrap_notebook

ctx = bootstrap_notebook()
globals().update(
    {
        "ctx": ctx,
        "log": ctx.log,
        "eofl": ctx.eofl,
        "obs": ctx.obs,
        "op": ctx.op,
    }
)
```
