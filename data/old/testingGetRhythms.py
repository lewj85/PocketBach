import getRhythms as gr

d = [0,0,0,0,0,0,0,0,0,0,0]
beatsArr = [1,2]
timesig = [4,4]

for test in range(1000000):
    rhythms = gr.getRhythms(beatsArr, timesig)
    lenR = len(rhythms)
    d[lenR] += 1

print(d)


# beatsArr = [1,2,3,4]
# if len(rhythms) > 7 or onlyRhythms.count('2') > 1 or onlyRhythms.count('4') > 3 or onlyRhythms.count('8') > 4 or onlyRhythms.count('16') > 6:
# [0, 0, 0, 153800, 173074, 169930, 221768, 281428, 0, 0, 0]
# 60% chance to be odd

# beatsArr = [1,2,3,4]
# if len(rhythms) > 8 or onlyRhythms.count('2') > 1 or onlyRhythms.count('4') > 3 or onlyRhythms.count('8') > 5 or onlyRhythms.count('16') > 6:
# [0, 0, 0, 122486, 137283, 134978, 183334, 224162, 197757, 0, 0]
# 48% chance to be odd
# beatsArr = [1,2]
# [0, 176574, 235382, 117778, 103084, 176040, 132114, 59028, 0, 0, 0]
# 53% chance to be odd
