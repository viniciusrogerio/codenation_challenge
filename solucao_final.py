import requests
import json
import string
import hashlib

# Getting data from Codenation API using personal Token
my_token = '049c9c550834eadd24884a00015716df5e625ff5'
r = requests.get(f'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token={my_token}')

# Using r.json() to further dump in proper format
json_data = r.json()

# Creating a new .json file named answer.json
json_file = open('answer.json','w',encoding='utf-8')

# Writing the json data we requested
json_file.seek(0)
json.dump(json_data,json_file)

# Storing needed infos
steps = json_data["numero_casas"]
encrypted = json_data["cifrado"].lower()
decrypted = ''

# Decrypting
alphabet = string.ascii_lowercase

for char in encrypted:
	if char in alphabet:
		current_index = alphabet.index(char)
		new_index = current_index - steps
		decrypted += alphabet[new_index]
	else:
		decrypted += char

decrypted = decrypted.lower()

# Now updating the .json file with the decrypted text
json_data["decifrado"] = decrypted
json_file.seek(0)
json.dump(json_data,json_file)

# Generating a digest and then updating the .json file again
json_data["resumo_criptografico"] = hashlib.sha1(decrypted.encode('utf-8')).hexdigest()
json_file.seek(0)
json.dump(json_data,json_file)

json_file.close()

# Submitting solution via POST
solution_file = open('answer.json','r')
answer = {"answer":solution_file}
response = requests.post(f'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token={my_token}', files = answer)
print(response.text)