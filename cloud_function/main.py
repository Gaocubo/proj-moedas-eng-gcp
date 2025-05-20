import requests
from flask import jsonify

def get_currency_data(request):
    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
    
    try:
        response = requests.get(url)
        data = response.json()

        # Seleciona algumas informações específicas para retornar
        resultado = {
            'USD': data['USDBRL']['bid'],
            'EUR': data['EURBRL']['bid'],
            'BTC': data['BTCBRL']['bid']
        }

        return jsonify(resultado)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

