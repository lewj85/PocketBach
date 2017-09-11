import requests
import time

url = 'https://api.hooktheory.com/v1/'
login = {"username": "myUsername",
	  "password": "myPassword"}

r = requests.post(url+'users/auth', data=login)
r.json()
'''
{'id': 136206, 'username': 'myUsername', 'activkey': 'myKey'}
'''

time.sleep(5)

activkey = 'myKey'
header = {"Authorization": "Bearer "+activkey}

# examples
# r = requests.get(url+'trends/nodes', headers=header)
# r.json()
#
# r = requests.get(url+'trends/nodes?cp=4', headers=header)
# r.json()
#
# r = requests.get(url+'trends/nodes?cp=4,6', headers=header)
# r.json()
# '''
# [{'chord_ID': '5', 'chord_HTML': 'V', 'probability': 0.456, 'child_path': '4,6,5'}, {'chord_ID': '1', 'chord_HTML': 'I', 'probability': 0.167, 'child_path': '4,6,1'}, {'chord_ID': '4', 'chord_HTML': 'IV', 'probability': 0.133, 'child_path': '4,6,4'}, {'chord_ID': '3', 'chord_HTML': 'iii', 'probability': 0.042, 'child_path': '4,6,3'}, {'chord_ID': '2', 'chord_HTML': 'ii', 'probability': 0.035, 'child_path': '4,6,2'}, {'chord_ID': '56', 'chord_HTML': 'V<sup>6</sup>', 'probability': 0.017, 'child_path': '4,6,56'}, {'chord_ID': '66', 'chord_HTML': 'vi<sup>6</sup>', 'probability': 0.011, 'child_path': '4,6,66'}, {'chord_ID': '67', 'chord_HTML': 'vi<sup>7</sup>', 'probability': 0.011, 'child_path': '4,6,67'}, {'chord_ID': '47', 'chord_HTML': 'IV<sup>7</sup>', 'probability': 0.009, 'child_path': '4,6,47'}, {'chord_ID': '5/6', 'chord_HTML': 'V/vi', 'probability': 0.008, 'child_path': '4,6,5/6'}, {'chord_ID': '5/5', 'chord_HTML': 'V/V', 'probability': 0.008, 'child_path': '4,6,5/5'}, {'chord_ID': '36', 'chord_HTML': 'iii<sup>6</sup>', 'probability': 0.008, 'child_path': '4,6,36'}, {'chord_ID': '164', 'chord_HTML': 'I<sup>6</sup><sub>4</sub>', 'probability': 0.007, 'child_path': '4,6,164'}, {'chord_ID': '27', 'chord_HTML': 'ii<sup>7</sup>', 'probability': 0.007, 'child_path': '4,6,27'}, {'chord_ID': '37', 'chord_HTML': 'iii<sup>7</sup>', 'probability': 0.005, 'child_path': '4,6,37'}, {'chord_ID': '642', 'chord_HTML': 'vi<sup>4</sup><sub>2</sub>', 'probability': 0.005, 'child_path': '4,6,642'}, {'chord_ID': 'b7', 'chord_HTML': '&#9837;VII', 'probability': 0.005, 'child_path': '4,6,b7'}, {'chord_ID': '16', 'chord_HTML': 'I<sup>6</sup>', 'probability': 0.005, 'child_path': '4,6,16'}, {'chord_ID': '664', 'chord_HTML': 'vi<sup>6</sup><sub>4</sub>', 'probability': 0.005, 'child_path': '4,6,664'}, {'chord_ID': 'b6', 'chord_HTML': '&#9837;VI', 'probability': 0.004, 'child_path': '4,6,b6'}, {'chord_ID': '57/5', 'chord_HTML': 'V<sup>7</sup>/V', 'probability': 0.003, 'child_path': '4,6,57/5'}, {'chord_ID': '57/2', 'chord_HTML': 'V<sup>7</sup>/ii', 'probability': 0.003, 'child_path': '4,6,57/2'}, {'chord_ID': '46', 'chord_HTML': 'IV<sup>6</sup>', 'probability': 0.003, 'child_path': '4,6,46'}, {'chord_ID': '57', 'chord_HTML': 'V<sup>7</sup>', 'probability': 0.002, 'child_path': '4,6,57'}, {'chord_ID': '364', 'chord_HTML': 'iii<sup>6</sup><sub>4</sub>', 'probability': 0.002, 'child_path': '4,6,364'}, {'chord_ID': 'L3', 'chord_HTML': 'iii', 'probability': 0.002, 'child_path': '4,6,L3'}, {'chord_ID': '17', 'chord_HTML': 'I<sup>7</sup>', 'probability': 0.002, 'child_path': '4,6,17'}, {'chord_ID': '564', 'chord_HTML': 'V<sup>6</sup><sub>4</sub>', 'probability': 0.002, 'child_path': '4,6,564'}, {'chord_ID': '5/3', 'chord_HTML': 'V/iii', 'probability': 0.002, 'child_path': '4,6,5/3'}, {'chord_ID': '7', 'chord_HTML': 'vii&deg;', 'probability': 0.002, 'child_path': '4,6,7'}, {'chord_ID': '264', 'chord_HTML': 'ii<sup>6</sup><sub>4</sub>', 'probability': 0.001, 'child_path': '4,6,264'}, {'chord_ID': '665', 'chord_HTML': 'vi<sup>6</sup><sub>5</sub>', 'probability': 0.001, 'child_path': '4,6,665'}, {'chord_ID': 'L7', 'chord_HTML': 'vii', 'probability': 0.001, 'child_path': '4,6,L7'}, {'chord_ID': '26', 'chord_HTML': 'ii<sup>6</sup>', 'probability': 0.001, 'child_path': '4,6,26'}, {'chord_ID': '57/6', 'chord_HTML': 'V<sup>7</sup>/vi', 'probability': 0.001, 'child_path': '4,6,57/6'}, {'chord_ID': '464', 'chord_HTML': 'IV<sup>6</sup><sub>4</sub>', 'probability': 0.001, 'child_path': '4,6,464'}, {'chord_ID': 'D47', 'chord_HTML': 'IVb7', 'probability': 0.001, 'child_path': '4,6,D47'}, {'chord_ID': 'C3', 'chord_HTML': '&#9837;iii', 'probability': 0.001, 'child_path': '4,6,C3'}, {'chord_ID': '242', 'chord_HTML': 'ii<sup>4</sup><sub>2</sub>', 'probability': 0.001, 'child_path': '4,6,242'}, {'chord_ID': 'b565', 'chord_HTML': 'v<sup>6</sup><sub>5</sub>', 'probability': 0.001, 'child_path': '4,6,b565'}, {'chord_ID': '7/3', 'chord_HTML': 'vii&deg;/iii', 'probability': 0.001, 'child_path': '4,6,7/3'}]
# '''

