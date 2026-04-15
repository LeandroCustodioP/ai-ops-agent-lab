from pydantic import BaseModel, Field
from typing import List, Literal

class TroubleshootingHypothesis(BaseModel):
    cause: str = Field(description="Descrição da hipótese do que pode estar causando o erro.")
    fix_suggestion: str = Field(description="Comando, código ou ação prática para testar/resolver esta hipótese específica.")
    confidence_score: float = Field(description="Probabilidade desta hipótese ser a correta (0.0 a 1.0).")

class Diagnosis(BaseModel):
    category: Literal["Infrastructure", "Database", "Code", "Permission"] = Field(
        description="Categoria técnica principal do erro."
    )
    error_summary: str = Field(description="Resumo técnico do erro encontrado no log.")
    hypotheses: List[TroubleshootingHypothesis] = Field(
        description="Lista de possíveis causas e soluções ordenadas pela maior probabilidade."
    )
    severity: Literal["Low", "Medium", "High", "Critical"]