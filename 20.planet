planet(mercury, 57.9, 4879).
planet(venus, 108.2, 12104).
planet(earth, 149.6, 12756).
planet(mars, 227.9, 6792).
planet(jupiter, 778.5, 142984).
planet(saturn, 1433.5, 120536).
planet(uranus, 2872.5, 51118).
planet(neptune, 4495.1, 49528).
distance_from_sun(Planet, Distance) :-
    planet(Planet, Distance, _).
diameter(Planet, Diameter) :-
    planet(Planet, _, Diameter).
planets_within_distance(MaxDistance, Planets) :-
    findall(Planet, (planet(Planet, Distance, _), Distance =< MaxDistance), Planets).
planets_larger_than(Diameter, Planets) :-
    findall(Planet, (planet(Planet, _, D), D > Diameter), Planets).
