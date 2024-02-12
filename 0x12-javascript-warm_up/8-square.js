#!/usr/bin/node
if (typeof Number(process.argv[2]) === 'number' && !isNaN(Number(process.argv[2]))) {
  const num = Number(process.argv[2]);
  let square = '';
  for (let i = 0; i < num; i++) {
    for (let j = 0; j < num; j++) {
      square += 'X';
    }
    if (i < num - 1) square += '\n';
  }
  console.log(square);
} else {
  console.log('Missing size');
}
