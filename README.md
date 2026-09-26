# ora-join-viz

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

## License

MIT.
