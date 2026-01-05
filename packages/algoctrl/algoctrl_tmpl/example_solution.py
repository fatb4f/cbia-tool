"""example_solution.py — demonstrates stage logging (v2).

Shows:
- Stage enum usage
- @stage_fn decorator usage
- boundary logs + metrics
"""

from __future__ import annotations

from typing import Iterable, Iterator, Optional

from algoctrl_tmpl.observer import Stage, StageObserver, stage_fn


@stage_fn(Stage.GEN, note="accept candidate stream")
def gen_candidates(nums: Iterable[int], *, obs: StageObserver) -> Iterator[int]:
    return iter(nums)


@stage_fn(Stage.STRUCT, note="streaming (no materialization)")
def struct_state(*, obs: StageObserver) -> dict:
    return {"checked": 0}


def first_matching(
    nums: Iterable[int], *, threshold: int, obs: StageObserver
) -> Optional[int]:
    it = gen_candidates(nums, obs=obs)
    state = struct_state(obs=obs)

    with obs.stage(Stage.FLOW, note="scan candidates"):
        for n in it:
            state["checked"] += 1

            # SELECT: prune cheap rejects early
            if n <= threshold:
                continue
            if (n % 2) == 0:
                continue
            if (n % 3) != 0:
                continue

            with obs.stage(Stage.EVAL, note="first match"):
                obs.metric(Stage.EVAL, "checked", state["checked"])
                obs.metric(Stage.EVAL, "match", n)
                return n

    with obs.stage(Stage.EVAL, note="no match"):
        obs.metric(Stage.EVAL, "checked", state["checked"])
        obs.metric(Stage.EVAL, "match", None)
    return None


def main() -> None:
    obs = StageObserver(run_id="demo-002", level="INFO")
    out = first_matching(range(1, 100), threshold=40, obs=obs)
    print("result:", out)


if __name__ == "__main__":
    main()
