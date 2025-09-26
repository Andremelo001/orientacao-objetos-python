# 🐍 Programação Orientada a Objetos em Python

Este repositório contém meus estudos e exemplos práticos sobre **Programação Orientada a Objetos (POO)** em Python, cobrindo desde conceitos fundamentais até princípios avançados de design de software.

## 📚 Conteúdo do Repositório

### 🔰 Conceitos Fundamentais

#### [`conceitos_iniciais/`](./conceitos_iniciais/)
- **`pessoa.py`** - Exemplo básico de classe com atributos e métodos
- **`minha_classe.py`** - Demonstração de estrutura básica de classes
- **`csv_handler.py`** - Manipulação de arquivos CSV com POO

#### [`classes_abstratas/`](./classes_abstratas/)
- Implementação de classes abstratas
- Base para hierarquias de classes mais robustas

### 🏗️ Pilares da POO

#### [`encapsulamento_protegido/`](./encapsulamento_protegido/)
- Uso de atributos e métodos protegidos
- Controle de acesso aos dados da classe

#### [`metodos_privados/`](./metodos_privados/)
- Implementação de métodos privados
- Encapsulamento de lógica interna

#### [`getters_setters/`](./getters_setters/)
- **`run.py`** e **`run2.py`** - Propriedades e métodos de acesso
- Controle de acesso e validação de dados

#### [`herancas/`](./herancas/)
- **`run.py`** - Herança simples (Mamífero → Cachorro)
- **`run2.py`** - Exemplos avançados de herança
- Reutilização de código e especialização de classes

#### [`polimorfismo/`](./polimorfismo/)
- Métodos com mesmo nome e comportamentos diferentes
- Flexibilidade e extensibilidade do código

### 🔧 Conceitos Avançados

#### [`metodos_de_classe/`](./metodos_de_classe/)
- **`run.py`** - Métodos de classe (`@classmethod`)
- **`ativ_metodo_de_classe.py`** - Atividades práticas

#### [`variaveis_de_classe/`](./variaveis_de_classe/)
- Variáveis compartilhadas entre instâncias
- Diferença entre atributos de classe e instância

#### [`interfaces_exemplos/`](./interfaces_exemplos/)
- Implementação de interfaces em Python
- Contratos entre classes

### 🏛️ Relacionamentos entre Classes

#### [`associacao_de_classes/`](./associacao_de_classes/)
- Relacionamentos "usa um" entre objetos
- Acoplamento fraco entre classes

#### [`agregacao/`](./agregacao/)
- Relacionamento "tem um" (agregação)
- Objetos independentes que trabalham juntos

#### [`composicao/`](./composicao/)
- Relacionamento "é parte de" (composição)
- Dependência forte entre objetos

#### [`injecao_de_dependencias/`](./injecao_de_dependencias/)
- **`run.py`** - Padrão de injeção de dependências
- **`ativ_injecao_de_dependencias.py`** - Exercícios práticos
- Redução de acoplamento e maior testabilidade

### 🎯 Princípios SOLID

#### [`S_responsabilidade_unica/`](./S_responsabilidade_unica/)
- **`inicial.py`** - Código antes da aplicação do princípio
- **`single_responsability.py`** - Sistema de cadastro com responsabilidade única
- **SRP**: Uma classe deve ter apenas uma razão para mudar

#### [`O_principio_aberto_fechado/`](./O_principio_aberto_fechado/)
- **`run1.py`** e **`run2.py`** - Extensibilidade sem modificação
- **OCP**: Aberto para extensão, fechado para modificação

#### [`L_substituicao_de_liskov/`](./L_substituicao_de_liskov/)
- **`run.py`** e **`run2.py`** - Substituibilidade de objetos
- **LSP**: Objetos derivados devem ser substituíveis por seus objetos base

#### [`I_segregacao_de_interfaces/`](./I_segregacao_de_interfaces/)
- **`run.py`** e **`run2.py`** - Interfaces específicas e coesas
- **ISP**: Clientes não devem depender de interfaces que não usam

#### [`D_inversao_de_dependencias/`](./D_inversao_de_dependencias/)
- **`run.py`** - Inversão de dependências com interfaces
- **`elementos/`** - Estrutura modular com interfaces
- **DIP**: Dependa de abstrações, não de implementações concretas

## 🚀 Como Executar os Exemplos

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Andremelo001/orientacao-objetos-python.git
   cd orientacao-objetos-python
   ```

2. **Execute os exemplos:**
   ```bash
   # Exemplo básico
   python conceitos_iniciais/pessoa.py
   
   # Herança
   python herancas/run.py
   
   # Princípios SOLID
   python S_responsabilidade_unica/single_responsability.py
   ```

## 🎯 Conceitos Cobertos

- ✅ **Classes e Objetos**
- ✅ **Encapsulamento** (public, protected, private)
- ✅ **Herança** (simples e múltipla)
- ✅ **Polimorfismo** (sobrescrita de métodos)
- ✅ **Abstração** (classes abstratas e interfaces)
- ✅ **Composição e Agregação**
- ✅ **Métodos de Classe e Estáticos**
- ✅ **Properties (getters/setters)**
- ✅ **Princípios SOLID**
- ✅ **Injeção de Dependências**
- ✅ **Padrões de Design**

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Conceitos de POO Pura**
- **Type Hints** para melhor documentação
- **Princípios de Clean Code**

---

**Autor:** André Melo  
**Objetivo:** Consolidar conhecimentos em POO com Python através de exemplos práticos e bem estruturados.