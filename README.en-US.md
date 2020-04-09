[Versão em português](https://github.com/viniciusrogerio/desafio_codenation/README.md)
# AceleraDev Codenation Challenge
[Introduction](https://github.com/viniciusrogerio/desafio_codenation#criptografia-de-júlio-césar) | [Rules](https://github.com/viniciusrogerio/desafio_codenation#regras) | [Instructions](https://github.com/viniciusrogerio/desafio_codenation#instruções) | [Solution](https://github.com/viniciusrogerio/desafio_codenation#veja-aqui-a-solução-proposta-por-mim) | [Contact](https://github.com/viniciusrogerio/desafio_codenation#contato)
***
### The Caesar Cipher

From the most curious ciphers in the history of humanity, we can quote the one used by the great roman military leader Julius Caesar to communicate with his generals. This cryptography is based on replacing the letters with their correspondent letter ahead, given a certain number of steps. For instance, let the number of steps = 12:

> Decrypted: code never lies, comments sometimes do. ron jeffries <br>
> Encrypted: `oapq zqhqd xuqe, oayyqzfe eayqfuyqe pa. daz vqrrduqe`

### Rules
The messages must be converted to lowercase as for encrypting as for decrypting. In our case, numbers and punctuation marks must be kept, i.e.:

> Decrypted: 1a.a<br> 
> Encrypted: `1d.d`

Write a program in any programming language which performs a HTTP requisition to the url below:

https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN

The result of the request will be a JSON according to the example:

>{ "numero_casas": 10,<br>    "token":"token_do_usuario",<br>    "cifrado": "texto criptografado",<br>    "decifrado": "aqui vai o texto decifrado",<br>    "resumo_criptografico": "aqui vai o resumo" }<br>
***Note***: *Those JSON parameters have been written in brazilian portuguese, as it's the original idiom of the company who launched this challenge.*
### Instructions

The first thing you wanna do is saving the JSON content in a file named answer.json, which will be further used in the following parts of the challenge.

You should use the number of steps to decrypt the message and update the JSON file value correspondent to key "decifrado". Next step is to generate a cryptographic digest of the decrypted text using the sha1 algorithm and update the JSON file again. Note: you can use any cryptography library of your favorite programming language to generate the digest.

Your program must submit the updated file for revision via POST to the API:

https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN

Warning: the API expects the file to be sent as multipart/form-data, as if it was sent by an HTML form, with a file type field named answer. Consider this when submitting the file.

The result will be your score or the correspondent error. You can submit as many times as you feel necessary, but the API won't let you submit more than once in a minute.
***
### [See my solution](https://github.com/viniciusrogerio/desafio_codenation/blob/master/solucao_final.py)
***Attention***: *the present token was obtained through the [Codenation platform](https://www.codenation.dev/) exclusively by those running the challenge, in order to access the API and identify the participant. Any attempt of access using the example token on the code won't be sucessful.*
***

### Contact me
For any doubts, comments or suggestions, please contact me on my e-mail vinicius.stat@gmail.com<br>
LinkedIn: https://www.linkedin.com/in/viniciusrogerio/
