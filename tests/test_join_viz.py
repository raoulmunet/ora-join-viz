from ora_join_viz import parse_joins

def test_two_joins():
    sql="""SELECT * FROM customers c
    JOIN orders o ON c.customer_id=o.customer_id
    LEFT JOIN order_items i ON o.order_id=i.order_id"""
    e=parse_joins(sql)
    assert len(e)==2
    assert e[0].right=="ORDERS"
    assert e[1].join_type=="LEFT"
