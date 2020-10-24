const data = ["Personalised Results", "Users", "and", "Tweets"]
let index = 0;
let count = 0;
var text = "";

(function type() {
    text = data[count]

    letter = text.slice(0, ++index)
    document.querySelector("#type").textContent = letter;

    if (letter.length === text.length) {
        count++;
        index = 0;
        setTimeout(() => {}, 2000)
    }
    if (count === data.length) {
        count = 0;
    }
    setTimeout(type, 200)

}())