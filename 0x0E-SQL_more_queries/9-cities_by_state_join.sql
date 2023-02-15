--Lists all cities in the database hbtn_0d_usa.
--Record are sorted in order of ascending cities.id.
SELECT c.'id', c.'name', s.'name'
  FROM 'CITIES' AS c
	INNER JOIN 'states' AS s
	ON c.'state_id' = s.'id'
ORDER BY c.'id';
