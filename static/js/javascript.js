let inputElement = document.getElementById("profile");
let a = document.getElementById("clearselect");

function showClear() {
  a.style.display = "block";
}
inputElement.addEventListener("click", showClear);
function clearInputField() {
  inputElement.value = "";
  a.style.display = "none";
}

a.addEventListener("click", clearInputField);
