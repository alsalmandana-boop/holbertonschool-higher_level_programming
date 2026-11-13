#!/usr/bin/node
const args = process.argv.slice(2);

if (args.count === 0) {
  console.log('No argument');
} else if (args.count === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
