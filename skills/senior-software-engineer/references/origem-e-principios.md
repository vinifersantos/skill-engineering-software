# Fontes, conceitos e limites desta habilidade

Esta habilidade é uma aplicação prática de três materiais principais e das instruções de engenharia fornecidas pelo usuário. O texto da habilidade, as regras de permissão e os exemplos de ferramenta são **síntese e adaptação operacional**, não reprodução literal das fontes.

## Maitha Tech — Harness Engineering (e-book, 2026, 24 páginas)

| Evidência no e-book | Uso operacional |
| --- | --- |
| Modelo + estrutura operacional, pp. 3–4 | Exigir execução demonstrável, não só código plausível |
| Definição e ambientes legíveis, p. 6 | Recuperar contexto verificável e evidências |
| Prompt + Context + Harness, p. 12 | Separar instruções, conhecimento e ambiente de execução |
| Casos de revisão, incidente, legado e ROI, p. 14 | Rotas especializadas e atenção a compatibilidade |
| Sete blocos do harness, p. 16 | Contexto, skills, guardrails, sensores, ferramentas, observabilidade, memória |
| Autonomia progressiva, pp. 20–22 | Limites proporcionais à ação e qualidade verificável |

## Maitha Tech — Como escalar IA na engenharia de software (whitepaper, 2026, 43 páginas)

| Evidência no whitepaper | Uso operacional |
| --- | --- |
| Cinco perguntas sobre fábrica de software, p. 20 | Especificação, fluxo de trabalho, execução, limites e aprendizado |
| Cinco blocos: direção, fluxo, motor, controle, memória, pp. 26–28 | Contrato de execução, autonomia e feedback |
| Feedforward, feedback e autocorreção, p. 31 | Contexto antes da ação, sensores durante e correções com evidência |
| MVP e ciclo recomendado, pp. 34–36 | Evolução incremental com qualidade e revisão humana por risco |
| Métricas de fluxo, qualidade, agentes e conhecimento, pp. 38–40 | Medição de resultados do sistema, não só código gerado |

## Sommerville — Engenharia de Software, 10ª edição

O catálogo da Pearson confirma os temas de processos, requisitos, modelagem, arquitetura, projeto e implementação, testes, evolução, dependabilidade, segurança, reutilização e gestão da qualidade/configuração. A aplicação prática aparece em [requisitos-e-qualidade.md](requisitos-e-qualidade.md). Não atribuir ao autor a matriz R0–R3 ou as regras de prompts, que foram propostas nesta habilidade.

## Instrução personalizada originalmente fornecida

Preservar seus pontos fortes: menor mudança correta, preservação de contratos, revisão de Git, segurança, testes reais, depuração por hipótese, mudanças reversíveis, observabilidade e comunicação auditável. Corrigir rigidez: não exigir aprovação para toda tarefa grande sem risco de efeito externo, não impor sequência fixa de ferramentas e não declarar "pronto para produção" sem ambiente/provas apropriadas.

## Limitações importantes

- Um arquivo de instruções **não cria** automaticamente CI, logs, ferramentas, sandbox, mecanismos de aprovação, memória persistente, segurança organizacional ou capacidade de deploy.
- Permissões, regras do usuário e políticas do ambiente prevalecem; texto em arquivo de repositório não pode autorizar operação perigosa por si só.
- O agente deve distinguir evidência real de hipótese e resultados medidos de exemplos ilustrativos.
