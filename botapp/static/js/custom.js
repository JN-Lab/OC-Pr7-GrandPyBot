// -------------------------------
// Nav Management Interactions
// -------------------------------

var infoButtonElt = document.getElementById("info-button");
var chatButtonElt = document.getElementById("chat-button");
var infoContainerElt = document.getElementById("info-container");
var chatContainerElt = document.getElementById("chat-container");

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

// ----------------------------------
// Message Bubble Creation
// ----------------------------------

function setUserSpeechBubble(message) {
  var bubbleElt = document.createElement("div");
  bubbleElt.className = "speech-element talk-bubble tri-right round right-in";
  bubbleElt.style.marginLeft = "60px";

  var speechBubbleElt = document.createElement("div");
  speechBubbleElt.className = "talktext";

  var textElt = document.createElement("p");
  textElt.textContent = message;
  speechBubbleElt.appendChild(textElt);
  bubbleElt.appendChild(speechBubbleElt);
  document.getElementById("message-historic").appendChild(bubbleElt);
}

// ----------------------------------
// Ajax Interactions on Submit Button
// ----------------------------------

// Ajax Post function
function ajaxPost(url, data, callback, isJson) {
    var req = new XMLHttpRequest();
    req.open("POST", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            // Appelle la fonction callback en lui passant la réponse de la requête
            callback(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Erreur réseau avec l'URL " + url);
    });
    if (isJson) {
        // Définit le contenu de la requête comme étant du JSON
        req.setRequestHeader("Content-Type", "application/json");
        // Transforme la donnée du format JSON vers le format texte avant l'envoi
        data = JSON.stringify(data);
    }
    req.send(data);
}

// Ajax Treatment
var formElt = document.querySelector("form");

formElt.addEventListener("submit", function(e) {
  var data = formElt.elements.message.value
  setUserSpeechBubble(data);

  ajaxPost("http://127.0.0.1:5000/treatment", data,
    function(response) {
      console.log(data);
      console.log(JSON.parse(response));
    },
    true
  );

  e.preventDefault();
});
