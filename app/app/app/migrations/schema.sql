-- USERS TABLE
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    phone_number VARCHAR(20) UNIQUE NOT NULL,
    name TEXT,
    first_seen TIMESTAMP DEFAULT NOW()
);

-- LAND PRICES TABLE
CREATE TABLE IF NOT EXISTS land_prices (
    id SERIAL PRIMARY KEY,
    location TEXT NOT NULL,
    price_usd NUMERIC,
    land_size TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
