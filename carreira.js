function encontrarCaracter(string) {
  const caracter = {};
  const stringSplited = string.toLowerCase().replace(" ", "").split("");

  for (let i = 0; i < stringSplited.length; i += 1) {
    if (caracter[stringSplited[i]]) {
      caracter[stringSplited[i]] += 1;
    } else {
      caracter[stringSplited[i]] = 1;
    }
  }

  const object = Object.entries(caracter).sort((a, b) => b[1] - a[1])[0];
  return object[0];
}

console.log(encontrarCaracter("bananaAAACCCCCcccc"));
