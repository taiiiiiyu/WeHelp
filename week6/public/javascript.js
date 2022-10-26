const signin = document.querySelector(".signin");
const signup = document.querySelector(".signup");
const switch0 = document.querySelector(".switch-0");
const switch1 = document.querySelector(".switch-1");

switch0.addEventListener("click", function () {
  signup.classList.remove("hidden");
  signin.classList.add("hidden");
});

switch1.addEventListener("click", function () {
  signup.classList.add("hidden");
  signin.classList.remove("hidden");
});
