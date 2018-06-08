// -------------------------------
// Nav Management Interactions
// -------------------------------

var infoButtonElt = document.getElementById("info-button");
var chatButtonElt = document.getElementById("chat-button");
var infoContainerElt = document.getElementById("info-container");
var chatContainerElt = document.getElementById("chat-container");

// Click on Chat Button
chatButtonElt.addEventListener("click", function() {
  chatButtonElt.className = "message-nav-element nav-selected";
  infoButtonElt.className = "message-nav-element nav-unselected";
  chatContainerElt.style.display = "flex";
  infoContainerElt.style.display = "none";
});

// Click on Info Button
infoButtonElt.addEventListener("click", function() {
  chatButtonElt.className = "message-nav-element nav-unselected";
  infoButtonElt.className = "message-nav-element nav-selected";
  infoContainerElt.style.display = "flex";
  chatContainerElt.style.display = "none";
});

// ----------------------------------
// Message Bubble Creation
// ----------------------------------

function setSpeechBubble(profile, message) {
  var bubbleElt = document.createElement("div");

  if (profile === "user") {
    bubbleElt.className = "speech-element talk-bubble tri-right round right-in scale-transition scale-in";
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

function setMapBubble(latitude, longitude, address) {
  var bubbleElt = document.createElement("div");
  bubbleElt.className = "card blue-grey darken-1 z-depth-0";

  var mapBubbleElt = document.createElement('div');
  mapBubbleElt.className = "card-image";
  mapBubbleElt.style.height = "300px";
  mapBubbleElt.style.width = "100%";
  mapBubbleElt.id = String((latitude + longitude) + Math.random());
  bubbleElt.appendChild(mapBubbleElt);

  var linkBubbleElt = document.createElement("div");
  linkBubbleElt.className = "card-action";
  var urlBubbleElt = document.createElement("a");
  urlBubbleElt.textContent = "ITINERAIRE";
  urlBubbleElt.href = "https://www.google.com/maps/dir/?api=1&destination=" + address.replace(/\s+/g, "+");
  urlBubbleElt.target = "_blank";
  linkBubbleElt.appendChild(urlBubbleElt);
  bubbleElt.appendChild(linkBubbleElt);

  document.getElementById("bubble-container").appendChild(bubbleElt);
  initMap(latitude, longitude, mapBubbleElt.id);
}

function setStoryBubble(title, text, link) {
  var bubbleElt = document.createElement("div");
  bubbleElt.className = "card blue-grey darken-1 z-depth-0";

  var contentBubbleElt = document.createElement("div");
  contentBubbleElt.className = "card-content white-text";
  var titleBubbleElt = document.createElement("span");
  titleBubbleElt.className = "card-title";
  titleBubbleElt.textContent = title;
  var textBubbleElt = document.createElement("p");
  textBubbleElt.textContent = text;
  contentBubbleElt.appendChild(titleBubbleElt);
  contentBubbleElt.appendChild(textBubbleElt);
  bubbleElt.appendChild(contentBubbleElt);

  var linkBubbleElt = document.createElement("div");
  linkBubbleElt.className = "card-action";
  var urlBubbleElt = document.createElement("a");
  urlBubbleElt.textContent = "PLUS D'INFOS";
  urlBubbleElt.href = link;
  urlBubbleElt.target = "_blank";
  linkBubbleElt.appendChild(urlBubbleElt);
  bubbleElt.appendChild(linkBubbleElt);

  document.getElementById("bubble-container").appendChild(bubbleElt);
}

function setLoaderBubble() {
  var preloaderElt = document.createElement("div");
  preloaderElt.id = "loader";
  preloaderElt.className = "loader-position speech-element preloader-wrapper active";
  preloaderElt.style.marginRight = "60px";
  var spinnerElt = document.createElement("div");
  spinnerElt.className = "spinner-layer spinner-blue-only";

  var clipperElt = document.createElement("div");
  clipperElt.className = "circle-clipper left";
  var circleClipperElt = document.createElement("div");
  circleClipperElt.className = "circle";
  clipperElt.appendChild(circleClipperElt);

  var gapElt = document.createElement("div");
  gapElt.className = "gap-patch";
  var circleGapElt = document.createElement("div");
  circleGapElt.className = "circle";
  gapElt.appendChild(circleGapElt);

  var rightElt = document.createElement("div");
  rightElt.className = "circle-clipper right";
  var circleRightElt = document.createElement("div");
  circleRightElt.className = "circle";
  rightElt.appendChild(circleRightElt);

  spinnerElt.appendChild(clipperElt);
  spinnerElt.appendChild(gapElt);
  spinnerElt.appendChild(rightElt);

  preloaderElt.appendChild(spinnerElt);
  document.getElementById("bubble-container").appendChild(preloaderElt);
}

// -----------------------------------------------------
// Get the Google Map with an API call
// -----------------------------------------------------

function initMap(latitude, longitude, divId) {
  var location = {lat: latitude, lng: longitude};
  var map = new google.maps.Map(document.getElementById(divId), {
    zoom: 15,
    center: location,
    gestureHandling: "cooperative"
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
    setMapBubble(response.latitude, response.longitude, response.address);
    setSpeechBubble("app", "Voici également ce que j'ai trouvé comme élément sur ce lieux");
    setStoryBubble(response.title, response.intro, response.page_link);
    console.log("switch structure OK:" + response.status);
    break;
  case "STORY_MISSING":
    setSpeechBubble("app", "Je connais l'endroit. Voici son addresse : " + response.address);
    setMapBubble(response.latitude, response.longitude, response.address);
    setSpeechBubble("app", "En revanche, je n'ai pas beaucoup d'informations sur l'histoire de ce lieux. Je vais tenter d'en trouver pour la prochaine fois!");
    console.log("switch structure OK:" + response.status);
    break;
  case "GOOGLE_GEOCODING_API_PROBLEM":
    setSpeechBubble("app", "Ah! Je rencontre un problème pour récupérer les coordonnées. C'est assez rare. Cela devrait revenir très rapidement.");
    console.log("switch structure OK:" + response.status);
    break;
  case "WIKIMEDIA_API_PROBLEM":
    setSpeechBubble("app", "Je connais l'endroit. Voici son addresse : " + response.address);
    setMapBubble(response.latitude, response.longitude, response.address);
    setSpeechBubble("app", "En revanche, je n'ai pas beaucoup d'informations sur l'histoire de ce lieux. Je vais tenter d'en trouver pour la prochaine fois!");
    console.log("switch structure OK:" + response.status);
    break;
  }
}

// ----------------------------------
// Waiting loader
// ----------------------------------

function waitingMessage() {
  var messageElt = document.getElementById("status-text");
  var loaderElt = document.getElementById('status-loading');
  messageElt.textContent = "laissez-moi réfléchir"
  messageElt.style.display = "inline";
  loaderElt.style.display = "inline";
  var count = 0;
  if (count < 3) {
    loaderElt.textContent += ".";
    count += 1;
    console.log(loaderElt.textContent);
    console.log(count);
  } else {
    loaderElt.textContent = "";
  }
}

// ----------------------------------
// Ajax Interactions on Submit Button
// ----------------------------------

// Ajax Post function
function ajaxPost(url, data, callback, isJson) {
    var req = new XMLHttpRequest();
    req.open("POST", url);

    req.addEventListener("loadstart", function () {
      var IntervalId = setInterval(waitingMessage(), 10);
      setLoaderBubble();
    })
    req.addEventListener("loadend", function () {
      var messageElt = document.getElementById("status-text");
      var loaderElt = document.getElementById('status-loading');
      messageElt.style.display = "none";
      loaderElt.style.display = "none";

      var loaderElt = document.getElementById("loader");
      loaderElt.remove();
    })
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

setSpeechBubble("app", "Bonjour! Cherchez-vous des informations sur un lieu?");
