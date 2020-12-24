CREATE TABLE IF NOT EXISTS item(
    id INTEGER,
    item_name VARCHAR NOT NULL,
    price FLOAT NOT NULL,
    CONSTRAINT pk1_id PRIMARY KEY (id)
);

DROP INDEX IF EXISTS item_name_unique_idx;
CREATE UNIQUE INDEX item_name_unique_idx ON item(LOWER(TRIM(item_name)));
