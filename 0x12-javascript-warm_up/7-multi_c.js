#!/usr/bin/node
if (!isNaN(Number(process.argv[2])) && typeof Number(process.argv[2]) === 'number') {
  for (let i = 0; i < Number(process.argv[2]); i++) console.log('C is fun');
} else {
  console.log('Missing number of occurrences');
}
