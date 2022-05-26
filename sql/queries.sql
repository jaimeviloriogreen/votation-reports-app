--! INSERT INTO TABLES

-- INSERT INTO TABLE votantes;
INSERT INTO
    votantes(nombre, apellido, sexo, cedula)
VALUES
    ('Jaime', 'Alcántara', 'Masculino', '02607653229'),
    ('Pablo', 'Rivera', 'Masculino', '05607853410'),
    ('Marina', 'Méndez', 'Femenino', '02500013211'),
    ('Julia', 'Santana', 'Femenino', '00134253610'),
    ('Zoraida', 'Nuñez', 'Femenino', '05834354656'),
    ('Pablo', 'Sarmiento', 'Masculino', '02623454950'),
    ('Raymundo', 'Muñoz', 'Masculino', '02600453252'),
    ('Minerva', 'Sosa', 'Femenino', '00100451152'),
    ('Alberto', 'Rodríguez', 'Masculino', '02537785150'),
    ('Sara', 'Mariñez', 'Femenino', '02327792259'),
    ('Carlos', 'Almanzar', 'Masculino', '0230072985'),
    ('Javier', 'De La cruz', 'Masculino', '00100027850'),
    ('Marlom', 'De Léon', 'Masculino', '02822027851'),
	('Ryan', 'Colunna',	'Masculino', '02811017855'),
	('Dere', 'De La Rosa', 'asculino', '02899011150'),
	('Melissa',	'Hughes', 'Femenino', '05600012518'),
	('Sheila', 'Espiritusanto', 'Femenino', '05399323024'),
	('Elizabeth', 'Carpio',	'Femenino',	'05309228192'),
	('Carliana', 'Sierra', 'Femenino', '05811230092'),
	('Jairo', 'Cruz', 'Masculino', '05800110091'),
	('Xavier', 'Melendez', 'Masculino', '05611323412'),
	('Oscar', 'Quiñonez', 'Masculino', '05893324407'),
	('Raisa', 'Casanova', 'Femenino', '05611323412'),
	('Esteban',	'De Jesús',	'Masculin', '00123323410'),
    ('Salvador', 'Carrasco', 'Masculino','02600023190'),
	('Michael',	'Smith', 'Masculino','02701233392'),
	('Máximo', 'Duarte', 'Masculino', '02611100300'),
	('Peterson', 'White', 'Masculino', '02701110313'),
	('Cristal',	'La Luz', 'Femenin','02701233392'),
    ('Esperanza', 'Mieses', 'Femenino', '02509111389'),
	('Jason', 'Soliman', 'Masculino', '02601238111'),
	('Alicia', 'Aquino', 'Femenino', '02613910828'),
	('Arianna',	'Castillo',	'Femenino', '00198763229'),
	('Dionisia', 'Concepción', 'Femenino', '00138263119'),
	('Omar', 'Nivar', 'Masculino', '02898632993'),
	('Mario', 'Alfonseca', 'Masculino',	'00100121110'),
	('Amanda', 'Jiménez', 'Femenino', '02698239882'),
	('Soila', 'Luna', 'Femenino', '02378233881'),
	('Raynel', 'Zapata', 'Masculino', '02603338190'),
	('Miriam', 'Rosario', 'Femenino', '02303218176'),
	('María', 'Pilar', 'Femenino', '00103218170'),
	('María', 'Dolores', 'Femenino', '05603212171'),
	('Laura', 'Silvestre', 'Femenino',	'05601313170'),
	('Antonio', 'Laureano',	'Masculino', '02801113172'),
	('Juan', 'López', 'Masculino', '02801221190'),
	('Alfredo', 'García', 'Masculino', '02601223110'),
	('Martín', 'Galvéz', 'Masculino', '02602773001'),
	('Adalberto', 'Sánchez', 'Masculino', '00102723419'),
	('Julio', 'Díaz', 'Masculino', '00112623210'),
	('Marcos', 'Jones',	'Masculino', '00100123219')
--!Queries para el Reporte
    --SELECT FROM TABLE voto
    SELECT 
        candidato, 
        votante, 
        fecha,
        puesto
    FROM 
        voto;

    -- SELECT FROM TABLE candidatos;
    SELECT id, nombre, apellido FROM candidatos;

    -- Total de votos emitidos
    SELECT COUNT(*) FROM voto;

    -- Total de voto por candidato
    SELECT COUNT(*) FROM voto WHERE candidato = 1;
    
    -- Total de votos por sexo
    SELECT 
        sexo, COUNT(sexo)
    FROM 
        voto
    INNER JOIN
        votantes
    ON
        voto.votante = votantes.id
    GROUP BY(sexo);
    
    -- Traer candidatos con sus candidaturas
    SELECT
        candidatos.id, nombre, apellido, posiciones
    FROM
        candidatos
    INNER JOIN 
        candidaturas 
    ON
        candidaturas.id = candidatos.aspiraciones;
-- Votos por candidatos
SELECT 
    nombre||' '||apellido, 
    COUNT(votante)
FROM
    voto
INNER JOIN
    candidatos
ON  
    candidatos.id = voto.candidato
GROUP BY(nombre||' '||apellido)
ORDER BY(COUNT(votante)) DESC;

-- INSERT INTO voto TABLE WHERE NOT EXISTS
INSERT INTO voto
    (candidato, votante)
SELECT 4, 37
WHERE NOT EXISTS(
    SELECT 
        votante
    FROM
        voto
    WHERE
        votante = 37
);

-- INSERT INTO votante TABLE WHERE NOT EXISTS
INSERT INTO votantes
    (nombre, apellido, sexo, cedula)
SELECT 'Jason','Soliman', 'Masculino', '02601238111'
WHERE NOT EXISTS(
    SELECT 
        cedula
    FROM
        votantes
    WHERE
        cedula = '02601238111'
);

    

