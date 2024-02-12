#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const arr = [];
  for (let i = 2; i < process.argv.length; i++) {
    arr.push(Number(process.argv[i]));
  }
  const initMax = Math.max(...arr);
  const newArr = arr.filter(item => item !== initMax);
  console.log(Math.max(...newArr));
}
