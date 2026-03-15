# Site Guidelines

Estas diretrizes definem o comportamento editorial, estrutural e operacional do site como um todo.

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

---

## Modos de alteração

Toda solicitação deve ser interpretada em um modo de alteração específico.

### `create_page`
Usar quando o objetivo for criar uma nova página.

Pode:
- criar um novo arquivo HTML específico
- adicionar links coerentes para a nova página
- reutilizar estilos e navegação do site

Não pode:
- sobrescrever páginas centrais sem pedido explícito
- reescrever homepage ou páginas índice só porque uma nova página foi criada

---

### `visual_refine_only`
Usar quando o objetivo for harmonizar visual, header, fundo, spacing, superfícies, bordas, componentes e consistência estética.

Pode:
- alterar classes
- alterar layout visual
- alterar header
- alterar fundo
- alterar sombras, bordas e cores
- melhorar consistência entre páginas

Não pode:
- reescrever textos principais
- mudar o papel editorial da página
- mover CTAs de uma página para outra
- adicionar novas seções sem pedido explícito
- transformar homepage em index page
- transformar página temática em manifesto

---

### `navigation_only`
Usar quando o objetivo for ajustar links, menus, botões e caminhos entre páginas.

Pode:
- alterar href
- alterar itens do menu
- adicionar links de navegação
- destacar item ativo
- ajustar navegação entre páginas já existentes

Não pode:
- reescrever blocos textuais
- alterar estrutura editorial da página além do necessário para navegação
- mover conteúdo temático para páginas erradas

---

### `content_edit`
Usar quando o objetivo for alterar textos, copy, blocos editoriais ou seções textuais.

Pode:
- reescrever texto
- reorganizar blocos textuais
- refinar tom editorial

Não pode:
- mudar o papel da página sem pedido explícito
- inventar fatos
- alterar páginas fora do escopo do pedido

---

### `full_page_rewrite`
Usar apenas quando o pedido disser claramente para recriar, refazer ou reescrever uma página inteira.

Pode:
- reestruturar toda a página
- reescrever conteúdo
- alterar layout e componentes livremente

Não pode:
- atingir outras páginas não solicitadas
- ignorar identidade, guidelines e structure do site

---

## Regra de escopo estrito

Quando o objetivo mencionar explicitamente:

- um arquivo específico
- páginas que não devem ser alteradas
- “sem alterar X”
- “apenas visual”
- “somente navegação”
- “ajuste cirúrgico”

o sistema deve tratar isso como restrição obrigatória e não como sugestão.

---

## Regra de preservação editorial

Mesmo quando houver refinamento visual, o sistema deve preservar:

- a função editorial da página
- o papel estrutural definido em `site_structure.md`
- o tipo de página definido em `page_types/`
- o briefing definido em `page_briefs/`, quando existir

O site deve crescer como sistema coerente, não como coleção aleatória de páginas.
