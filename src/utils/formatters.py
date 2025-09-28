def format_price(price):
    try:
        if isinstance(price, str):
            numeric_price = float(price.strip().replace('.', '').replace(',', '.'))
        else:
            numeric_price = float(price)

        formatted_str = f"{numeric_price:,.2f}"
        formatted_str = formatted_str.replace(',', '@').replace('.', ',').replace('@', '.')

        return f"R$ {formatted_str}"

    except (ValueError, TypeError):
        return "R$ 0,00"
