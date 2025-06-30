const definitionsButton = document.getElementById("definitions-button");
const definitionsUl = document.getElementById("definitions-box");

let clicked = true;

definitionsButton.addEventListener("click", () => {
  if (clicked) {
    definitionsUl.style.display = "flex";
    definitionsButton.innerHTML = "hide definitions";
    clicked = false;
  } else {
    definitionsUl.style.display = "none";
    definitionsButton.innerHTML = "show definitions";
    clicked = true;
  }

  definitionsButton.classList.toggle("hide-state");
});
