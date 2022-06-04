class NotesCore:
    def notes(self, data):
        data = data['numbers']
        result = {
            'total': len(data),
            'max': float("-inf"),
            'min': float("inf"),
            'mean': sum(data)/len(data)
        }
        for note in data:
            if note > result['max']:
                result['max'] = note
            if note < result['min']:
                result['min'] = note

        return result
