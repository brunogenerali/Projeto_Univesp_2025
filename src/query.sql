-- Criar tabela com a porcentagem de candidatos por gênero em cada partido de 2024
DROP TABLE IF EXISTS tb_porcentagem_genero_partido;
CREATE TABLE IF NOT EXISTS tb_porcentagem_genero_partido AS 
SELECT
    SG_PARTIDO, 
    ROUND(
        (CAST(COUNT(CASE WHEN DS_GENERO = 'FEMININO' THEN 1 END) AS REAL) * 100) / COUNT(*)
    , 2) AS 'PORCENTAGEM_FEMININO',
    ROUND(
        (CAST(COUNT(CASE WHEN DS_GENERO = 'MASCULINO' THEN 1 END) AS REAL) * 100) / COUNT(*)
    , 2) AS 'PORCENTAGEM_MASCULINO'
FROM
    tb_candidatos_2024
WHERE
    DS_GENERO != 'NÃO DIVULGÁVEL'
GROUP BY
    SG_PARTIDO
ORDER BY
    PORCENTAGEM_FEMININO;
    
-- Verificar os dados selecionados
SELECT
    *
FROM
    tb_porcentagem_genero_partido
limit
    10;