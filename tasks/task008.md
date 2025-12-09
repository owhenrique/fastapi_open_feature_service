# TASK-008 — Refatoração Estrutural + BaseClasses + Correções Arquiteturais

## 🎯 Objetivo Geral
Garantir consistência arquitetural, eliminar duplicações, corrigir incoerências e introduzir abstrações fundamentais (BaseRepository e BaseService), preparando o projeto para maior escala e para as tasks mais avançadas.

---

## 🧩 Parte 1 — Criação das BaseClasses

### BaseRepository
- [x] Criar `BaseRepository` com métodos genéricos:
  - [x] `add(session, entity)`
  - [x] `get_by_id(session, id)`
  - [ ] `delete(session, entity)`
- [x] Garantir que as classes concretas (ex.: `FeatureFlagRepository`) **estendem** a base.
- [ ] Mover lógica duplicada ou acoplada para a base.
- [x] Não incluir lógica de domínio na base (somente persistência).

### BaseService
- [ ] Criar `BaseService` com responsabilidades comuns:
  - [ ] Guardar a sessão (session)
  - [ ] Padronizar retorno/fluxo das operações
- [ ] Evitar lógica de negócio na base.
- [ ] `FeatureFlagService` deve herdar dela.

---

## 🧩 Parte 2 — Refatoração no FeatureFlagRepository
- [ ] Remover código duplicado
- [ ] Garantir consistência com as novas BaseClasses
- [ ] Conferir nome de métodos (ex.: `get_by_name`, `get_by_technical_key`)
- [ ] Verificar retorno e consistência de exceções

---

## 🧩 Parte 3 — Refatoração no FeatureFlagService
- [ ] Remover responsabilidades que pertencem ao repository
- [ ] Centralizar validações de negócio
- [ ] Assegurar que nenhum método viole:
  - [ ] "Service não pode conter SQL"
  - [x] "Repository não pode conter regras de negócio"
- [x] Revisar mensagens e códigos de exceção

---

## 🧩 Parte 4 — Ajustes nas Rotas
- [ ] Verificar nomes das rotas
- [ ] Verificar assinaturas das path operations
- [x] Garantir que **nenhuma** validação de negócio esteja nas rotas
- [x] Garantir padronização do uso de `HTTPException`

---

## 🧩 Parte 5 — Ajustes de Consistência Geral
- [x] Padronizar nomes dos arquivos:
  - [x] Nada verboso demais
  - [ ] Não usar nomes inconsistentes (ex.: `repositorie`)
- [x] Ajustar imports quebrados
- [ ] Verificar docstrings
- [ ] Revisar exceções criadas na task 006
- [ ] Revisar DTOs de entrada/saída

---

## 🧩 Parte 6 — Definição do Padrão de Entidade
- [ ] Revisar se o modelo está com:
  - [ ] Campos obrigatórios bem definidos
  - [ ] Campos opcionais claros
  - [x] Datas (`created_at`, `updated_at`) consistentes

---

## 🧩 Parte 7 — Entregáveis esperados
- [ ] Explicar todas as refatorações feitas
- [ ] Apontar inconsistências encontradas
- [ ] Mostrar antes/depois de trechos importantes
- [ ] Informar se baseclasses ajudaram ou atrapalharam
- [ ] Indicar dúvidas ou problemas encontrados

---

## 🔥 Observações finais
- Nada de criar testes novos.
- Nada de implementar novas features.
- Foque apenas em correção, limpeza e padronização.
- O objetivo é preparar terreno para tasks mais complexas.
