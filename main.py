# ai-ops-agent-lab/main.py
from src.agent_brain import run_diagnosis

def main():
    log_path = "data/mock_error.log"
    
    print(f"🚀 Iniciando diagnóstico para: {log_path}\n")
    
    try:
        with open(log_path, "r") as f:
            log_content = f.read()
        
        # Chama o cérebro do agente
        result = run_diagnosis(log_content)
        
        # Exibição bonitona do resultado
        print("✅ Diagnóstico Concluído:")
        print("-" * 30)
        print(f"CATEGORIA: {result['category']}")
        print(f"RESUMO: {result['error_summary']}")
        print(f"SEVERIDADE: {result['severity']}")
        print("\nHIPÓTESES:")
        
        for i, hypo in enumerate(result['hypotheses'], 1):
            print(f"\n{i}. {hypo['cause']}")
            print(f"   💡 Sugestão: {hypo['fix_suggestion']}")
            print(f"   📊 Confiança: {hypo['confidence_score'] * 100}%")
            
    except FileNotFoundError:
        print("❌ Erro: Arquivo de log não encontrado.")
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()