# pull all data for up to 4 chords in a row and store in a json file
filename = 'hooktheoryData.json'
f = open(filename, 'a')

# probabilities for first chord
myData = requests.get(url+'trends/nodes', headers=header)
f.write(str(myData.json()))
# save and reopen after each write because data-extraction will take over an hour and there may be errors...
f.close()
f = open(filename, 'a')

# probabilities after 1 chord
for chord1 in range(1,8):
    try:
        myData = requests.get(url+'trends/nodes?cp='+str(chord1), headers=header)
        f.write('\n\n'+str(myData.json()))
    except:
        f.write('\n\nUnable to extract for '+chord1)
    f.close()
    f = open(filename, 'a')
    time.sleep(5)

# probabilities after 2 chords
for chord1 in range(1,8):
    for chord2 in range(1,8):
        try:
            myData = requests.get(url+'trends/nodes?cp='+str(chord1)+','+str(chord2), headers=header)
            f.write('\n\n'+str(myData.json()))
        except:
            f.write('\n\nUnable to extract for '+chord1+','+chord2)
        f.close()
        f = open(filename, 'a')
        time.sleep(5)

# probabilities after 3 chords
for chord1 in range(1,8):
    for chord2 in range(1,8):
        for chord3 in range(1,8):
            try:
                myData = requests.get(url+'trends/nodes?cp='+str(chord1)+','+str(chord2)+','+str(chord3), headers=header)
                f.write('\n\n'+str(myData.json()))
            except:
                f.write('\n\nUnable to extract for '+chord1+','+chord2+','+ chord3)
            f.close()
            f = open(filename, 'a')
            time.sleep(5)

# probabilities after 4 chords
for chord1 in range(1,8):
    for chord2 in range(1,8):
        for chord3 in range(1,8):
            for chord4 in range(1,8):
                try:
                    myData = requests.get(url+'trends/nodes?cp='+str(chord1)+','+str(chord2)+','+str(chord3)+','+str(chord4), headers=header)
                    f.write('\n\n'+str(myData.json()))
                except:
                    f.write('\n\nUnable to extract for '+chord1+','+chord2+','+chord3+','+chord4)
                f.close()
                f = open(filename, 'a')
                time.sleep(5)

f.close()