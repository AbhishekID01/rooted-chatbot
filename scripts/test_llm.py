from services.slang_service import get_slang
from services.llm_service import generate_response

row = get_slang("sigma")

response = generate_response(
    question="What does sigma mean?",
    context=row
)

print("\n===== RESPONSE =====\n")
print(response)