from pydantic import BaseModel


class AIAnalysis(BaseModel):

    overall_health: str

    executive_summary: str

    key_insights: list[str]

    recommendations: list[str]