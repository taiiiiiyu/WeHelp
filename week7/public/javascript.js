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

function search() {
  let username = document.querySelector(".search").value;
  fetch("http://127.0.0.1:3000/api/member?=" + username)
    .then((response) => {
      return response.json();
    })
    .then((response) => {
      let result = document.querySelector(".searchResult");
      if (response.data) {
        let name = response.data.name;
        let username = response.data.username;
        result.innerHTML = name + `(${username})`;
      } else {
        result.innerHTML = "查無結果";
      }
    });
}

function update() {
  let name = document.querySelector(".update").value;
  let updateName = {
    name: name,
  };
  fetch("http://127.0.0.1:3000/api/member", {
    method: "PATCH",
    body: JSON.stringify(updateName),
    headers: { "Content-type": "application/json" },
  })
    .then((response) => response.json())
    .then((json) => {
      let update = document.querySelector(".updateResult");
      let msgName = document.querySelector("#msgTitle");
      if (json.ok) {
        msgName.innerHTML = `${name}，歡迎回來`;
        update.innerHTML = "更新成功";
      } else {
        update.innerHTML = "更新失敗";
      }
    });
}
