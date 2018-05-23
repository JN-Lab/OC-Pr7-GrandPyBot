// -------------------------------
// Nav Management Interactions
// -------------------------------

infoButtonElt = document.getElementById("info-button");
chatButtonElt = document.getElementById("chat-button");
infoContainerElt = document.getElementById("info-container");
chatContainerElt = document.getElementById("chat-container");

// Click on Chat Button
chatButtonElt.addEventListener("click", function() {
  chatButtonElt.style.color = "#F9AA33";
  chatButtonElt.style.backgroundColor = "#FFFFFF";
  infoButtonElt.style.color = "#232F34";
  infoButtonElt.style.backgroundColor = "#CFD8DC";
  chatContainerElt.style.display = "flex";
  infoContainerElt.style.display = "none";
});

// Click on Info Button
infoButtonElt.addEventListener("click", function() {
  infoButtonElt.style.color = "#F9AA33";
  infoButtonElt.style.backgroundColor = "#FFFFFF";
  chatButtonElt.style.color = "#232F34";
  chatButtonElt.style.backgroundColor = "#CFD8DC";
  infoContainerElt.style.display = "flex";
  chatContainerElt.style.display = "none";
});
