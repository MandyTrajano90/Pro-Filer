# ProFiler 🪲


  
<details>
<summary><strong>🧑‍💻 O que foi desenvolvido</strong></summary>

Uma aplicação com uma interface de linha de comando (CLI) que recebe como entrada um caminho (diretório ou arquivo) e gera um relatório com informações sobre o caminho informado.

É preciso corrigir os bugs e implementar os testes para garantir que a aplicação funcione corretamente. Apliquei tudo o que aprendi sobre debugging e testes automatizados em Python!

</details>

<details>
  <summary><strong>:memo: Habilidades desenvolvidas </strong></summary>

Neste projeto, aprendi a:

- Encontrar bugs no código de uma aplicação escrita em Python;
- Corrigir bugs no código de uma aplicação escrita em Python;
- Criar testes para uma aplicação escrita em Python;
- Utilizar o `pytest` para criar testes automatizados em uma aplicação escrita em Python.

</details>



## Instalando o projeto

1. Clone o repositório

- Use o comando: `git clone git@github.com:MandyTrajano90/Pro-Filer.git`
- Entre na pasta do repositório que você acabou de clonar:
  - `cd Pro-Filer`

2. Instale as dependências

    - Siga os passos do tópico [**🏕️ Ambiente Virtual**]

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary>
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

</details>

<details>
<summary><strong>🎛 Linter</strong></summary>

Para garantir a qualidade do código, utilizei nesse projeto o linter `Flake8`. Assim o código fica alinhado com as boas práticas de desenvolvimento, sendo mais legível e de fácil manutenção! Para poder executar o `Flake8`, certifique-se de ter seguido os passos do tópico [**🏕️ Ambiente Virtual**] dentro do repositório.

Para rodá-lo localmente no repositório, execute o comando a seguir:

```bash
python3 -m flake8
```

Se a análise do `Flake8` encontrar problemas no seu código, tais problemas serão mostrados no seu terminal. Se não houver problema no seu código, nada será impresso no seu terminal.

</details>

<details>
  <summary><strong>🛠 Testes</strong></summary>

  👀 Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  python3 -m pytest
  ```

  O arquivo `pyproject.toml` já configura corretamente o `pytest`. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv --continue-on-collection-errors
  ```

  O `pytest` possui diversos parâmetros que podem ser utilizados para executar os testes de diferentes formas. Alguns exemplos são:

  ```bash
  python3 -m pytest tests/test_nome_do_arquivo.py  # Executa todos os testes do arquivo de testes especificado
  python3 -m pytest tests/test_nome_do_arquivo.py::test_nome_do_teste  # Executa apenas o teste especificado
  python3 -m pytest -k expressao  # Executa apenas os testes que contém a expressão informada como substring
  python3 -m pytest -x  # Executa os testes até encontrar o primeiro erro
  ```

  Você pode combinar os parâmetros para executar os testes da forma que desejar! Para mais informações, consulte a [documentação do pytest](https://docs.pytest.org/en/7.3.x/contents.html).
  </details>

  <details>
<summary><strong> ⚠️Para executar a aplicação</strong></summary>

1. Siga os passos do tópico [**🏕️ Ambiente Virtual**]
2. Configure o auto-complete da aplicação com o comando `pro-filer --install-completion` e reinicie o terminal;
3. Execute o comando `pro-filer` seguido de um caminho (diretório ou arquivo) e uma ação. Por exemplo:

```bash
pro-filer . preview
```

![pro-filer preview](./images/pro-filer-preview.gif)

A aplicação já está funcional!
 </details>
</details>


## 👁️ Dê uma olhada no código



https://github.com/user-attachments/assets/6007a343-5231-4fe7-bbd6-2a1a8eb39c27


<!-- Olá, Tryber!
Esse é apenas um arquivo inicial para o README do seu projeto.
É essencial que você preencha esse documento por conta própria, ok?
Não deixe de usar nossas dicas de escrita de README de projetos, e deixe sua criatividade brilhar!
:warning: IMPORTANTE: você precisa deixar nítido:
- quais arquivos/pastas foram desenvolvidos por você; 
- quais arquivos/pastas foram desenvolvidos por outra pessoa estudante;
- quais arquivos/pastas foram desenvolvidos pela Trybe.
-->
