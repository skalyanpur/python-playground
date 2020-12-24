CREATE TABLE IF NOT EXISTS api_user(
id BIGSERIAL,
username VARCHAR NOT NULL,
password VARCHAR NOT NULL,
active BOOLEAN DEFAULT TRUE,
email_address varchar NOT NULL ,
CONSTRAINT api_user_id_pk PRIMARY KEY (id)
);

DROP INDEX IF EXISTS username_uidx_1;
CREATE UNIQUE INDEX username_uidx_1 ON api_user(LOWER(TRIM(username)));

DROP INDEX IF EXISTS email_address_uidx_1;
CREATE UNIQUE INDEX email_address_uidx_1 ON api_user(LOWER(TRIM(email_address)));
