from __future__ import annotations
from dataclasses import dataclass,asdict
import re

@dataclass(frozen=True)
class JoinEdge:
    left: str
    right: str
    join_type: str
    condition: str
    def to_dict(self): return asdict(self)

TABLE=r'([A-Za-z][\w$#]*(?:\.[A-Za-z][\w$#]*)?)'
ALIAS=r'([A-Za-z][\w$#]*)'

def parse_joins(sql:str)->list[JoinEdge]:
    base=re.search(rf"\bFROM\s+{TABLE}(?:\s+{ALIAS})?",sql,re.I)
    if not base: return []
    left_obj=base.group(1).upper()
    current_alias=(base.group(2) or base.group(1)).upper()
    alias_to_obj={current_alias:left_obj}
    edges=[]
    pattern=re.compile(rf"\b(?:(INNER|LEFT|RIGHT|FULL|CROSS)\s+)?JOIN\s+{TABLE}(?:\s+{ALIAS})?\s*(?:ON\s+(.+?))?(?=\b(?:INNER|LEFT|RIGHT|FULL|CROSS)?\s*JOIN\b|\bWHERE\b|\bGROUP\b|\bORDER\b|\bCONNECT\b|$)",re.I|re.S)
    for m in pattern.finditer(sql):
        jt=(m.group(1) or "INNER").upper()
        obj=m.group(2).upper()
        alias=(m.group(3) or m.group(2)).upper()
        cond=re.sub(r"\s+"," ",(m.group(4) or "").strip())
        alias_to_obj[alias]=obj
        edges.append(JoinEdge(alias_to_obj.get(current_alias,current_alias),obj,jt,cond))
        current_alias=alias
    return edges
