from __future__ import annotations
import argparse,json
from pathlib import Path
from .core import parse_joins

def main(argv=None):
    p=argparse.ArgumentParser(description="Visualize Oracle ANSI JOINs.")
    p.add_argument("source")
    p.add_argument("--format",choices=("text","json","mermaid"),default="text")
    a=p.parse_args(argv)
    edges=parse_joins(Path(a.source).read_text(encoding="utf-8"))
    if a.format=="json":
        print(json.dumps([e.to_dict() for e in edges],indent=2))
    elif a.format=="mermaid":
        print("flowchart LR")
        for i,e in enumerate(edges):
            label=(e.join_type + (": "+e.condition if e.condition else "")).replace('"',"'")
            print(f'    L{i}["{e.left}"] -->|"{label}"| R{i}["{e.right}"]')
    else:
        for e in edges: print(f"{e.left} --[{e.join_type}: {e.condition}]--> {e.right}")
    return 0
if __name__=="__main__": raise SystemExit(main())
