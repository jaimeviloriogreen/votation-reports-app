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
    ('Alberto', 'Rodríguez', 'Masculino'),
     ('Sara', 'Mariñez', 'Femenino'),
    ('Carlos', 'Almanzar', 'Masculino'),
    ('Javier', 'De La cruz', 'Masculino'),
    ('Marlom', 'De Léon', 'Masculino'),
    ('Ryan', 'Colunna', 'Masculino'),
    ('Dere', 'De La Rosa', 'Masculino'),
    ('Melissa', 'Hughes', 'Femenino'),
    ('Sheila', 'Espiritusanto', 'Femenino'),
    ('Elizabeth', 'Carpio', 'Femenino'),
    ('Carliana', 'Sierra', 'Femenino'),
    ('Jairo', 'Cruz', 'Masculino'),
    ('Xavier', 'Melendez', 'Masculino'),
    ('Oscar', 'Quiñonez', 'Masculino'),
    ('Raisa', 'Casanova', 'Femenino'),
    ('Esteban', 'De Jesús', 'Masculino'),
    ('Mario', 'Alfonseca', 'Casculino'),
    ('Salvador', 'Carrasco', 'Masculino'),
    ('Michael', 'Smith', 'Masculino'),
    ('Máximo', 'Duarte', 'Masculino'),
    ('Peterson', 'White', 'Masculino'),
    ('Cristal', 'La Luz', 'Femenino'),
    ('Esperanza', 'Mieses', 'Femenino');

--!Queries para el Reporte
    -- Total de votos emitidos
    SELECT COUNT(*) FROM voto;

    -- Total de voto por candidato
    SELECT COUNT(*) FROM voto WHERE candidato = 1;


