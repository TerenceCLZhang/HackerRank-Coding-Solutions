"use strict";

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;

process.stdin.on("data", (inputStdin) => {
  inputString += inputStdin;
});

process.stdin.on("end", (_) => {
  inputString = inputString
    .trim()
    .split("\n")
    .map((string) => {
      return string.trim();
    });

  main();
});

function readLine() {
  return inputString[currentLine++];
}

function getLetter(s) {
  let firstCharacter = s[0].toLowerCase();

  switch (true) {
    case "aeiou".includes(firstCharacter):
      return "A";
    case "bcdfg".includes(firstCharacter):
      return "B";
    case "hjklm".includes(firstCharacter):
      return "C";
    default:
      return "D";
  }
}

function main() {
  const s = readLine();

  console.log(getLetter(s));
}
