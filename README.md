# Agenda de Contatos com Envio de Mensagens via WhatsApp

Este projeto permite cadastrar contatos e enviar mensagens automaticamente para eles através do WhatsApp utilizando a biblioteca `pywhatkit`.

## Funcionalidades

- **Cadastrar Contatos**: Adicione contatos à sua agenda com nome e número de telefone (incluindo código de país).
- **Enviar Mensagens**: Envie mensagens para os contatos cadastrados. O sistema aguarda um tempo antes de enviar a mensagem via WhatsApp.
- **Agenda de Contatos**: Armazene seus contatos e utilize-os para enviar mensagens de forma rápida e eficiente.

## Como usar

1. **Instalação das dependências**:
   O script utiliza a biblioteca `pywhatkit`. Para instalá-la, execute:

```bash
pip install pywhatkit
```

2.  **Rodando o script**:
```
• Execute o script Python no seu terminal.
• Escolha uma das opções no menu:
• Adicionar contato: Insira o nome e o número do contato.
• Enviar mensagem: Escolha um contato da agenda e envie uma mensagem para ele.
• Sair: Encerra o programa.
```


## Exemplo de Uso
```
1. Adicionar contato
2. Enviar mensagem
3. Sair

↳ Escolha uma opção: 1
↳ Digite o nome do contato: João
↳ Digite o telefone do contato (com o código do país, exemplo: +55XXXXXXXXXXX): +5511999999999
↳ Contato João adicionado com sucesso!

Depois aparecerá novamente o menu:
1. Adicionar contato
2. Enviar mensagem
3. Sair

↳ Escolha uma opção: 2
↳ Contatos cadastrados:
- João

↳ Digite o nome do contato para enviar a mensagem: João
↳ Você escolheu o contato: João - +5511999999999
↳ Digite a mensagem que deseja enviar: Olá João, tudo bem?
↳ Aguardando 10 segundos para enviar a mensagem...
↳ Mensagem enviada para João!
