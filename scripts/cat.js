const cat = document.getElementById("cat");

let catStopped = false;

cat.addEventListener("click", () => {
  if (catStopped) {
    cat.style.animationPlayState = "running";
    cat.style.opacity = 1;
    catStopped = false;
  } else {
    cat.style.animationPlayState = "paused";
    cat.style.opacity = 0.5;
    catStopped = true;
  }
});
