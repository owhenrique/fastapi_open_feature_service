# TASK-010 — Introduzir Contexto de Avaliação para Feature Flags

## Objetivo

Evoluir o sistema de feature flags para permitir **avaliação por contexto**, mantendo o modelo simples e sem introduzir regras complexas prematuramente (policies, targeting avançado, etc.).

Ao final desta task, o sistema deve ser capaz de responder **se uma flag está habilitada considerando um contexto explícito**, mesmo que inicialmente esse contexto seja simples.

---

## Contexto

Atualmente, a decisão de `is_enabled` depende apenas do estado operacional da flag (`ON` / `OFF`).

Em sistemas reais, feature flags raramente são avaliadas de forma totalmente global. Normalmente, a decisão depende de algum **contexto**, como:

* ambiente (dev, staging, prod)
* aplicação cliente
* usuário ou grupo
* tenant

Nesta task, **não implementaremos regras complexas**, mas sim a **infraestrutura mínima** para suportar contexto no futuro.

---

## Escopo da Task

### 1. Introduzir o conceito de Context no domínio

Criar uma estrutura simples de contexto, por exemplo:

* `FlagContext`
* ou `EvaluationContext`

Esse contexto pode conter, inicialmente:

* `environment: str | None`
* `actor: str | None` (usuário, sistema, cliente, etc.)

**Observações importantes:**

* O contexto **não deve conter lógica de negócio**
* Deve ser apenas um **objeto de dados**

---

### 2. Atualizar o Service para aceitar contexto na avaliação

Adicionar um novo método no service:

* `is_enabled_with_context(identifier, context) -> bool`

Regras iniciais:

* Se a flag estiver `OFF`, retorna `False` independentemente do contexto
* Se a flag estiver `ON`, retorna `True`
* O contexto **ainda não altera o comportamento**, apenas participa da assinatura

O método atual `is_enabled` **não deve ser removido**.

Ele pode:

* delegar internamente para `is_enabled_with_context`, ou
* continuar existindo como um atalho sem contexto

---

### 3. Expor uma nova rota que aceite contexto

Criar uma nova rota, por exemplo:

```
GET /v1/feature-flags/{technical_key}/enabled/context
```

O contexto pode ser recebido via:

* query params (exemplo: `?environment=prod&actor=api`), ou
* body (caso você considere mais coerente)

A rota deve:

* validar a existência da flag
* delegar a decisão ao service
* retornar o seguinte payload:

```json
{
  "is_enabled": true
}
```

---

### 4. Testes

Adicionar testes cobrindo:

**Service**

* avaliação com contexto quando a flag está `ON`
* avaliação com contexto quando a flag está `OFF`

**Router**

* chamada com contexto válido
* flag inexistente

Os testes **não precisam validar lógica de contexto**, apenas garantir que:

* o contexto é aceito
* o fluxo de decisão está correto

---

## Critérios de Aceitação

* [ ] Existe uma estrutura clara representando o contexto
* [ ] O service possui um método explícito para avaliação com contexto
* [ ] O método atual `is_enabled` continua funcionando
* [ ] Existe uma nova rota para avaliação com contexto
* [ ] Testes cobrem service e router
* [ ] Nenhuma regra de negócio complexa foi introduzida
* [ ] O código permanece simples, legível e extensível

---

## Fora de Escopo

Esta task **não deve implementar**:

* policies
* segmentação por usuário
* cache
* regras condicionais
* percentuais de rollout

Esses temas ficam reservados para tasks futuras.

---

## Resultado Esperado

Ao final da TASK-010, o projeto terá evoluído de:

> feature flag global

para:

> feature flag avaliável por contexto

sem aumento significativo de complexidade arquitetural.
