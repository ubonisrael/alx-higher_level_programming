#!/usr/bin/node
if (!isNaN(Number(process.argv[2])) && typeof Number(process.argv[2]) === 'number') console.log(`My number: ${Number(process.argv[2])}`);
else console.log('Not a number');
