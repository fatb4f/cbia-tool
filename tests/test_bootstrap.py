from cbia_workbench.repl.bootstrap import bootstrap


def test_bootstrap_keys():
    ctx = bootstrap(log_dir=".tmp-logs")
    assert "log" in ctx
    assert "eofl" in ctx
    assert "obs" in ctx
    assert "op" in ctx
