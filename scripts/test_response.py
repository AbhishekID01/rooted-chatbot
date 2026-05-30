from services.slang_service import get_slang
from services.response_service import build_slang_response

row = get_slang("sigma")

response = build_slang_response(row)

print(response)