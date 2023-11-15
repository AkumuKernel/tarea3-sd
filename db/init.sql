CREATE TABLE registros (
    id SERIAL NOT NULL,
    palabra varchar NOT NULL,
    numero int NOT NULL,
    archivo int NOT NULL,
    PRIMARY KEY (id)
);