DROP TABLE IF EXISTS votantes;
CREATE TABLE votantes(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    sexo VARCHAR(10) NOT NULL,
    cedula VARCHAR(11) NOT NULL
);
DROP TABLE IF EXISTS candidatos;
CREATE TABLE candidatos(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL
);
DROP TABLE IF EXISTS voto;
CREATE TABLE voto(
    id SERIAL PRIMARY KEY,
    candidato INT REFERENCES candidatos(id),
    votante INT REFERENCES votantes(id),
    fecha DATE DEFAULT CURRENT_DATE, 
    puesto VARCHAR(50)
);

DROP TABLE IF EXISTS candidaturas;
CREATE TABLE candidaturas(
    id SERIAL PRIMARY KEY,
    posiciones VARCHAR(50) NOT NULL
);

