DROP TABLE IF EXISTS public.votantes;
CREATE TABLE votantes(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    sexo VARCHAR(10) NOT NULL
);
DROP TABLE IF EXISTS public.candidatos;
CREATE TABLE candidatos(
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL
);
DROP TABLE IF EXISTS public.voto;
CREATE TABLE voto(
    id SERIAL PRIMARY KEY,
    candidato INT REFERENCES candidatos(id),
    votante INT REFERENCES votantes(id),
    fecha DATE DEFAULT CURRENT_DATE, 
    puesto VARCHAR(50)
);

