class TableCore:
    def calculate(self, data):
        number = data['number']
        table = {}
        for multiplier in range(1, 11):
            table[f'{number} x {multiplier} '] = number * multiplier

        return table
