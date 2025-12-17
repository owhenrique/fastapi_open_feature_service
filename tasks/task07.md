# TASK 07 — Update & Delete + Primeiros Testes de Verdade

## ✅ Parte 1 — Update

### Requisitos de Negócio
- [x] Só atualizar se a flag existir.
- [x] Só atualizar se `name` e `technical_key` não colidirem com outros registros.
- [x] Atualizar apenas os campos:
  - [x] `name`
  - [x] `technical_key`
  - [x] `operational_status`
- [x] `updated_at` deve refletir o update.
- [x] Nenhuma validação na rota.

### Requisitos de Arquitetura
- [x] Criar método no repository: `update(entity)`.
- [x] Criar método no service: `update(id, payload)`.
- [x] Criar DTO de entrada: `FeatureFlagUpdateSchema`.
- [x] Criar rota: `PUT /feature-flags/{id}`.

### Critérios de Aceite
- [ ] Update retorna a entidade atualizada.
- [ ] Conflitos levantam exceções de domínio (não HTTP diretamente).

---

## ✅ Parte 2 — Delete

### Requisitos de Negócio
- [ ] Só deletar se existir.
- [ ] Não permitir delete silencioso.
- [ ] Deleção permanente (soft-delete será futuro).

### Requisitos de Arquitetura
- [ ] Criar método no repository: `delete(session, entity)`.
- [ ] Criar método no service: `delete(id)`.
- [ ] Criar rota: `DELETE /feature-flags/{id}`.
- [ ] Service deve recuperar a entidade antes de deletar.

### Critérios de Aceite
- [ ] Resposta deve ser 204 (sem body).
- [ ] Se flag não existe → exceção de domínio.

---

## ✅ Parte 3 — Testes (nível iniciante)

### Infra de Testes
- [ ] Criar banco SQLite em memória.
- [ ] Criar fixture de sessão que:
  - [ ] Cria tabelas antes do teste.
  - [ ] Limpa depois.
  - [ ] Não usa o DB da aplicação.

### Testes obrigatórios
- [ ] Testar `repository.get_by_id`.
- [ ] Testar `service.read_one`.
- [ ] Testar rota `GET /feature-flags/{id}`.

### Regras
- [ ] Nada de integração completa do projeto.
- [ ] Nada de mocks pesados.
- [ ] Nada de TDD completo.
- [ ] Apenas consolidar a base.

### Critérios de Aceite
- [ ] `pytest` deve executar pelo menos 3 testes.
- [ ] Cada teste deve ter:
  - [ ] arrange (criar flag no banco em memória)
  - [ ] act
  - [ ] assert

---

## 📘 Parte 4 — Estudo

### Estudo obrigatório
- [ ] Ler capítulo sobre “Repositories” e “Service Layer” do *Cosmic Python*:
  - [ ] "Why do we need repositories?"
  - [ ] "Thin service layer"
  - [ ] “Do not mix domain logic with infrastructure”

- [ ] Ler documentação FastAPI — seção “Testing”:
  - [ ] Testing with SQL Database
  - [ ] dependency_overrides

---

## 🧩 Entregáveis esperados para o dia seguinte
- [ ] Explicar decisões de implementação
- [ ] Mostrar trechos importantes
- [ ] Descrever testes criados
- [ ] Relatar erros encontrados
- [ ] Informar tempo gasto por parte
