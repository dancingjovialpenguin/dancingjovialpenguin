const cat = document.getElementById("cat");

let catStopped = false;

cat.addEventListener("click", () => {
  if (catStopped) {
    cat.style.animationPlayState = "running";
    catStopped = false;
  } else {
    cat.style.animationPlayState = "paused";
    catStopped = true;
  }
});
