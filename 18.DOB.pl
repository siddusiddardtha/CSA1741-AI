person(john_doe, date(1990, 5, 15)).
person(jane_smith, date(1985, 7, 20)).
person(alice_jones, date(1992, 12, 3)).
person(bob_brown, date(1978, 3, 22)).
dob(Name, date(Year, Month, Day)) :-
    person(Name, date(Year, Month, Day)).
