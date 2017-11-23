def distanceToTonal(distance, key = 'C'):
    distance %= 12
    if key == 'C':
        return {
            0 : 'a',
            1 : 'as',
            2 : 'b',
            3 : 'c',
            4 : 'cs',
            5 : 'd',
            6 : 'ds',
            7 : 'e',
            8 : 'f',
            9 : 'fs',
            10 : 'g',
            11 : 'gs'
        }.get(distance, -1)

