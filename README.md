# ora-join-viz

[![tests](https://github.com/raoulmunet/ora-join-viz/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-join-viz/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Turn common Oracle SQL joins into a compact dependency graph.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Supported for common ANSI JOIN syntax |
> | Oracle Database 23ai | ✅ Supported for common ANSI JOIN syntax |
> | Oracle AI Database 26ai | ✅ Supported for common ANSI JOIN syntax |
>
> Legacy Oracle outer-join syntax using `(+)` is not yet fully visualized and is explicitly outside the current parser scope.

## Features

- discovers tables and aliases;
- detects INNER / LEFT / RIGHT / FULL / CROSS joins;
- extracts the ON condition as an edge label;
- outputs text, JSON or Mermaid;
- requires no database connection.

## Usage

```bash
ora-join-viz examples/order_query.sql
ora-join-viz examples/order_query.sql --format mermaid
```

Example:

```text
CUSTOMERS c --[INNER: c.customer_id = o.customer_id]--> ORDERS o
ORDERS o --[LEFT: o.order_id = i.order_id]--> ORDER_ITEMS i
```

## Scope

The parser targets readable ANSI JOIN SQL. Deeply nested inline views, dynamically generated SQL and legacy `(+)` semantics are not guessed.

## Visual demo

A static visual preview is included in [`docs/index.html`](docs/index.html).

To publish it with GitHub Pages: **Settings → Pages → Deploy from a branch → `main` → `/docs`**. The repository is already prepared with `docs/.nojekyll`.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
