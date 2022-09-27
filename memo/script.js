const c1Content = document.getElementById("content");
const c2Date = document.getElementById("date");
const c3Time = document.getElementById("time");
const addBtn1 = document.getElementById("addedBtn");
const deletBtn2 = document.getElementById("deletedBtn");
const list = document.getElementById("list");

const listContent = [];
function render() {
  let htmlList = "";

  listContent.forEach(function (item) {
    htmlList =
      htmlList +
      `
        <div class="item">
            <div>
                <p>內容：${item.content}</p>
                <p>時間：${item.date} ${item.time}</p>
                <hr/>
            </div>
        </div>
        `;
  });
  list.innerHTML = htmlList;
}

addBtn1.addEventListener("click", function () {
  listContent.unshift({
    content: c1Content.value,
    date: c2Date.value,
    time: c3Time.value,
  });

  render();
});

deletBtn2.addEventListener("click", function () {
  listContent.shift();

  render();
});
