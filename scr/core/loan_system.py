class LoanSystemCore:
    def calculate(self, data):
        salary = data['salary']
        house_value = data['house_value']
        years = data['years']

        limit = salary * 30 / 100
        parcel = house_value / (years * 12)

        if parcel > limit:
            return f'A parcela {parcel} excedeu 30% de {salary} que e {limit}'
        else:
            return f'Emprestimo Aprovado. Sua parcela sera de {parcel} por mes'
