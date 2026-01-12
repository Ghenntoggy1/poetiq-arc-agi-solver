from arc_agi.config import CONFIG_LIST
from arc_agi.solve_parallel_coding import solve_parallel_coding
from arc_agi.types import ARCAGIGrid, ARCAGIResult


async def solve(
    train_in: list[ARCAGIGrid],
    train_out: list[ARCAGIGrid],
    test_in: list[ARCAGIGrid],
    problem_id: str | None = None,
) -> list[ARCAGIResult]:
    result = await solve_parallel_coding(
        train_in=train_in,
        train_out=train_out,
        test_in=test_in,
        expert_configs=[cfg.copy() for cfg in CONFIG_LIST],
        problem_id=problem_id,
    )

    return result
