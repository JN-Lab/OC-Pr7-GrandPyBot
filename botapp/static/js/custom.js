// ----------------------------------
// Nav Management
// ----------------------------------

// Function to get the good section id to activate
function getSectionId(navLinkElt) {
  var sectionId = "";
  for (let link of navLinkElt) {
    if (/is-active/i.test(link.className)) {
      /#(.+)$/.exec(link.href);
      var regex = RegExp.$1;
      sectionId = regex;      
    }
  }
  return sectionId;
}

// Function to push "activate" class to the selected section
function setSectionActivation(sectionId, sectionElt) {
  for (let section of sectionElt) {
    if (section.id === sectionId) {
      section.className = "nav-element";
    } else {
      section.className = "nav-element inactive";
    }
  }
}

// function that link all operations

function manageSection(navLinkElt, sectionElt) {
  var sectionId = getSectionId(navLinkElt);
  setSectionActivation(sectionId, sectionElt);
}

// Function to switch is-active class when a nav link is clicked
function manageNavActiveClass(hrefLink, navLinkElt) {
  for (let link of navLinkElt) {
    if (link.href === hrefLink) {
      link.className = "nav-link is-active";
    } else {
      link.className = "nav-link";
    }
  }
}

/**
CODE EXECUTION
*/

var navLinkElt = document.getElementsByClassName("nav-link");

var sectionElt = document.getElementsByClassName("nav-element");

manageSection(navLinkElt, sectionElt);

for (let link of navLinkElt) {
  link.addEventListener("click", function(e) {
    var linkClicked = e.target;
    manageNavActiveClass(linkClicked.href, navLinkElt);
    manageSection(navLinkElt, sectionElt);
  });
}

// ----------------------------------
// Message Bubble Creation
// ----------------------------------

function setSpeechBubble(profile, message) {
  var bubbleElt = document.createElement("div");
  
  if (profile === "user") {
    bubbleElt.className = "card-bubble talk-right__simple";
  } else if (profile === "app") {
    bubbleElt.className = "card-bubble talk-left__simple";
  }
  
  var contentBubbleElt = document.createElement("div");
  contentBubbleElt.className = "card-bubble__text";
  contentBubbleElt.textContent = message;
  
  bubbleElt.appendChild(contentBubbleElt);
  document.getElementById("message-container").appendChild(bubbleElt);
}

function setMapBubble(latitude, longitude, address) {
  var bubbleElt = document.createElement("div");
  bubbleElt.className = "card";

  var mediaBubbleElt = document.createElement("div");
  mediaBubbleElt.className = "card-media";
  mediaBubbleElt.id = String((latitude + longitude) + Math.random());
  bubbleElt.appendChild(mediaBubbleElt);

  var linkBubbleElt = document.createElement("div");
  linkBubbleElt.className = "card-actions";
  var urlBubbleElt = document.createElement("a");
  urlBubbleElt.className = "card-actions__link";
  urlBubbleElt.textContent = "ITINERAIRE";
  urlBubbleElt.href = "https://www.google.com/maps/dir/?api=1&destination=" + address.replace(/\s+/g, "+");
  urlBubbleElt.target = "_blank";
  linkBubbleElt.appendChild(urlBubbleElt);
  bubbleElt.appendChild(linkBubbleElt);

  document.getElementById("message-container").appendChild(bubbleElt);
  initMap(latitude, longitude, mediaBubbleElt.id);
}

function setStoryBubble(title, text, link) {
  var bubbleElt = document.createElement("div");
  bubbleElt.className = "card";

  var titleBubbleElt = document.createElement("div");
  titleBubbleElt.className = "card-title";
  var titleTextElt = document.createElement("h2");
  titleTextElt.textContent = title;
  titleBubbleElt.appendChild(titleTextElt);
  bubbleElt.appendChild(titleBubbleElt);

  var contentBubbleElt = document.createElement("div");
  contentBubbleElt.className = "card-text";
  var textBubbleElt = document.createElement("p");
  textBubbleElt.textContent = text;
  contentBubbleElt.appendChild(textBubbleElt);
  bubbleElt.appendChild(contentBubbleElt);

  var linkBubbleElt = document.createElement("div");
  linkBubbleElt.className = "card-actions card-border-top";
  var urlBubbleElt = document.createElement("a");
  urlBubbleElt.className = "card-actions__link";
  urlBubbleElt.textContent = "PLUS D'INFOS";
  urlBubbleElt.href = link;
  urlBubbleElt.target = "_blank";
  linkBubbleElt.appendChild(urlBubbleElt);
  bubbleElt.appendChild(linkBubbleElt);

  document.getElementById("message-container").appendChild(bubbleElt);
}

function setLoaderBubble() {
  var preloaderElt = document.createElement("div");
  preloaderElt.id= "loader";
  preloaderElt.className = "spinner";
  document.getElementById("message-container").appendChild(preloaderElt);
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
// Ajax Interactions on Submit Button
// ----------------------------------

// Ajax Post function
function ajaxPost(url, data, callback, isJson) {
    var req = new XMLHttpRequest();
    req.open("POST", url);

    req.addEventListener("loadstart", function () {
      setLoaderBubble();
    })
    req.addEventListener("loadend", function () {
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