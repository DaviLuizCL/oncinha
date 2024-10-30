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
---
2. **Criação do Ambiente de desenvolvimento python**
  ```bash
      python -m venv .venv
      source .venv/bin/activate
---
3. **Instalando dependências DENTRO DO AMBIENTE VIRTUAL**
  ```bash
      pip install -r requirements.txt
---
### Nesse momento, temos tudo que precisamos para tocar o projeto com MAKE

1. **Instalando dependências DENTRO DO AMBIENTE VIRTUAL**
    ```bash
        make compose

---
