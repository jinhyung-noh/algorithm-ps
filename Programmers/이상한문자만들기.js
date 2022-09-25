const solution = (string) => {
  const words = string.split(" ");
  const weirdWords = words.map(makeWeirdWord);
  return weirdWords.join(" ");
};

const makeWeirdWord = (word) => {
  const weirdWordArr = [];
  for (let idx = 0; idx < word.length; idx++) {
    const char = word[idx];
    if (idx % 2 === 0) {
      weirdWordArr.push(char.toUpperCase());
      continue;
    }
    weirdWordArr.push(char.toLowerCase());
  }
  return weirdWordArr.join("");
};
