SELECT 
    CONCAT(s.seller_id, '-', oi.product_id) AS seller_product_id, -- <--- NUEVA CLAVE ÚNICA
    s.seller_id,
    LOWER(TRIM(s.seller_city)) AS seller_city_clean,
    LOWER(TRIM(s.seller_state)) AS seller_state_clean,
    oi.product_id,
    p.product_category_name,
    p.product_weight_g,
    COUNT(oi.order_item_id) AS unidades_vendidas,
    COUNT(DISTINCT oi.order_id) AS total_pedidos, 
    SUM(oi.price) AS ingreso_total_producto,
    (SUM(oi.price) / COUNT(DISTINCT oi.order_id)) AS ticket_medio
FROM sellers s
INNER JOIN order_items oi ON s.seller_id = oi.seller_id
INNER JOIN products p ON oi.product_id = p.product_id
GROUP BY 
    s.seller_id,
    LOWER(TRIM(s.seller_city)),
    LOWER(TRIM(s.seller_state)),
    oi.product_id,
    p.product_category_name,
    p.product_weight_g;
