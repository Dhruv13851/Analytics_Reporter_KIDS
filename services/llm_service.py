from langchain_groq import ChatGroq

from config import Config
from models.llm_output_model import AIAnalysis
from prompts.llm_prompt import analytics_prompt


class LLMService:

    def __init__(self):

        self.llm = ChatGroq(
            api_key=Config.GROQ_API_KEY,
            model=Config.GROQ_MODEL,
            temperature=Config.GROQ_TEMPERATURE,
            max_tokens=Config.GROQ_MAX_TOKENS,
            timeout=Config.GROQ_TIMEOUT,
        )

        self.chain = (
            analytics_prompt
            | self.llm.with_structured_output(AIAnalysis)
        )

    def analyze(self, comparison_report: dict) -> dict:

        response = self.chain.invoke(
            {
                "comparison": comparison_report
            }
        )

        return response.model_dump()