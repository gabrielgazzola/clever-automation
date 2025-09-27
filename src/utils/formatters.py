import locale

try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("Alerta: Locale 'pt_BR.UTF-8' não suportado. Usando o locale padrão do sistema.")

def format_price(price):
    try:
        if isinstance(price, (int, float)):
            numeric_price = float(price)

        elif isinstance(price, str):
            normalized_price = price.strip().replace('.', '').replace(',', '.')
            if not normalized_price:
                raise ValueError("String vazia não é um número válido")
            numeric_price = float(normalized_price)

        else:
            raise TypeError("Tipo de entrada não suportado")

        return locale.currency(numeric_price, grouping=True)

    except (ValueError, TypeError):
        return locale.currency(0, grouping=True)
