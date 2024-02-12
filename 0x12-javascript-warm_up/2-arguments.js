#!/usr/bin/node
const argsNo = process.argv.length

if (argsNo === 2) console.log("No argument");
if (argsNo === 3) console.log("Argument found");
if (argsNo > 3) console.log("Arguments found");
