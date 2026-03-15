# Site Structure

Este arquivo descreve a estrutura editorial e funcional do site.

Ele existe para orientar agentes e futuras automações sem depender de mudanças no código do pipeline.

A estrutura do site deve ser entendida a partir deste arquivo em conjunto com:

- `site_identity.md`
- `site_guidelines.md`
- `page_types/`
- `page_briefs/`

---

## Core Pages

Estas são páginas centrais do site.

### `index.html`
- role: homepage manifesto
- status: active
- purpose: apresentar a filosofia, identidade técnica e tom editorial do site
- overwrite_policy: do not overwrite unless explicitly requested

### `projetos.html`
- role: index page
- status: active
- purpose: servir como mapa técnico principal das áreas e páginas temáticas do site
- overwrite_policy: do not overwrite unless explicitly requested

### `notas.html`
- role: notes page
- status: placeholder
- purpose: reunir notas públicas, aprendizados, writeups curtos e documentação editorial/técnica
- overwrite_policy: do not overwrite unless explicitly requested

---

## Section Pages

Estas são páginas temáticas que aprofundam áreas específicas.

### `homelab.html`
- role: section page
- status: planned
- brief: `page_briefs/homelab.md`
- purpose: aprofundar a área de homelab com mais concretude técnica e visual

### `minecraft.html`
- role: section page
- status: planned
- purpose: aprofundar a área de servidores, plugins, operação e experimentação em Minecraft

### `ai-agents.html`
- role: section page
- status: planned
- purpose: aprofundar a área de agentes, pipelines, geração, validação e previews

### `automacao.html`
- role: section page
- status: planned
- purpose: reunir automações, integrações, scripts e fluxos operacionais

### `rede-vpn.html`
- role: section page
- status: planned
- purpose: aprofundar redes, WireGuard, acesso remoto, topologia e segurança operacional

### `software.html`
- role: section page
- status: planned
- purpose: reunir ferramentas, interfaces, sistemas e aplicações experimentais

### `apps-mobile.html`
- role: section page
- status: planned
- purpose: aprofundar desenvolvimento e testes de apps Android/iOS

---

## Page Roles

Cada página do site tem um papel editorial diferente.

### Homepage
- página de identidade
- manifesto técnico
- curta
- forte
- filosófica
- não deve funcionar como índice de projetos

### Index Page
- página organizadora
- mais concreta
- mais estrutural
- serve como mapa de navegação para áreas técnicas

### Section Page
- página temática específica
- aprofunda um domínio
- pode ter mais presença visual
- deve permanecer factual e coerente com o tema

---

## Navigation

A navegação principal do site deve priorizar:

- Início
- Projetos
- Notas

Páginas temáticas devem ser acessadas principalmente a partir de `projetos.html` e de links internos coerentes.

---

## Overwrite Rules

Regras de segurança estrutural:

- `index.html` não deve ser sobrescrito quando o objetivo for criar uma nova página temática
- `projetos.html` não deve ser sobrescrito quando o objetivo for criar uma nova página temática
- `notas.html` não deve ser sobrescrito quando o objetivo for criar uma nova página temática
- novas páginas devem ser criadas como novos arquivos HTML específicos
- sobrescrita de páginas centrais só pode acontecer com pedido explícito

---

## Existing Structure vs Planned Structure

O pipeline deve distinguir:

### Estrutura existente
Páginas já presentes no diretório `frontend/`

### Estrutura planejada
Páginas listadas aqui com status `planned`

Se uma página estiver marcada como `planned`, ela pode ser criada futuramente sem alterar páginas centrais.

---

## Editorial Consistency

Toda nova página deve ser compatível com:

- identidade do site
- guidelines globais
- papel editorial da página
- navegação principal
- linguagem visual já existente

O site deve crescer como sistema coerente, não como coleção aleatória de páginas.

