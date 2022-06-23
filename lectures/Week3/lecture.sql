-- Owner table queries
SELECT * FROM owner;
INSERT INTO owner (firstName, lastName, email) VALUES ("Jane", "Doe", "jane@doe.com"), ('Bob', 'Ross', 'bob@ross.com'), ('Melissa', 'Longenberger', 'mlongenberger@codingdojo.com');
INSERT INTO owner (firstName, lastName, email) VALUES ('Hayden', 'Longaberger', 'bubby@gmail.com');
UPDATE owner SET lastName='Longenberger' WHERE id=4;
UPDATE owner SET lastName='Longenberger' WHERE id=8;
SELECT * FROM owner left join pet on owner.id = pet.owner_id left join species on pet.species_id = species.id WHERE owner.id = 3;

-- species table queries
SELECT * FROM species;
INSERT INTO species (species) VALUES ('Dog'), ('Cat'), ('Fish'), ('Bird'), ('Snake'), ('Bunny'), ('Sugar Bear');

-- Pet table queries
SELECT * FROM pet;
INSERT INTO pet (name, breed, gender, age, color, species_id, owner_id) VALUES ('Copper Tone', 'Beagle', 'Male', 1, 'Black,Brown,White',1, 3), ('Roxy Mae', 'Red Nose Pit Sheperd Mix', 'Female', 2, 'White', 1, 3), ('Whiskey Lou', 'Rhodesian ridgeback and hound', 'Female', 6, 'Light Brown', 1,1) ;
UPDATE pet SET owner_id=4 WHERE id=2;
UPDATE pet SET owner_id=3 WHERE id=2;
SELECT * FROM pet left join species on pet.species_id = species.id left join owner on pet.owner_id = owner.id where pet.id=1;