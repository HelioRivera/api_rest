-- Script de llenado de datos para myapp_product
-- Elimina datos existentes si es necesario
TRUNCATE TABLE public.myapp_product RESTART IDENTITY CASCADE;

-- Inserta datos de prueba
INSERT INTO public.myapp_product (name, description, price, created_at) VALUES
('Laptop Pro', 'Potente laptop con 16GB RAM y SSD 512GB', 1299.99, NOW() - INTERVAL '10 days'),
('Smartphone X', 'Teléfono inteligente con cámara de 48MP', 799.50, NOW() - INTERVAL '7 days'),
('Tablet Lite', 'Tablet económica ideal para estudiantes', 299.00, NOW() - INTERVAL '5 days'),
('Auriculares BT', 'Auriculares inalámbricos con cancelación de ruido', 199.95, NOW() - INTERVAL '3 days'),
('Teclado Mecánico', 'Teclado gaming con switches azules', 89.99, NOW() - INTERVAL '1 day'),
('Monitor 4K', 'Monitor de 27 pulgadas con resolución 4K', 499.00, NOW()),
('Mouse Inalámbrico', 'Mouse ergonómico con 6 botones programables', 49.99, NOW()),
('Disco Duro Externo', '1TB de almacenamiento portátil USB 3.0', 69.90, NOW()),
('Router Wi-Fi 6', 'Router de última generación con Wi-Fi 6', 149.00, NOW()),
('Altavoz Bluetooth', 'Altavoz portátil con 20h de autonomía', 119.50, NOW());

-- Verifica los datos insertados
SELECT * FROM public.myapp_product ORDER BY created_at DESC;