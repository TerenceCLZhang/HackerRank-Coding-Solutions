const button = document.getElementById("btn");

button.addEventListener("click", function () {
  let currentNumber = Number(button.textContent);
  currentNumber++;
  button.textContent = currentNumber;
});
