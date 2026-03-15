# Site Guidelines

Estas diretrizes definem o comportamento editorial e estrutural do site como um todo.

---

## Regras gerais

- O site representa Amadeu Beraldin.
- O tom deve ser técnico, honesto, claro e organizado.
- O site não deve parecer uma página de marketing tradicional.
- O site deve transmitir experimentação real, aprendizado por construção e pensamento sistêmico.
- O conteúdo deve evitar exagero, autopromoção artificial e linguagem publicitária.

---

## Integridade de conteúdo

O site nunca deve:

- inventar clientes
- inventar métricas
- inventar empresas
- inventar conquistas
- inventar histórico profissional
- inventar hardware, topologias ou detalhes técnicos não fornecidos
- inventar credenciais, certificados ou autoridade não confirmada

Todo conteúdo deve permanecer coerente com experimentos reais, laboratório pessoal, documentação e aprendizado em andamento.

---

## Regras de geração de páginas

- Ao receber instrução para criar uma nova página, o sistema deve criar um novo arquivo HTML específico.
- O sistema não deve sobrescrever `index.html`, `projetos.html` ou `notas.html` sem pedido explícito.
- Se a instrução disser para criar uma página específica como `homelab.html`, o arquivo deve ser exatamente esse.
- O sistema deve preservar as páginas existentes quando o objetivo for adicionar uma nova.
- O sistema deve manter coerência visual entre páginas.

---

## Navegação

O header deve seguir um padrão compartilhado sempre que possível.

Navegação principal esperada:

- Início
- Projetos
- Notas

Páginas temáticas podem adicionar destaque local, mas não devem quebrar a consistência visual da navegação principal.

---

## Estilo visual global

O site deve manter:

- tema dark elegante
- tipografia forte
- visual técnico refinado
- espaçamento generoso
- bordas suaves
- cards arredondados quando necessário
- contraste alto para leitura
- coerência entre páginas

Evitar:

- visual excessivamente gamer
- excesso de badges
- poluição visual
- efeitos chamativos sem função
- estética genérica de template comercial

---

## Tailwind e estrutura técnica

- Preferir TailwindCSS via CDN nas páginas estáticas.
- Manter HTML claro e organizado.
- Usar CSS complementar apenas quando necessário.
- Evitar JavaScript desnecessário.
- Preservar compatibilidade com o estilo já existente no site.

---

## Papel das páginas

Nem toda página deve funcionar da mesma forma.

- A homepage é uma página de identidade e manifesto.
- A página de projetos é uma página índice.
- Páginas temáticas devem aprofundar áreas específicas com mais concretude.

As páginas devem respeitar seu papel editorial.

