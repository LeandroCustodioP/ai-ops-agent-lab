import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq # Biblioteca específica
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from src.models import Diagnosis

load_dotenv()

def run_diagnosis(log_content: str):
    model = ChatGroq(model="llama-3.3-70b-versatile", temperature=0) # Groq é perfeito aqui
    parser = JsonOutputParser(pydantic_object=Diagnosis)

    prompt = ChatPromptTemplate.from_messages([
        ("system", """Você é o Especialista de Dados Sênior da Bússola Consultoria.
        Sua tarefa é realizar um Troubleshooting profundo de logs do Airflow.
        
        Siga estas diretrizes:
        1. Analise o traceback detalhadamente.
        2. Liste múltiplas hipóteses caso o erro seja ambíguo.
        3. Para cada hipótese, forneça uma solução técnica acionável.
        4. Responda estritamente no formato JSON solicitado.
        
        {format_instructions}"""),
        ("user", "LOG DE ERRO:\n{log_text}")
    ]).partial(format_instructions=parser.get_format_instructions())

    chain = prompt | model | parser
    return chain.invoke({"log_text": log_content})