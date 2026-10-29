"""Compare the trend chart traces between two sets of harness runs.

Usage (any Python 3, stdlib only):
    python3 dev/compare_before_after.py <before_results_root> <after_results_root> <case> [<case> ...]

Each root holds one directory per case as `dev/run-test-cases.sh` leaves them
(`<root>/<case>/<hash>_trend_chart.html` + `result.json`). For every case, every
dashboard view's plotly figure is parsed; series are matched BY POSITION within the
view and their x and y values compared. A series whose name changed but whose values
did not is reported as a label change, separately from a value difference (the only
expected label change is the Patrol Type category: slug -> display name). Exit code 1
on any value difference, lost view or changed series count.
"""

import json
import re
import sys
from pathlib import Path

TOL = 1e-9


def traces(html: str) -> list[dict]:
    m = re.search(r"Plotly\.newPlot\(\s*\"[^\"]+\",\s*(\[.*?\]),\s*\{", html, re.S)
    return json.loads(m.group(1)) if m else []


def views(root: Path, case: str) -> dict[str, list[dict]]:
    result = json.loads((root / case / "result.json").read_text())
    out = {}
    for key, widgets in result["result"]["views"].items():
        for w in widgets:
            if not (w.get("data") or "").endswith(".html"):
                continue
            out[key] = traces((root / case / Path(w["data"]).name).read_text())
    return out


def same_values(a, b) -> bool:
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(same_values(x, y) for x, y in zip(a, b))
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) <= TOL
    return a == b


def compare(before: dict[str, list[dict]], after: dict[str, list[dict]]) -> tuple[list[str], list[str]]:
    diffs, labels = [], []
    if set(before) - set(after):
        diffs.append(f"views lost: {sorted(set(before) - set(after))}")
    extra = sorted(set(after) - set(before))
    if extra:
        diffs.append(f"views only in after: {extra}")
    for key in sorted(set(before) & set(after)):
        b_tr, a_tr = before[key], after[key]
        if len(b_tr) != len(a_tr):
            diffs.append(f"{key}: series count before={len(b_tr)} after={len(a_tr)} "
                         f"(after names: {[t.get('name') for t in a_tr]})")
            continue
        for i, (b, a) in enumerate(zip(b_tr, a_tr)):
            for axis in ("x", "y"):
                if not same_values(b.get(axis), a.get(axis)):
                    diffs.append(f"{key} series {i} ({b.get('name')}) {axis}: before={b.get(axis)} after={a.get(axis)}")
            if b.get("name") != a.get("name"):
                labels.append(f"{key} series {i}: {b.get('name')!r} -> {a.get('name')!r}")
    return diffs, labels


def main() -> None:
    before_root, after_root, *cases = sys.argv[1:]
    failed = False
    for case in cases:
        b, a = views(Path(before_root), case), views(Path(after_root), case)
        diffs, labels = compare(b, a)
        n_series = sum(len(t) for t in a.values())
        status = "DIFF" if diffs else "same"
        print(f"{status:4} {case}: {len(a)} view(s), {n_series} series")
        for d in diffs:
            print("     ", d)
        for lab in labels:
            print("      label:", lab)
        failed |= bool(diffs)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
