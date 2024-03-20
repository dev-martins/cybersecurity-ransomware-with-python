# Ransomware Simples em Python

Este projeto consiste em um simples ransomware desenvolvido em Python. Ele foi criado como parte de um teste prático para o curso de cibersegurança, demonstrando conceitos de criptografia e manipulação de arquivos.

## Funcionalidades

O ransomware é composto por dois scripts Python:

1. criptografador.py: Este script é responsável por criptografar um arquivo de texto fornecido utilizando o algoritmo de criptografia AES (Advanced Encryption Standard) no modo de operação CTR (Counter). Após a criptografia, o arquivo original é removido e um novo arquivo com a extensão ".ransomwaretroll" é criado, contendo os dados criptografados.

2. descriptografador.py: Este script é responsável por descriptografar um arquivo criptografado previamente pelo criptografador.py. Ele utiliza a mesma chave de criptografia para descriptografar o arquivo e restaurá-lo ao seu estado original. Após a descriptografia, o arquivo criptografado é removido e um novo arquivo descriptografado é criado.

## Utilização
Para utilizar este ransomware, siga as seguintes instruções:

Criptografar um arquivo:

Execute o script criptografador.py, fornecendo o nome do arquivo que deseja criptografar como argumento. Por exemplo:
```bash
python criptografador.py teste.txt
```

Certifique-se de ter uma chave de criptografia válida definida no código.
Descriptografar um arquivo:

Execute o script descriptografador.py, fornecendo o nome do arquivo criptografado como argumento. Por exemplo:
```bash
python descriptografador.py teste.txt.ransomwaretroll
```

Utilize a mesma chave de criptografia utilizada para criptografar o arquivo.
Aviso Legal
Este ransomware é fornecido apenas para fins educacionais e de aprendizado. O uso deste software para atividades ilegais ou maliciosas é estritamente proibido. O autor não se responsabiliza pelo uso indevido deste software.