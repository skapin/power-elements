INSERT INTO "customer" (uniqid, name, email, password) VALUES
('e79aa54d-2494-4aaf-a26e-e9b60315edd2', 'aiothe', 'aiothe@aio.eu', '$pbkdf2-sha256$1000000$EUIopXTOmfo.13qv1ZqTUg$a48aEYbRyK4n409Dl2q/LYncyYSqAKTQY75.Xptzzbc');


INSERT INTO numii (uniqid, name,created_at, updated, state, customer_id) VALUES ('d6d0eeb8-8389-11e8-b276-2f6e8437d221','numii_xs_3',NOW(), NOW(), 'SERVICE', 'e79aa54d-2494-4aaf-a26e-e9b60315edd2');
