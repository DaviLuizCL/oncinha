# Oncinha, a prima do tigrinho


## Tutorial de Configuração do Projeto

### Tecnologias necessárias
  - docker -> 27.3.1+
  - docker-compose -> 1.29.2+
  - python 3.10.2
  - GNU Make 4.3+

#### Passos para Configuração

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/DaviLuizCL/oncinha.git
   cd oncinha
   ```

   

---
2. **Criação do Ambiente de desenvolvimento python**
  ```bash
  python -m venv .venv
  source .venv/bin/activate (ou .venv\Scripts\Activate se você utiliza Ruindows)
```
---
3. **Instalando dependências DENTRO DO AMBIENTE VIRTUAL**
  ```bash
  pip install -r requirements.txt
  ```
---
### Nesse momento, temos tudo que precisamos para tocar o projeto com MAKE

4. **Instalando dependências DENTRO DO AMBIENTE VIRTUAL**
    ```bash
    make compose
    ```

---

### Para rodar SEM o make, (windows user be like)


1. **Buildar a aplicação**
  ```bash
  docker-compose build
  ```
---

2. **Rodar a aplicação**
 ```bash
docker-compose up
 ```
---
3. **Rezar para dar certo**
 ```bash
ave Maria (5 séries de 10)
  ```


---
---
### Passo a passo para trabalhar no projeto

1.**Pegar as mudanças da MAIN** 
  ```bash
     git pull (estando na main)
   ```

2. **Trocar a Branch para a sua**
   ```bash
     git checkout -b seunome/oqvocevaifazer (estando na main)
   ```


### Fez tudo?

3. **Adicione tudo** 
  ```bash
     git add . (estando na sua branch)
  ```
4. **Comitando alterações**
   **Padrão de commit**
   - A mensagem de commit DEVE ser prefixado com um tipo, que consiste em um substantivo, feat, fix, etc., seguido por um escopo OPCIONAL, e OBRIGATÓRIO terminar com dois-pontos e um espaço.
   - O tipo feat DEVE ser usado quando um commit adiciona um novo recurso ao seu aplicativo ou biblioteca.
   - O tipo fix DEVE ser usado quando um commit representa a correção de um problema em seu aplicativo ou biblioteca.
   - Um escopo PODE ser fornecido após um tipo. Um escopo DEVE consistir em um substantivo que descreve uma seção da base de código entre parênteses, por exemplo, fix(parser): 
   - Uma descrição DEVE existir depois do espaço após o prefixo tipo/escopo. A descrição é um breve resumo das alterações de código, por exemplo, fix: problema na interpretação do array quando uma string tem vários espaços.
   - Para mais informações consulte: https://www.conventionalcommits.org/pt-br/v1.0.0-beta.4/
   ```bash
      git commit -m "Sua mensagem"
   ```

5. **Empurrando pra main**
**Certifique o nome da Branch antes**
```bash
git push origin seunome/oqvocevaifazer
```
6. **Abrindo Pull Request**
- Abra seu Github
- Repositório da oncinha
- lá terá as opções de abrir o pull request
- faça o pull request, e seja feliz