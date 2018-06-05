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

function setSpeechBubble(profile, message) {
  var bubbleElt = document.createElement("div");

  if (profile === "user") {
    bubbleElt.className = "speech-element talk-bubble tri-right round right-in";
    bubbleElt.style.marginLeft = "60px";
  } else if (profile === "app") {
    bubbleElt.className = "speech-element talk-bubble tri-right round left-in";
    bubbleElt.style.marginLeft = "30px";
    bubbleElt.style.backgroundColor = "#A3BDED";
  }

  var speechBubbleElt = document.createElement("div");
  speechBubbleElt.className = "talktext";

  var textElt = document.createElement("p");
  textElt.textContent = message;
  speechBubbleElt.appendChild(textElt);
  bubbleElt.appendChild(speechBubbleElt);
  document.getElementById("bubble-container").appendChild(bubbleElt);
}

function setMapBubble(latitude, longitude) {
  var bubbleElt = document.createElement("div");
  bubbleElt.className = "speech-element talk-bubble round";
  bubbleElt.style.marginLeft = "30px";
  bubbleElt.style.height = "250px";
  bubbleElt.style.width = "90%";
  bubbleElt.id = String((latitude + longitude) + Math.random());
  document.getElementById("bubble-container").appendChild(bubbleElt);
  initMap(latitude, longitude, bubbleElt.id);
}

// -----------------------------------------------------
// Get the Google Map with an API call
// -----------------------------------------------------

function scriptGoogleApi(apiKey) {
  var scriptElt = document.createElement("script");
  scriptElt.src = "https://maps.googleapis.com/maps/api/js?key=" + apiKey + "&callback=initMap";
  document.body.appendChild(scriptElt);
}

function initMap(latitude, longitude, divId) {
  var location = {lat: latitude, lng: longitude};
  var map = new google.maps.Map(document.getElementById(divId), {
    zoom: 15,
    center: location
  });
  var marker = new google.maps.Marker({
    position: location,
    map: map
  });
}

// -----------------------------------------------------
// Manage the different response according JSON received
// -----------------------------------------------------

function setResponse(response) {
  switch (response.status) {
  case "LOCATION_MISSING":
    setSpeechBubble("app", "Merci pour votre message. Dîtes moi où vous souhaitez aller?");
    console.log("switch structure OK: " + response.status);
    break;
  case "WRONG_LOCATION":
    setSpeechBubble("app", "Merci pour votre message. Je ne suis pas sûr d'avoir bien compris où vous souhaitez aller. Pouvez-vous répéter s'il vous plait?");
    console.log("switch structure OK: " + response.status);
    break;
  case "COMPLETE":
    setSpeechBubble("app", "Je connais l'endroit. Voici son addresse : " + response.address);
    setMapBubble(response.latitude, response.longitude);
    setSpeechBubble("app", response.intro);
    console.log("switch structure OK:" + response.status);
    break;
  case "STORY_MISSING":
    setSpeechBubble("app", "Je connais l'endroit. Voici son addresse : " + response.address);
    setMapBubble(response.latitude, response.longitude);
    setSpeechBubble("app", "En revanche, je n'ai pas beaucoup d'informations sur l'histoire de ce lieux. Je vais tenter d'en trouver pour la prochaine fois!");
    console.log("switch structure OK:" + response.status);
    break;
  case "GOOGLE_GEOCODING_API_PROBLEM":
    setSpeechBubble("app", "Ah! Je rencontre un problème pour récupérer les coordonnées. C'est assez rare. Cela devrait revenir très rapidement.");
    console.log("switch structure OK:" + response.status);
    break;
  case "WIKIMEDIA_API_PROBLEM":
    setSpeechBubble("app", "Je connais l'endroit. Voici son addresse : " + response.address);
    setMapBubble(response.latitude, response.longitude);
    setSpeechBubble("app", "En revanche, je n'ai pas beaucoup d'informations sur l'histoire de ce lieux. Je vais tenter d'en trouver pour la prochaine fois!");
    console.log("switch structure OK:" + response.status);
    break;
  }
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

  if (data) {
    setSpeechBubble("user", data);

    ajaxPost("http://127.0.0.1:5000/treatment", data,
      function(response) {
        response = JSON.parse(response);
        console.log(data);
        console.log(response);
        setResponse(response);
        if ((response.status === "LOCATION_MISSING") || (response.status === "WRONG_LOCATION")) {
          formElt.elements.message.value = "Je souhaiterais aller...";
        } else {
          formElt.elements.message.value = "";
        }
      },
      true
    );
  } else {
    setSpeechBubble("app", "Veuillez indiquez votre recherche avant d'envoyer");
  }
  e.preventDefault();
});

// ----------------------------------
// Start initialisation
// ----------------------------------

scriptGoogleApi("YOUR_API_KEY");
setSpeechBubble("app", "Bonjour! Cherchez-vous des informations sur un lieu?");
