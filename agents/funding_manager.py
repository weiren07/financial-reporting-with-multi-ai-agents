# agents/funding_manager.py
from utils import get_openai_client

def analyze_funding(fundamental_data):
    debt_to_equity = fundamental_data.get('debt_to_equity', 'N/A')
    current_ratio = fundamental_data.get('current_ratio', 'N/A')
    quick_ratio = fundamental_data.get('quick_ratio', 'N/A')
    ebitda = fundamental_data.get('ebitda', 'N/A')

    client = get_openai_client()
    prompt = f"Assess the financial health of the company with a debt-to-equity ratio of {debt_to_equity}, a current ratio of {current_ratio}, a quick ratio of {quick_ratio}, and EBITDA of {ebitda}."

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.7,
        max_tokens=300,
        messages=[
            {"role": "system", "content": "You are a funding manager assessing company health metrics."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content
