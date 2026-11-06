# Sensores e gates de qualidade

Escolher verificações **a partir do repo real**, não por suposição. Não instalar dependências, acessar rede ou alterar infraestrutura apenas para executar checks sem considerar escopo e permissão. Preferir testes direcionados antes da suite completa; verificar o retorno de cada comando.

## Descoberta rápida

- Verificar manifests, arquivos de lock, scripts do projeto, instruções de contribuição e CI existente.
- Descobrir gerenciador de pacotes e versões usados; respeitar `packageManager`, lockfile, virtualenv, versão de runtime e ferramentas locais.
- Conferir se há testes ou comandos definidos antes de reportar que não existem.
- Comandos abaixo são **exemplos condicionais**, não receitas obrigatórias.

| Ecossistema | Sinais | Verificações possíveis conforme scripts e configuração |
| --- | --- | --- |
| Node.js / TypeScript | `package.json`, lockfile, `tsconfig.json` | testes registrados no package.json; `npm run lint` se existir; `npm run build` se existir; `tsc --noEmit` se configurado e instalado |
| Python | `pyproject.toml`, `requirements*.txt`, `pytest.ini` | `pytest` (ou testes selecionados), `ruff check`, `mypy` quando presentes/configurados |
| Go | `go.mod` | `go test ./...`, `go vet ./...` quando apropriados |
| Rust | `Cargo.toml` | `cargo test`, `cargo clippy` se disponível |
| Java / Kotlin | `pom.xml`, `build.gradle*` | `./mvnw test`, `./gradlew test`, build conforme tarefa e wrapper |
| C# / .NET | `*.sln`, `*.csproj` | `dotnet test`, `dotnet build` conforme ambiente |
| SQL / PostgreSQL | migrations, schema, queries, RLS | revisar diferenças de schema, constraints, permissões, índices e plano de rollback; exercitar apenas em ambiente isolado |
| Infra / CI | Terraform, YAML de pipelines, Dockerfiles | validação sintática, plan/dry-run somente quando seguros e disponíveis; não aplicar contra conta real sem autorização |

## Matriz por mudança

| Mudança | Gate mínimo | Gate adicional se risco elevado |
| --- | --- | --- |
| Correção simples | reproduzir defeito ou descrever critério + teste direcionado + diff | regressão do módulo afetado |
| Refatoração | testes existentes do módulo + contratos preservados | comparação de comportamento e observabilidade |
| API e integração | testes de payload, status, autenticação, erros e compatibilidade | contrato entre serviços, idempotência, timeouts, retries e limites |
| Auth e autorização | casos permitidos e negados, privilégio mínimo e segurança de sessão | teste de bypass, logs sem dados sensíveis, revisão humana |
| Banco | verificação de SQL, integridade e impacto de migração | plano de backup e rollback testado em staging; revisão de acesso e RLS quando aplicável |
| Frontend | estados de carregamento, erro, vazio e acessibilidade básica | responsividade, fluxo end-to-end e desempenho quando aplicável |
| Infra | diff e configurações validadas | revisão de blast radius, rollback e aprovação para efeito externo |

## Protocolo ao falhar

1. Registrar o comando, resultado é mensagem de erro útil.
2. Distinguir erro introduzido pela mudança de falha preexistente, indisponibilidade de dependências ou ambiente incorreto.
3. Corrigir causa verificável e reexecutar o teste relevante. Não reduzir severidade do erro para poder declarar sucesso.
4. Se o bloqueio persistir, terminar com status honesto e orientação reprodutível.

## Evidência no fechamento

Exemplo compacto:

```text
Mudança: adicionada validação de email em src/...
Verificação: npm test -- --runInBand  [PASSOU: 24 testes]
Verificação: npm run lint            [PASSOU]
Verificação: npm run build           [NÃO EXECUTADO: sem dependências instaladas]
Risco residual: validar fluxo com provedor externo em homologação
```

Adaptar ao projeto e **não inventar contagens ou resultados**. Se usuário pediu apenas explicacao, não apresentar testes fictícios.
