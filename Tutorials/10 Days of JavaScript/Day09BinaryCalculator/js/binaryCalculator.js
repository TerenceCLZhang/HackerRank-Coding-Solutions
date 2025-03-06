const res = document.getElementById("res");
const btns = document.getElementById("btns");

let opAdded = false;

const calculate = () => {
  equation = res.innerHTML;
  const binaryExpression = equation.replace(/[01]+/g, (match) => `0b${match}`);
  res.innerHTML = eval(binaryExpression).toString(2);
};

for (let btn of btns.children) {
  btn.addEventListener("click", () => {
    switch (btn.id) {
      case "btn0":
      case "btn1":
        res.innerHTML += btn.id.charAt(3);
        break;

      case "btnClr":
        res.innerHTML = "";
        opAdded = false;
        break;

      case "btnEql":
        if (opAdded && res.innerHTML != "") {
          calculate();
          opAdded = false;
        }
        break;

      case "btnSum":
      case "btnSub":
      case "btnMul":
      case "btnDiv":
        if (!opAdded && res.innerHTML != "") {
          switch (btn.id) {
            case "btnSum":
              res.innerHTML += "+";
              break;
            case "btnSub":
              res.innerHTML += "-";
              break;
            case "btnMul":
              res.innerHTML += "*";
              break;
            case "btnDiv":
              res.innerHTML += "/";
              break;
          }
          opAdded = true;
        }
        break;
    }
  });
}
