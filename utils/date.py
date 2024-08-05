from datetime import datetime


def get_current_month_year():
    # Obtém a data e hora atuais
    now = datetime.now()
    # Formata o mês e o ano no formato desejado
    formatted_date = now.strftime("%m / %Y")
    return formatted_date

# Exemplo de uso
current_month_year = get_current_month_year()
print(current_month_year)
