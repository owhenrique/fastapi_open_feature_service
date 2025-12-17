# ✅ TASK 09 — Avaliação de Feature Flags + Evolução Funcional


## 🎯 Objetivo Geral

Evoluir o sistema de Feature Flags com **comportamento de domínio real**, indo além do CRUD, adicionando operações que representem como a aplicação cliente consome flags no dia a dia.

A task foca em **implementação funcional nova**, com pequenas melhorias de organização e consistência, sem refatorações estruturais profundas.

---

## 🧩 Parte 1 — Avaliação de Flag (`is_enabled`)

### Requisitos de Negócio

* O sistema deve permitir avaliar se uma Feature Flag está ativa ou não.
* A avaliação é baseada em:

  * existência da flag
  * valor do campo `operational_status`
* Flags inexistentes **não são tratadas como `false` silenciosamente** — devem gerar erro explícito.

### Requisitos de Arquitetura

* Criar método no **service**:

  * `is_enabled(technical_key: str) -> bool`

* O método deve:

  1. Buscar a flag pelo `technical_key`
  2. Lançar exceção de domínio se não existir
  3. Retornar `True` ou `False` conforme o status operacional

* Criar rota dedicada:

```
GET /feature-flags/{technical_key}/enabled
```

* A rota deve retornar:

```json
{
  "is_enabled": true
}
```

### Critérios de Aceite

* Flag ON → retorna `true`
* Flag OFF → retorna `false`
* Flag inexistente → erro HTTP derivado de exceção de domínio
* Nenhuma regra de negócio na rota

---

## 🧩 Parte 2 — Endpoint de Leitura Simples (Client-Friendly)

> Subtarefa pensada para uso real por aplicações clientes.

### Requisitos de Negócio

* Criar um endpoint simplificado para consumo externo, voltado a clientes que **não precisam da flag inteira**.

### Requisitos de Arquitetura

* Criar rota:

```
GET /feature-flags/{technical_key}/value
```

* A resposta deve conter apenas:

```json
{
  "technical_key": "example-flag",
  "is_enabled": true
}
```

* A rota deve reutilizar o método `is_enabled` do service (não duplicar lógica).

### Critérios de Aceite

* Nenhuma lógica duplicada entre rotas
* Service concentra toda a regra de avaliação
* Exceções continuam sendo de domínio

---

## 🧩 Parte 3 — Testes da Nova Funcionalidade

### Objetivo dos Testes

Garantir que a nova funcionalidade seja confiável e preparada para uso real.

### Escopo

Testar apenas:

* `service.is_enabled`
* rota `/enabled`
* rota `/value`

### Regras

* Usar o banco em memória já existente
* Sem mocks
* Sem TDD obrigatório

### Critérios de Aceite

* Pelo menos:

  * 1 teste para flag ON
  * 1 teste para flag OFF
  * 1 teste para flag inexistente

---

## 🧩 Parte 4 — Pequenas Melhorias de Consistência

### Itens Esperados

* Garantir que:

  * nomes de métodos estejam coerentes entre service e repository
  * exceções tenham mensagens consistentes
  * responses sigam um padrão claro

> ⚠️ **Não é uma refatoração estrutural** — apenas ajustes locais de clareza.

---

## 📦 Entregáveis Esperados

* Código funcional implementado
* Testes da nova funcionalidade
* Explicação curta sobre:

  * decisões tomadas
  * o que faria diferente em um cenário maior

---

## 🧠 Observação do Tech Lead

Esta task representa a transição de *"CRUD de cadastro"* para *"comportamento de domínio"*.

A decisão de **não desacoplar o ORM agora é correta** — esse tipo de arquitetura só vale a pena quando a complexidade real exige.

O foco aqui é **clareza, utilidade e evolução incremental**.
