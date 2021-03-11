const domain = window.location.origin;

function chooseGreeting(data) {
  let items = data.greetings;
  let greeting = document.getElementById('greeting');
  greeting.innerText = items[Math.floor(Math.random() * items.length)];
}

function updateGreeting() {
  fetch(domain + '/data/greetings.json')
    .then((resonse) => resonse.json())
    .then((data) => {
      chooseGreeting(data);
    });
}

window.onload = updateGreeting;
