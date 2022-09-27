const btnCloseModal = document.querySelector(".close");
const container = document.querySelector(".container");
const modal = document.querySelector(".modal");
const h1 = document.getElementById("h1");

btnCloseModal.addEventListener("click", function () {
  container.classList.remove("hidden");
  h1.classList.remove("hidden");
  modal.classList.add("hidden");
});
