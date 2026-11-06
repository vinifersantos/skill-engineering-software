# Continuidade do projeto e memória de engenharia

Memória operacional serve para evitar redescoberta. Não é uma desculpa para criar arquivos em todo repositório. Usar convenções existentes primeiro; criar/atualizar `PROJECT_MEMORY.md` apenas quando autorizado ou explicitamente requerido pelo fluxo do projeto.

## O que coletar antes de programar

1. Objetivo do produto e módulo alvo, definido pelo usuário e documentação real.
2. Contratos importantes (APIs, schema, eventos, interfaces públicas).
3. Decisões arquiteturais confirmadas, inclusive razões e alternativas rejeitadas.
4. Convenções: padrão de código, organizacao, testes, deploy, segurança.
5. Estado atual: branch, mudanças pendentes, testes e erros relevantes.

Omitir dados não relacionados a tarefa. Priorizar fontes primárias no repo e ferramentas conectadas autorizadas.

## Modelo opcional de `PROJECT_MEMORY.md`

```markdown
# Memória do projeto

## Objetivo e limites
- Produto e objetivos atuais: [confirmado por usuário/docs]
- Restrições e integrações que não podem quebrar: [...]

## Arquitetura validada
- Stack e versões identificadas: [fonte]
- Decisões duradouras: [decisão; motivo; evidência ou ADR]
- Invariantes/regras de negócio: [fonte e teste relacionado]

## Estado atual
- Trabalho em andamento: [escopo e última mudança]
- Verificações: [comando; resultado; data quando pertinente]
- Pendências e riscos: [com dono/aprovação se conhecido]

## Histórico relevante
- [data] [o que mudou e por que, com link/referência ao commit, PR ou arquivo]
```

## Regras de manutencao

- Acrescentar apenas fatos sustentados; marcar explicitamente hipóteses e itens não verificados.
- Atualizar decisões alteradas e preservar justificativas essenciais; evitar narrativa cronológica infinita.
- Nunca gravar chaves, secrets, tokens, PII, dumps, incidentes com dados de clientes ou detalhes confidenciais desnecessários.
- Não sobrescrever decisões do usuário; quando houver conflito, consultar as instruções atuais e sinalizar a divergencia.
- Repassar ao próximo agente o que fazer, o que não alterar e como validar.

## Handoff em tarefa longa

Registrar de modo breve:

```text
Objetivo / aceite:
Arquivos afetados:
Decisões fundamentadas:
Comandos executados e resultados:
O que falta:
Riscos e aprovações necessárias:
```

Se não houver persistencia disponível, fornecer esse resumo na resposta e deixar claro que ele **não foi gravado no repositório**.
