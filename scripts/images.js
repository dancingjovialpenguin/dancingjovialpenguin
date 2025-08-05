const sidebarDiv = document.getElementById("sidebar");
const aboutSection = document.getElementById("about");
const imagesUl = document.getElementById("images");

function placeImages() {
  let screenWidth = window.innerWidth;

  if (screenWidth <= 768) {
    aboutSection.insertBefore(imagesUl, aboutSection.children[2]);
  } else {
    sidebarDiv.appendChild(imagesUl);
  }
}

placeImages();

window.addEventListener("resize", placeImages);
