CREATE TABLE IF NOT EXISTS orders (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL,
    status VARCHAR(12) NOT NULL CHECK (status IN ('come', 'not come', 'not know')),
    how_much INTEGER NOT NULL
);