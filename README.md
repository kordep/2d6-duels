# 2d6 Duels

App de mesa para jogar **2d6 Duels**, jogo de duelo com 2d6 criado por **Tito B.A.** — *"A deadly sport for a more civilized age"*.

🎮 **Jogar agora:** https://USUARIO.github.io/2d6-duels/ *(link atualizado após publicação)*

## O que é

Um app de arquivo único (HTML), que abre direto no navegador do celular ou PC, funciona **offline** e salva seus duelistas no aparelho. Feito para jogar com um amigo passando o mesmo aparelho.

## Funcionalidades

- **🪶 Forja de Duelistas** — gere combatentes rolando tudo pelos dados (criação, penas no chapéu, honra, estilo de luta), evolua e gerencie seu elenco.
- **⚔ Duelo** — resolve iniciativa, ataques, feridas, aparas/contra-ataques, mutilações e sangramento conforme as regras.
- **Dois modos de rolagem:**
  - 🎲 **Automático** — o app rola os dados por você.
  - ✍ **Dados físicos** — vocês rolam os dados de verdade e digitam os resultados; o app julga o que acontece.
- **📜 Regras** — resumo das mecânicas para consulta rápida.

Arte (xilogravuras e textura de pergaminho) extraída do jogo original.

## Como usar

Basta abrir o [`index.html`](index.html) no navegador. Para jogar no celular, abra o link do GitHub Pages e use "Adicionar à Tela de Início".

## Desenvolvimento

O app é gerado a partir de `index.src.html` (template) + `build.py`, que embute as imagens de `assets/` como base64 no `index.html` final:

```bash
python3 build.py
```

---

Jogo original por Tito B.A. · App de mesa.
