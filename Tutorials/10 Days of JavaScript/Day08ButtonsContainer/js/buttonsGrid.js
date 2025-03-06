const btns = document.getElementById("btns");
const btn5 = document.getElementById("btn5");

btn5.addEventListener("click", () => {
  let arr = Array.from(btns.children);

  // Create 2D array to store button values
  let grid = [];
  for (let i = 0; i < 3; i++) {
    grid.push(arr.splice(0, 3));
  }

  // Rotate the buttons clockwise
  [
    grid[0][0].innerHTML,
    grid[0][1].innerHTML,
    grid[0][2].innerHTML,
    grid[1][0].innerHTML,
    grid[1][2].innerHTML,
    grid[2][0].innerHTML,
    grid[2][1].innerHTML,
    grid[2][2].innerHTML,
  ] = [
    grid[1][0].innerHTML,
    grid[0][0].innerHTML,
    grid[0][1].innerHTML,
    grid[2][0].innerHTML,
    grid[0][2].innerHTML,
    grid[2][1].innerHTML,
    grid[2][2].innerHTML,
    grid[1][2].innerHTML,
  ];
});
