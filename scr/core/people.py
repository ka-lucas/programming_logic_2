class PeopleCore:
    def analysis(self, data):
        result = {
            'total': 0,
            'men': 0,
            'woman': 0
        }

        for person in data:
            gender = person['gender'].upper()
            if gender not in ['M', 'F']:
                return f'invalid gender {gender}'

            if person['age'] > 18:
                result['total'] += 1
            if person['gender'] == 'M':
                result['men'] += 1
            if person['gender'] == 'F' and person['age'] < 20:
                result['woman'] += 1

        return result
