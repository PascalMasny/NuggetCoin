# NuggetCoin

> Nugget Coin is a theoretical representation of the blockchain 🔗 and crypto mining ⛏️.

Ein Lern-Sandkasten für die Grundlagen von **Blockchain** und **Proof-of-Work-Mining** in Python. Kein echter Coin, sondern der Versuch, selbst nachzubauen, wie Blöcke, Hashes und Mining eigentlich zusammenhängen.

## Was drin ist
- **`blockchain.py`**: saubere `Block`/`Blockchain`-Klassen mit Proof of Work. `mine(difficulty)` erhöht die Nonce so lange, bis der SHA-256-Hash mit N Nullen beginnt.
- **`nugget.py`**: baut eine kleine NuggetCoin-Kette aus 3 Blöcken mit je 2 Transaktionen und schreibt sie nach `Blockchain/*.block` (jeweils Vorgänger- und aktueller Hash).
- **`mining_the_nugget.py`**: ein Pseudo-Miner mit Lade-Animation, der eine passende Nonce für einen Ziel-Präfix aus Nullen brute-forced.
- **`token.sol`**: erster Gehversuch mit einem ERC20-Token in Solidity.

## Nutzung
```bash
python3 nugget.py               # Blockchain aufbauen
python3 mining_the_nugget.py    # einen Block "minen"
```

## Konzept
Jeder Block hängt über den Hash seines Vorgängers an der Kette. Proof of Work heißt: eine Nonce finden, deren Hash eine bestimmte Anzahl führender Nullen hat. Das kostet Rechenzeit und macht nachträgliche Manipulation teuer.
Referenzen: [Blockchain-Tutorial](https://www.youtube.com/watch?v=pYasYyjByKI) · [Mining-Tutorial](https://www.youtube.com/watch?v=ZhnJ1bkIWWk)

## Stack
`Python 3` · `hashlib` (SHA-256) · `Solidity` (Token-Stub)

<details>
<summary>🇬🇧 English</summary>

A learning sandbox for the basics of blockchain and proof-of-work mining in Python. Not a real coin, but a hands-on rebuild of how blocks, hashes and mining fit together: a `Block`/`Blockchain` with PoW (`blockchain.py`), a 3-block toy chain with transactions (`nugget.py`), a brute-force miner with a loading spinner (`mining_the_nugget.py`), and a first ERC20 token stub in Solidity (`token.sol`).
</details>

> Blockchain zum Selberbauen, 2025.
