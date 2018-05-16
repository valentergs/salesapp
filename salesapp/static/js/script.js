currentYear = 2018

var rodrigo = {
  nome: 'Rodrigo Valente',
  idade: 41,
  estCivil: 'casado',
  nasc: 1976,
  nacionalidade: 'brasileira',
};

var vanessa = {
  nome: 'Vanessa Valente',
  idade: 37,
  nasc: 1981,
  estCivil: 'casada',
  nacionalidade: 'brasileira',
};

var gustavo = {
  nasc: '28-06-2012',
  nome: 'Gustavo Valente',
  idade: 5,
  estCivil: 'solteiro',
  nacionalidade: 'brasileira',
};

gustavo.estCivil = 'casado'

var pessoa = gustavo;
console.log(gustavo.idade);

var eduardo = new Object();
eduardo.age = 3;
eduardo.name = 'Eduardo Valente';
eduardo.gender = 'Male';
eduardo.yearOfBirth = 2015;

console.log(currentYear - eduardo.yearOfBirth);
