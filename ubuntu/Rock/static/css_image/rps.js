var comp = document.createElement("BUTTON");
var node = document.createTextNode("This is a new paragraph.");
var element = document.getElementById("compAnswer");
let answers = ["Rock", "Paper", "Scissors"];

var total_wins = 0;

function random() { return Math.floor(Math.random() * 3-1) + 1;}

let answer = document.querySelector('#answer')
        document.querySelector('#rock').onclick = function() {
            answer.innerHTML = "Rock";
            comp.appendChild(node);
            let int = random ()
            comp.innerHTML= answers[int]
            element.appendChild(comp);

            let a = answer.innerHTML;
            let b = comp.innerHTML;
            let result = winner(a,b);

            update_results(result, total_wins)

        }
        document.querySelector('#paper').onclick = function() {
            answer.innerHTML = "Paper"
            comp.appendChild(node);
            let int = random ()
            comp.innerHTML= answers[int]
            element.appendChild(comp);

            let a = answer.innerHTML;
            let b = comp.innerHTML;
            let result = winner(a,b);

            update_results(result, total_wins)
        }
        document.querySelector('#scissors').onclick = function() {
            answer.innerHTML="Scissors"
            comp.appendChild(node);
            let int = random ()
            comp.innerHTML= answers[int]
            element.appendChild(comp);

            let a = answer.innerHTML;
            let b = comp.innerHTML;
            let result = winner(a,b);

            update_results(result, total_wins)
        }


function winner (a,b) {
    var awins = 0;
    var alosses = 0;
    var ties = 0;

    if(a == b) ties++;
    else {
             if(a=="Rock" && b=="Scissors") awins++;
        else if(a=="Rock" && b=="Paper") alosses++;
        else if(a=="Paper" && b=="Scissors") alosses++;
        else if(a=="Paper" && b=="Rock") awins++;
        else if(a=="Scissors" && b=="Paper") awins++;
        else if(a=="Scissors" && b=="Rock") alosses++;
    }

    if (awins > 0) {
        total_wins++;
        return "You Win"
    }

    if (alosses > 0) {
        return "You Lose"
    }

    if (ties > 0) {
        return "It's a tie"
    }
}


function update_results (result, total_wins) {

    var element = document.getElementById("win");
    element.innerHTML= result

    if (result == "You Win") {
        var winCount = document.getElementById("winCount")
        winCount.innerHTML = total_wins
    }
}