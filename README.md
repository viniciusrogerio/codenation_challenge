# Desafio AceleraDev Codenation
[Introdução](https://github.com/viniciusrogerio/desafio_codenation#criptografia-de-júlio-césar) | [Regras](https://github.com/viniciusrogerio/desafio_codenation#regras)
***
### Criptografia de Júlio César

Das Criptografias mais curiosas na história da humanidade podemos citar a criptografia utilizada pelo grande líder militar romano Júlio César para comunicar com os seus generais. Essa criptografia se baseia na substituição da letra do alfabeto avançado um determinado número de casas. Por exemplo, considerando o número de casas = 3:

> Normal: a ligeira raposa marrom saltou sobre o cachorro cansado <br>
> Cifrado: `d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr`

### Regras
As mensagens serão convertidas para minúsculas tanto para a criptografia quanto para descriptografia. No nosso caso os números e pontos serão mantidos, ou seja:

> Normal: 1a.a<br> 
> Cifrado: `1d.d`

Escrever programa, em qualquer linguagem de programação, que faça uma requisição HTTP para a url abaixo:

https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=SEU_TOKEN

O resultado da requisição vai ser um JSON conforme o exemplo:

>{ "numero_casas": 10,<br>    "token":"token_do_usuario",<br>    "cifrado": "texto criptografado",<br>    "decifrado": "aqui vai o texto decifrado",<br>    "resumo_criptografico": "aqui vai o resumo" }

O primeiro passo é você salvar o conteúdo do JSON em um arquivo com o nome answer.json, que irá usar no restante do desafio.

Você deve usar o número de casas para decifrar o texto e atualizar o arquivo JSON, no campo decifrado. O próximo passo é gerar um resumo criptográfico do texto decifrado usando o algoritmo sha1 e atualizar novamente o arquivo JSON. OBS: você pode usar qualquer biblioteca de criptografia da sua linguagem de programação favorita para gerar o resumo sha1 do texto decifrado.

Seu programa deve submeter o arquivo atualizado para correção via POST para a API:

https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=SEU_TOKEN

OBS: a API espera um arquivo sendo enviado como multipart/form-data, como se fosse enviado por um formulário HTML, com um campo do tipo file com o nome answer. Considere isso ao enviar o arquivo.

O resultado da submissão vai ser sua nota ou o erro correspondente. Você pode submeter quantas vezes achar necessário, mas a API não vai permitir mais de uma submissão por minuto.
***
### [Veja aqui a solução proposta por mim](https://github.com/viniciusrogerio/desafio_codenation/blob/master/solucao_final.py)
***Atenção***: *o token em questão foi obtido através da [plataforma Codenation](https://www.codenation.dev/) exclusivamente pelos participantes do desafio, para tornar possível o acesso à API e a identificação do participante. Qualquer tentativa de acesso a partir do token que consta no código não será bem sucedida.*
***
Para dúvidas, críticas ou sugestões, me contatar pelo e-mail vinicius.stat@gmail.com
