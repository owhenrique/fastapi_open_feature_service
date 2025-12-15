# Task 009 — Desacoplamento de Domínio + Nova Funcionalidade

## Contexto

Atualmente, o domínio de *Feature Flags* está fortemente acoplado ao ORM (`SQLModel`). O `FlagService` cria diretamente instâncias do modelo persistente (`Flag`), e os repositórios operam exclusivamente sobre esse modelo.

Embora funcional, esse desenho dificulta:

* Evolução do domínio sem impacto direto na persistência
* Testes unitários puros (sem banco)
* Substituição futura de ORM ou fonte de dados

Além disso, até o momento o sistema não possui **nenhuma regra de negócio que vá além de CRUD**, o que limita a validação da arquitetura proposta.

Esta task propõe **uma refatoração estrutural** + **uma funcionalidade nova**, forçando o domínio a se expressar de forma mais rica.

---

## Objetivos

### 1️⃣ Refatoração — Desacoplamento do Modelo de Domínio

Criar uma separação clara entre:

* **Entidade de domínio** (pura, sem ORM)
* **Modelo de persistência** (SQLModel)

O serviço **não deve mais instanciar diretamente** o modelo persistente.

---

### 2️⃣ Nova Funcionalidade — Avaliação de Feature Flag

Implementar uma funcionalidade que permita **avaliar se uma feature flag está ativa**, considerando regras de domínio.

Essa funcionalidade **não deve ser apenas um wrapper de leitura**.

---

## Escopo Detalhado

### 🔧 Parte A — Refatoração (Obrigatória)

#### A.1 — Entidade de Domínio

* Criar uma entidade de domínio para Feature Flag (ex: `FeatureFlag`)
* Essa entidade:

  * **Não pode** depender de `SQLModel`, `ORM`, `Session` ou FastAPI
  * Deve conter apenas:

    * Dados
    * Regras de domínio

📌 Exemplo de responsabilidades esperadas:

* Representar o estado da flag
* Expor comportamento (métodos), não apenas atributos

---

#### A.2 — Modelo de Persistência

* O modelo atual (`Flag`) deve se tornar explicitamente um **modelo de persistência**
* Ele pode continuar usando `SQLModel`
* Ele **não deve conter lógica de negócio**

---

#### A.3 — Repositório como Boundary

* O repositório passa a ser responsável por:

  * Converter modelo persistente → entidade de domínio
  * Converter entidade de domínio → modelo persistente

📌 O `FlagService`:

* Não pode importar o modelo ORM
* Deve trabalhar **exclusivamente com a entidade de domínio**

---

### ✨ Parte B — Nova Funcionalidade (Obrigatória)

#### B.1 — Regra de Negócio: Avaliação da Flag

Criar uma operação de domínio que responda:

> "Essa feature flag está ativa?"

Essa avaliação deve considerar **regras explícitas**, por exemplo:

* O status operacional da flag
* Outras condições que façam sentido no domínio (ex: flag desativada por padrão, futura expansão)

📌 A regra **deve viver no domínio**, não no service nem no router.

---

#### B.2 — Exposição via Service

* O `FlagService` deve expor um método para essa avaliação
* O service apenas **orquestra**, não decide

---

#### B.3 — Endpoint Novo

Criar um novo endpoint para avaliação da flag.

📌 Requisitos gerais:

* Não deve quebrar endpoints existentes
* Deve retornar um payload simples e explícito

---

## Testes

### Testes Obrigatórios

* Testes **unitários do domínio** (sem banco, sem FastAPI)
* Testes do service para a nova funcionalidade
* Teste do endpoint novo

📌 Pelo menos um teste deve provar que:

* A regra de avaliação funciona **independente da persistência**

---

## Critérios de Aceitação

### Refatoração

* [ ] Nenhuma regra de negócio no modelo ORM
* [ ] Service não importa o modelo persistente
* [ ] Domínio não depende de infraestrutura
* [ ] Repositório atua como boundary

### Funcionalidade Nova

* [ ] Existe uma operação clara de domínio para avaliação da flag
* [ ] O service apenas delega a decisão
* [ ] Existe endpoint específico para avaliação

### Testes

* [ ] Testes unitários do domínio existem
* [ ] Nova funcionalidade está coberta por testes
* [ ] Testes existentes continuam passando

---

## Fora de Escopo

* Event sourcing
* Feature flag por usuário
* Integração com cache
* Autorização/autenticação

---

## Observações Finais

* **Não implemente soluções genéricas demais**
* Prefira clareza a abstração
* Justifique decisões no código, se necessário

Esta task não é sobre quantidade de código, mas sobre **clareza de limites arquiteturais**.
