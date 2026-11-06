# Requisitos, qualidade e evolução: ponte com a Engenharia de Software

Esta referência traduz conceitos clássicos de engenharia de software em **gates objetivos para agentes de código**. Apoia-se na organização temática de *Software Engineering*, 10ª edição, de Ian Sommerville: processos, engenharia de requisitos, modelagem, arquitetura, projeto/implementação, testes, evolução, dependabilidade/segurança e gestão da qualidade/configuração. Os itens operacionais abaixo são adaptações desta skill e não citações literais do autor.

## 1. Separar problema, requisitos e decisão técnica

Antes de alterar funcionalidade relevante, registrar:
- **Problema e objetivo:** quem é impactado e o que significa melhorar.
- **Funcionais:** comportamentos observáveis, regras de negócio, permissões e exceções.
- **Não funcionais:** segurança, privacidade, confiabilidade, disponibilidade, acessibilidade, desempenho, rastreabilidade e operação, conforme contexto.
- **Restrições:** stack, APIs, integrações, dados, padrões e prazos que não podem ser ignorados.
- **Aceite:** pelo menos um cenário feliz e casos negativos/limite quando aplicáveis, com forma concreta de verificar.

Não inventar precisão. Se o pedido é pequeno, usar somente os aspectos relevantes; não criar especificação formal de várias páginas.

## 2. Especificar antes de gerar em trabalhos grandes

A produção de software envolve descoberta/especificação, projeto, implementação, validação e evolução. Em tarefas amplas, transformar intenção em contrato técnico verificável, de preferência incremental:

```
Intenção -> requisito verificável -> solução candidata -> implementação mínima -> testes -> evidência -> aprendizado
```

Escolher a abordagem de processo pelo contexto, sem tratar modelo de ciclo de vida como ritual fixo. A cada incremento, revisar riscos e mudanças de requisitos.

## 3. Arquitetura e design deliberados

- Identificar responsabilidades, limites de módulos e interfaces antes de introduzir acoplamentos.
- Revisar compatibilidade e consumidores, especialmente em APIs públicas, eventos e schemas.
- Justificar abstrações por variabilidade ou complexidade demonstrada; não criar camadas para antecipar necessidades imaginadas.
- Para mudanças estruturais, registrar alternativa escolhida, custos, riscos e caminho de reversão.
- Preservar invariantes de sistemas legados até que seus motivos sejam conhecidos.

## 4. Testes ligados aos critérios de aceite

Usar uma matriz simples quando útil:

| Tipo | Evidência típica |
| --- | --- |
| Unitário | Regra e condição de borda isolada |
| Integração | Contrato entre componentes, persistência ou serviço |
| E2E | Jornada de negócio crítica quando há infraestrutura |
| Segurança | Acesso permitido/negado, entrada maliciosa, segredos protegidos |
| Operação | Saúde, falhas, logs/alertas e capacidade de reversão quando relevante |

Evitar testes que apenas reproduzem a implementação. Falhas anteriores não devem ser confundidas com efeitos do novo código.

## 5. Evolução e gestão da configuração

- Preservar mudanças pré-existentes e não atualizar dependências fora do escopo sem razão.
- Usar versionamento, testes de regressão, documentação de contratos e decisões arquiteturais quando proporcionais.
- Não afirmar conformidade, confiabilidade ou prontidão de produção sem evidências correspondentes.
- Quando houver métricas de fato disponíveis, avaliar retrabalho, tempo de ciclo, falhas e custo; não substituir valor por linhas de código geradas.

## Origem bibliográfica e limites

Ian Sommerville, *Software Engineering*, 10ª edição, Pearson. Capítulos e temas confirmados pelo catálogo da editora, sem incorporar trechos extensos protegidos por direitos autorais. A matriz de gates, a redação e as decisões de autonomia são propostas operacionais desta skill, **não termos formais atribuídos ao livro**.

- Catálogo: https://www.pearson.com/en-us/subject-catalog/p/systems-engineering-and-analysis/P200000003258/9780137503148
- Registro compartilhado pelo usuário: https://archive.org/details/sommerville-engenharia-de-software-10e
