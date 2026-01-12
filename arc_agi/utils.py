from arc_agi.types import RunResult


def canonical_test_key(results: list[RunResult]) -> str:
    
    # ===== PRINT DEBUG END ======
    print(f"CANONICAL TEST KEY:{str([r['output'] for r in results])}")
    print("=" * 50)
    # ===== PRINT DEBUG END ======
    
    return str([r["output"] for r in results]) # ["a", "b"]
