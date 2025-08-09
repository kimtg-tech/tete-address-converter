# address_converter/views.py

from django.shortcuts import render
from .api_client import get_address_info

def address_converter_view(request):
    # POST 요청 (폼 제출 시)
    if request.method == 'POST':
        addresses_raw = request.POST.get('addresses', '')
        # 엔터(newline) 기준으로 주소 분리, 빈 줄은 제외
        address_list = [addr.strip() for addr in addresses_raw.splitlines() if addr.strip()]

        results = []
        for addr in address_list:
            info = get_address_info(addr)
            result_row = {
                'input_address': addr,
                'converted_address': info.get('address', ''),
                'status': info['status'],
                'status_message': '성공' if info['status'] == 'success' else f"실패 ({info['reason']})"
            }
            results.append(result_row)

        return render(request, 'address_converter/result.html', {'results': results})

    # GET 요청 (첫 페이지 접속 시)
    return render(request, 'address_converter/index.html')