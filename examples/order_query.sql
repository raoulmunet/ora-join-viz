SELECT
    c.customer_id,
    o.order_id,
    i.product_id
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id
LEFT JOIN order_items i
    ON o.order_id = i.order_id;
