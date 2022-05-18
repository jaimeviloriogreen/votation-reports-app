--SELECT FROM TABLE voto
SELECT 
    candidato, 
    votante, 
    fecha,
    puesto
FROM 
    voto;

-- INSERT INTO voto TABLE WHERE NOT EXISTS
INSERT INTO voto
    (candidato, votante, puesto)
SELECT 1, 4, 'Alcalde'
WHERE NOT EXISTS(
    SELECT 
        votante
    FROM
        voto
    WHERE
        votante = 4
);

-- SELECT FROM TABLE candidatos;
SELECT id, nombre, apellido FROM candidatos;

-- INSERT INTO TABLE votantes;
INSERT INTO
    votantes(nombre, apellido, sexo)
VALUES
    ('Jaime', 'Alcántara', 'Masculino'),
    ('Pablo', 'Rivera', 'Masculino'),
    ('Marina', 'Méndez', 'Femenino'),
    ('Julia', 'Santana', 'Femenino'),
    ('Zoraida', 'Nuñez', 'Femenino'),
    ('Pablo', 'Sarmiento', 'Masculino'),
    ('Raymundo', 'Muñoz', 'Masculino'),
    ('Minerva', 'Sosa', 'Femenino'),
    ('Alberto', 'Rodríguez', 'Masculino');